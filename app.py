from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Define the correct username and password
correct_username = 'user'
correct_password = 'password'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form['username']
    password = request.form['password']

    # Check if the username and password match the correct credentials
    if username == correct_username and password == correct_password:
        # Execute the SensoryConnect.py file
        subprocess.Popen(['python', 'Sensory.py'])
        return render_template('home.html', username=username)
    else:
        return "Invalid login. Please try again."

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
