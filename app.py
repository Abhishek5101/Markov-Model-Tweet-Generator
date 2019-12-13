from flask import Flask, render_template
from sampling import sample, histogram
from markov import sentence_generator

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', sentence=sentence_generator())


if __name__ == "__main__":
	app.run(debug=True)