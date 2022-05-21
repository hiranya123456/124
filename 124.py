from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'blink',
        'number': u'9228546739', 
        'done': False
    },
    {
        'id': 2,
        'name': u'jennie',
        'number': u'994538024', 
        'done': False
    }
]

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)
    contacts = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'number': request.json.get('number', ""),
        'done': False
    }
    contacts.append(contacts)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
