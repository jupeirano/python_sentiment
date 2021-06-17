import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Twitter Sentiment Analysis</h1><p>API in construction</p>"

app.run()