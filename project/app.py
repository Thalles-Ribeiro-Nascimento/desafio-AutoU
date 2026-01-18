from classifier import *
from flask import request, render_template, Flask

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/")
def text_email():
    text = request.form.get("email_text")

    if text == "":
        return render_template("index.html", error="Não há email para classificar!")

    category = classify_email(text)
    response = generate_response(text, category)

    return render_template(
        "index.html",
        result=category,
        response=response,
        text=text
    )

@app.post("/upload")
def file_email():
    file = request.files.get("email_file")

    if not file or not file.filename.endswith((".pdf",".txt")):
        return "Por favor, envie apenas arquivos PDF ou TXT."

    if file.filename.endswith(".txt"):
        email_txt = file.read().decode("utf-8")

        category = classify_email(email_txt)
        response = generate_response(email_txt, category)
        return render_template(
            "index.html",
            result=category,
            response=response
        )

    email_text = extrair_pdf(file)

    if not email_text:
        return "Não foi possível extrair texto do PDF."

    category = classify_email(email_text)
    response = generate_response(email_text, category)

    return render_template(
        "index.html",
        result=category,
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True)
