from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    with open('dummy.txt', 'r') as fp:
        data = fp.read()
    return data
@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        data = request.form['data']
        with open('dummy.txt', 'a') as fp:
            fp.write(data)
        return jsonify({"result": "success"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)

