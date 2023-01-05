import boto3, os, json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
load_dotenv()

app = Flask(__name__)
api = Api(app)
CORS(app)


s3 = boto3.resource(
    's3',
    region_name=os.getenv("REGION_NAME"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
    endpoint_url=os.getenv("ENDPOINT_URL")
)

    

class _s3(Resource):
    def get(self):
        result = {'status':"LMAO"}
        return jsonify(result)

    def post(self):
        value_file = request.files['data']
        type_file = value_file.content_type
        filename = secure_filename(value_file.filename)
        try:
            s3.meta.client.upload_file(filename,os.getenv("BUCKET_NAME"),filename, ExtraArgs={'ContentType': type_file})
            response = {'ok':value_file.filename}
        except Exception as e:
            response = {'err':e}

        return jsonify(response)            

api.add_resource(_s3,"/")
if __name__ == "__main__":
	app.run(debug=True,port=80)

#cdn access = https://cdn.comnetbe.my.id/