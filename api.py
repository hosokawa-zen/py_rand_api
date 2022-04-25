from crypt import methods
from flask import Flask, request
import random

app = Flask(__name__)
app.debug = True

@app.route("/", methods=["GET"])
def home():
    fromnum = request.args.get("from")
    if(fromnum is None):
        fromnum = 1
    else :
        fromnum = int(fromnum)
    tonum = request.args.get("to")
    if(tonum is None):
        tonum = 1000
    else :
        tonum = int(tonum)
    result = random.randint(fromnum, tonum)
    return str(result)

app.run()