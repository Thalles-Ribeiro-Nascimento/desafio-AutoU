from classifier import *
from flask import request, render_template, Flask

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/")
def text_email():
    text = request.form.get("email_text")
    category = classify_email(text)
    response = generate_response(text, category)
    result = category

    return render_template(
        "index.html",
        result=result,
        response=response,
        text=text
    )

@app.post("/upload")
def file_email():
    file = request.files.get("email_file")

    if not file or not file.filename.endswith((".pdf",".txt")):
        return "Por favor, envie apenas arquivos PDF ou TXT.", 400

    if file.filename.endswith(".txt"):
        email_txt = file.read().decode("utf-8")

        category = classify_email(email_txt)
        response = generate_response(email_txt, category)
        return render_template(
            "index.html",
            category=category,
            reply=response
        )

    email_text = extrair_pdf(file)

    if not email_text:
        return "Não foi possível extrair texto do PDF.", 400

    category = classify_email(email_text)
    response = generate_response(email_text, category)

    return render_template(
        "index.html",
        category=category,
        reply=response
    )

if __name__ == "__main__":
    app.run(debug=True)
