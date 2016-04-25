#!flask/bin/python

from flask import Flask, request, render_template, jsonify, make_response
app = Flask(__name__, static_url_path='/static')

FILENAME="buzz.dat"

@app.route('/', methods=['POST'])
def buzz():
    print "in buzz route"
    open(FILENAME, 'w').write(request.form['buzz'])
    resp = make_response("OK")
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3001)

