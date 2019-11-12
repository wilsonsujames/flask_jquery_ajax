from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    print("add number")
    a = request.args.get('a')
    b = request.args.get('b')
    print()
    print()
    result=int(a)+int(b)
    return jsonify(result=result)

@app.route('/')
def index():
    return render_template('index.html')
	
	

if __name__ == "__main__":
    app.run(debug=True)	