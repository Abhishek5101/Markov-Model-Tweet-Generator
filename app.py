from flask import Flask
from sampling import sample, histogram


app = Flask(__name__)


@app.route('/')
def index():
	return sample(histogram('one two fish three fish red blue fish fish fish fish'))