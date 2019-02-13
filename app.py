from flask import Flask
from flask import request
from tools import linkfinder
import json



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/jsfinduri/')
def jsfinduri():                      #未作 ip限制过滤  防止ssrf
    url = request.args.get('uri')
    file = linkfinder.send_request(url)
    endpoints = linkfinder.parser_file(file, linkfinder.regex_str, mode=0)
    return json.dumps({"domain":url,"link":[endpoint for endpoint in endpoints]})


if __name__ == '__main__':
    app.run(debug=True)   #host='0.0.0.0'
