from classifier import *
from flask import request, render_template, Flask

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get("email_text")
        category = classify_email(text)

        if category is None:
            return error(400, "Não foi possível categorizar o email.")

        response = generate_response(text, category)

        return render_template(
            "index.html",
            result=category,
            response=response,
            text=text
        )

    return render_template("index.html")

@app.post("/upload")
def file_email():
    file = request.files.get("email_file")

    if not file or not file.filename.endswith((".pdf",".txt")):
        return error(400, "Envie arquivos .pdf ou .txt!")

    if file.filename.endswith(".txt"):
        email_txt = file.read().decode("utf-8")
        category = classify_email(email_txt)

        if category is None:
            return error(400, "Não foi possível categorizar o email.")

        response = generate_response(email_txt, category)
        return render_template(
            "index.html",
            result=category,
            response=response
        )


    email_text = extrair_pdf(file)
    category = classify_email(email_text)

    if category is None:
        return error(400, "Não foi possível categorizar o email.")
    response = generate_response(email_text, category)

    return render_template(
        "index.html",
        result=category,
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True)
