from flask import Flask, request, render_template, jsonify
import gunicorn

app_name = "Python App With Flask, HTML, And REST"
app = Flask(app_name)
client = "VMware"
framework = "Python with Pipenv"

messages = [
    {
        'client':client,
        'framework':framework,
        'msg_subject':'Secure Software Supply Chains Are Great!', 
        'msg_body':'With A Secure Software Supply Chain, Deploying Python Code To PROD is Safe, Reliable, And Fast!'
    }
]

@app.route("/")
def hello():
    return render_template('index.html', client=client, framework=framework)

@app.route('/messages')
def get_incomes():
    return jsonify(messages)

@app.route('/versions')
def versions():
    gu_version = gunicorn.__version__
    return "Gunicorn version: " + gu_version

app.debug=False
