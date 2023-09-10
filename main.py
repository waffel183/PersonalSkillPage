from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "hello! this is main page <h1>hello</h1>"

if __name__ == "__main__":
    app.run()