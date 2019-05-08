from flask import Flask,jsonify,json, request
from gevent.pywsgi import WSGIServer
from blockchain import createwallet
import json
app = Flask(__name__)

@app.route('/register', methods=['GET'])
def register():
    wallet = createwallet.create_wallet('1234password', '58ck39ajuiw', 'http://127.0.0.1:3000/', label = 'Test wallet',email='devod0485@gmail.com')
    return jsonify({'address': wallet.address,'guid': wallet.identifier,'label':wallet.label})

#
# @app.route('/api/v2/create', methods=['GET','POST'])
# def create():
#     print("yes in create ======================")



if __name__ == '__main__':
   app.run(debug=True)
   # http_server = WSGIServer(('127.0.0.1', 5000), app)
   # http_server.serve_forever()