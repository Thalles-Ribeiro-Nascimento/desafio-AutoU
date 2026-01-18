from classifier import *
from flask import request, render_template, Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    Rota padrão da aplicação que responde aos métodos HTTP - GET e POST.
    O corpo da requisição é enviado pelo formulário do index.html

    :return: Página Web com a resposta gerada pela IA
    """

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
    """
    Rota para receber um arquivo .pdf ou .txt e que responde ao método HTTP - POST.
    O arquivo é enviado através do formulário do index.html. O mesmo passa por uma verificação
    de tipos e se está vázio. Caso esteja vazio ou não corresponda
    aos tipos permitidos, a aplicação lançará um erro 400 indicando que
    houve um Bad Request. Caso esteja tudo ok, será retornada uma página html com a resposta e categoria do e-mail.

    :return: Página Web com a resposta gerada pela IA
    """
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
        ), 200


    email_text = extrair_pdf(file)
    category = classify_email(email_text)

    if category is None:
        return error(400, "Não foi possível categorizar o email.")
    response = generate_response(email_text, category)

    return render_template(
        "index.html",
        result=category,
        response=response
    ), 200


@app.route('/n8n', methods=['POST'])
def n8n_api() :
    """
    Rota extra para envio da resposta gerada pela IA para o remetente, que responde ao método HTTP - POST.
    Integração feita junto ao N8N para automatizar o envio do e-mail. A rota recebe um Json com o atributo 'text'
    que sera usado para classificação e posteriormente para a resposta da IA.

    :return: Json - Response
    """

    text = request.get_json()
    category = classify_email(text=text['text'])

    if category is None:
        return "Não foi possível categorizar o email."

    response = generate_response(text['text'], category)

    return jsonify({"Response": response}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
