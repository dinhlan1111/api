from flask import Flask, render_template, request, json



# Doan ma khoi tao server
app = Flask(__name__)


# Khai bao ham xu ly request inde
@app.route("/")
def main():
    return render_template('index.html')

# Khai bao ham xu ly request detect
@app.route('/api/recognize', methods=['POST'])
def detect():

    # Lay du lieu image B64 gui len va chuyen thanh image
    image_b64 = json.loads(request.data)['code']
    print (image_b64)
    
    res = "test"

    
    print (res)
    return json.dumps(res)


# Thuc thi server
if __name__ == '__main__':
    app.run(debug=True)
