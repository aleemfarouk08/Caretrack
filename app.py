
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to CareTrack</h1>
    <h2>Residential Childcare Management System</h2>
    <p>Supporting safer care and better documentation.</p>
    <p>CareTrack Version 0.1</p>
    """

if __name__ == "__main__":
    app.run()
