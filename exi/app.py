from flask import Flask


app = Flask(__name__)
app.config.from_object('exi.settings.Config')
app.config.from_envvar('EXI_SETTINGS', silent=True)


@app.route('/')
def hello_world():
    return 'Hello World! Yeah!'
