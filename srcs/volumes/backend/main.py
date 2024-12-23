import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return "Airbnb data analysis Backend is running!"

@app.route('/api/postdata', methods=['POST'])
def post_data():
    # Get user input from the request
    logging.info('--------------------------------------------')
    data = request.get_json()
    stock = data.get('stock', '')

    
    if not stock:
        return jsonify({"error": "No city provided"}), 400
    
		# Open and parse the file
    # data = open_and_parse_file(stock)

    if data.get('error'):
        return jsonify(data), 400
    
    # Create a json response
    return jsonify({
				'stock': stock,
		})
    
if __name__ == '__main__':
    app.run(debug=True)
