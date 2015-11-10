import json

from flask import Flask
from flask import render_template
from flask import request

from es3_to_special import gen_for_class

app = Flask(__name__)

@app.route('/')
def index():

	value = request.args.get('value')

	if value:
		return json.dumps(gen_for_class(value))

	return render_template('index.html')

if __name__ == '__main__':
	app.run()