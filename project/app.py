from classifier import *
from flask import request, render_template, Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    response = None
    text = ""

    if request.method == "POST":
        text = request.form.get("email_text")

        if text:
            category = classify_email(text)
            response = generate_response(category)
            result = category

    return render_template(
        "index.html",
        result=result,
        response=response,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)
