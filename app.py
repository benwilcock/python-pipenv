from flask import Flask, request, render_template, jsonify
import gunicorn

app_name = "Python App With Flask, HTML, And REST"
app = Flask(app_name)

messages = [
    {
        'msg_subject':'Secure Software Supply Chains Are Great!', 
        'msg_body':'With A Secure Software Supply Chain, Deploying Python Code To PROD is Safe, Reliable, And Fast!'
    }
]

@app.route("/")
def hello():
    client = "VMware"
    return render_template('index.html', client=client)

@app.route('/messages')
def get_incomes():
    return jsonify(messages)

@app.route('/versions')
def versions():
    gu_version = gunicorn.__version__
    return "Gunicorn version: " + gu_version

app.debug=False
