from flask import Flask, render_template, request, json
import socket

app = Flask(__name__)

ip = socket.gethostbyname(socket.gethostname())


@app.route("/")
def main():
    test = "test"
    return test


@app.route("/api/recognize", methods=['POST'])
def detect():
    imageString = json.loads(request.data)['code']
    print(imageString)
    res = "test"
    
    return json.dumps(res)


if __name__ == "__main__":
    app.run(debug=True)
