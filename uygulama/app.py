import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    ortam_degiskeni = os.getenv("APP_NAME")
    return f"Merhaba Dünya. Bu ortam degiskeninde calisiyorum: {ortam_degiskeni}"

if __name__ == "__main__":
    app.run()