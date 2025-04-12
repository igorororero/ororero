
# uproszczona wersja — w Twoim pliku będzie pełny kod z canvas
import json
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/callback")
def callback():
    return "Działa!"

if __name__ == "__main__":
    app.run()
