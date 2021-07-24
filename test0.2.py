import os, sys
from flask import Flask
from flask import jsonify
from flask import make_response

from flask import request
from flask_restful import Api
from flask_restful import Resource

exporting_threads = {}
app = Flask(__name__)
api = Api(app)

class SimpleApi(Resource):

	def get(self):
		data = {
			"name":"Yusran",
			"company": "Jawdat Teknologi",
			"role": "Engineer"
		}
	return make_response(jsonify(data))

api.add_resource(SimpleApi, '/data/')

if (__name__) == '__main__':
	port = int(os.environ.get('PORT', 4242))
	app.run(host="0.0.0.0", debug=True, port=port, threaded=True)