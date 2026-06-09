import flask
app = flask.Flask(__name__)





@app.route('/test', methods=['POST'])
def test():
    data = flask.request.json
    print(data)
    return "Test Confirmed"








if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5204)