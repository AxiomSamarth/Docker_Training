from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Welcome to Flask Web App hosted on Azure!"

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
