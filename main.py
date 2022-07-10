from flask import Flask, render_template
from requests import Session


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/ip=<ip>")
def check_geo_ip(ip):
    ses = Session()
    try:
        res = ses.get('https://ipinfo.io/' + ip + '/json').json()["country"]
        return {"code":"200", "country": res}
    except:
        return {"code":"400", "message": f"can't check GEO {ip}"}


@app.route('/login')
def login():
    return 'have nothing v3'


@app.route('/redirect')
def redirect():
    return render_template("redirect.html")


# git 'https://github.com/khimnguynn/learn_jenkins.git'


if __name__ == '__main__':
    app.run()