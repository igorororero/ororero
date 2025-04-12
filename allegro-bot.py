from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot działa! Flask jest uruchomiony na Render."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render ustawia PORT w zmiennych środowiskowych
    app.run(host="0.0.0.0", port=port)
