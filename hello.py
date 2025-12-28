from flask import Flask

app = Flask(__name__) # __name__ -> "hello.py"


@app.route("/") # endpoint. When user visits "/", this function is automatically     called.
def hello():
    return "Hello, there.!"


@app.route("/ping", methods=['GET', 'POST']) # only respond to GET and POST requests
def ping():
    return {"message": "why are you pinging me?"}


if __name__ == "__main__":
    app.run(debug=True)  # debug=True -> auto-reload server on code changes