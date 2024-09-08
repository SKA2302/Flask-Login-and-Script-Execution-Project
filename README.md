# SimpleLoginSystem

**SimpleLoginSystem** is a basic Flask application designed to authenticate users via a login form. Upon successful login, it triggers the execution of a Python script. The system uses hardcoded credentials for authentication and redirects users to a home page once authenticated.

## Features

- **User Authentication**: Validates users through a simple login form with hardcoded credentials.
- **Script Execution**: Executes the `Sensory.py` script in the background upon successful login.
- **User Interface**: Provides a straightforward and easy-to-understand Flask-based interface.

## Technologies Used

- **Flask**: Web framework used for developing the backend.
- **HTML/CSS**: Used for creating the frontend interface.
- **Python subprocess**: Utilized for executing the external `Sensory.py` script.


### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Flask


## Usage

1. **Run the Flask Application:**
    ```bash
    python app.py
    ```

2. **Open Your Browser:**
    Navigate to `http://localhost:5000` to access the login page.

3. **Login:**
    Enter the correct username and password to trigger the execution of python file and be redirected to the home page.


