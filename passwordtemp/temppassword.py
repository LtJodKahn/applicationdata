from flask import request, Flask
import random
import string
import json, socket

app = Flask(__name__)

#
# curl http://localhost:9000
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"password\" : \"xxxxxxxx\" }" -X POST http://localhost:9001/check  -H "Content-type: application/json"
#

@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    password = request.json['password']
    password_length = len(password)

    returnDictionary = {}
    returnDictionary["password"] = password
    returnDictionary["length"] = password_length
    
    attemptedpassword = request.json['password']
    
    if returnDictionary["password"] == attemptedpassword:
      returnDictionary["success"] = True
    else:
      characters = string.ascii_letters + string.digits + string.punctuation
      password = ''.join(random.choice(characters) for i in range(7))
      returnDictionary["success"] = False
      returnDictionary["password"] = password
      #alert the account
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)
      
      #alert the account
