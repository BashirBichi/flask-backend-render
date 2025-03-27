from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask API!"})

# Home Route (Optional for local testing)
@app.route('/')
def home():
    return render_template('index.html')

# Form Handling (Example)
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form.get('name')
    return jsonify({"response": f"Hello, {data}!"})

if __name__ == '__main__':
    app.run(debug=True)