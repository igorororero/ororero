from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Działa! ✅ Bot uruchomiony na Render."

if __name__ == "__main__":
    # Dla Render: nasłuchuj na 0.0.0.0 (nie localhost!) i na porcie 5000
    app.run(host="0.0.0.0", port=5000)
