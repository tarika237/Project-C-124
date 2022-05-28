from flask import Flask,request,jsonify

app = Flask(__name__)

tasks = [
    {
    "id":1,
    "Contact":u"9667556234",
    "Name":u"Sia",
    "Done":False
    }
]

@app.route("/addDATA",methods = ["POST"])
def task():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "Message":"Please provide data"
        },400)

    task = {
        "id":tasks[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get["Contact",""],
        "Done":False
    }
    tasks.append(task)

    return jsonify({
        "status":"SUCCESS",
        "message":"Task added successfully"     
    })

@app.route("/getDATA")
def getTasl():
    return jsonify({
        "data":tasks
    })

app.run()




