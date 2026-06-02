from flask import Flask, render_template, request
from services.fizzbuzz_service import generate_fizzbuzz

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/the-app", methods=["GET", "POST"])
def the_app():
    results = []

    if request.method == "POST":
        print("POST received", flush=True)
        fizz_value = int(request.form["fizz_value"])
        buzz_value = int(request.form["buzz_value"])
        stop_value = int(request.form["stop_value"])

        results = generate_fizzbuzz(fizz_value, buzz_value, stop_value)
        print(results, flush=True)

    return render_template("the-app.html", results=results)


@app.route("/the-code")
def the_code():
    return render_template("the-code.html")


if __name__ == "__main__":
    app.run(debug=True)
