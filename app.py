from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My DevOps Project!</h1>
    <h2>CI/CD Pipeline Successfully Running</h2>
    <p>Deployed using Docker and Flask.</p>
    <p>My AWS and DevOps Journey!</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)