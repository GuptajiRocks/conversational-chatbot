from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/textacc", methods=["POST"])
def accept_prompt():
    # prompt = request.args.get("message")
    # print(prompt)

    data = request.get_json()
    prompt = data.get('message', '')
    print(f"Received Message: {prompt}")

    return render_template("test.html", mess=prompt)


if __name__ == "__main__":
    app.run(debug=True)
