import searchData
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

custom_put_args = reqparse.RequestParser()
custom_put_args.add_argument("definition", type=str, help='Definition of the word here', required=True)

@app.route("/")
def home():
    return 'This is wordapi'


class Define(Resource):
    def get(self, word):
        ls = searchData.searchWord(word)
        return jsonify({'definition': ls})
    
    def post(self):
        return

    
class Custom(Resource):
    def get(self, word):
        return searchData.searchCustom(word)
    
    def put(self, word):
        args = custom_put_args.parse_args()
        return searchData.putCustom(word, defn=args['definition'])

api.add_resource(Define, '/define/<string:word>')
api.add_resource(Custom, '/custom/<string:word>')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
