from flask import Flask, request, jsonify
import prometheus_client
from prometheus_client import Counter

app = Flask(__name__)

# Define a Prometheus counter to track the number of requests to each endpoint.
REQUEST_COUNT = Counter('request_count', 'Number of requests received', ['endpoint'])

def fibonacci(n):
    """Compute the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    REQUEST_COUNT.labels(endpoint='/health').inc()
    return "200 OK", 200

@app.route('/get', methods=['GET'])
def get_fibonacci():
    """Endpoint to get the Fibonacci sequence up to a given number 'n'."""
    REQUEST_COUNT.labels(endpoint='/get').inc()
    
    # Get the query parameter 'n'
    n_str = request.args.get('n')
    if n_str is None:
        return jsonify({"error": "Missing 'n' parameter"}), 400

    try:
        n = int(n_str)
    except ValueError:
        return jsonify({"error": "'n' must be an integer"}), 400

    if n < 0:
        return jsonify({"error": "'n' must be a non-negative integer"}), 400

    # Calculate Fibonacci sequence up to n
    result = [fibonacci(i) for i in range(n + 1)]
    return jsonify(result), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    """Endpoint to expose Prometheus metrics."""
    return prometheus_client.generate_latest(), 200

# Run the Flask app.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
