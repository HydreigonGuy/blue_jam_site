
from flask import Flask, render_template

app = Flask(__name__, static_folder="static/")


@app.route('/')
def home():
    return render_template("home.html")

def main():
    app.run(host="0.0.0.0", port=5004)

if __name__ == "__main__":
    main()