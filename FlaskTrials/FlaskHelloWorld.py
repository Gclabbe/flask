from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<username>')
def hello(username = None):
	return render_template('hello.html', name = username)

if __name__ == "__main__":
	app.run()
