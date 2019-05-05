from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   data = json.loads(request.data)
   #print(data)
   connection.privmsg(event.target,("New commit by: {} message {} ID:{}".format(data['commits'][0]['author']['name'],data['commits'][0]['message'],data['ref'])))
   return "OK"

if __name__ == '__main__':
   app.run(host='0.0.0.0')


