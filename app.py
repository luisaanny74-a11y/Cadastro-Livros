from datetime import date

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "categoria": "Romance"},
    {"id": 2, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "categoria": "Fantasia"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "ano": 1949, "categoria": "Ficção Científica"},
    {"id": 4, "titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988, "categoria": "Ficção"},
    {"id": 5, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "ano": 1813, "categoria": "Romance"},
    {"id": 6, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ano": 1953, "categoria": "Distopia"},
]


@app.route("/")
def index():
    return render_template("index.html", total_livros=len(livros))


@app.route("/cadastro")
def formulario_cadastro():
    return render_template("cadastro.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar_livro():
    titulo = request.form.get("titulo", "").strip()
    autor = request.form.get("autor", "").strip()
    categoria = request.form.get("categoria", "").strip() or "Não informada"
    ano_texto = request.form.get("ano", "").strip()
    ano_atual = date.today().year

    if not titulo or not autor:
        return render_template("cadastro.html", erro="Informe o título e o autor para cadastrar o livro.", dados=request.form), 400

    try:
        ano = int(ano_texto) if ano_texto else "Não informado"
        if isinstance(ano, int) and not 1 <= ano <= ano_atual:
            raise ValueError
    except ValueError:
        return render_template("cadastro.html", erro=f"Informe um ano entre 1 e {ano_atual}.", dados=request.form), 400

    proximo_id = max((livro["id"] for livro in livros), default=0) + 1
    livros.append({"id": proximo_id, "titulo": titulo, "autor": autor, "ano": ano, "categoria": categoria})
    return redirect(url_for("listar_livros", cadastrado="1"))


@app.route("/livros")
def listar_livros():
    return render_template("lista.html", livros=livros, cadastrado=request.args.get("cadastrado") == "1")


@app.route("/livros/<int:livro_id>/excluir", methods=["POST"])
def excluir_livro(livro_id):
    livro = next((item for item in livros if item["id"] == livro_id), None)
    if livro:
        livros.remove(livro)
        return redirect(url_for("listar_livros", excluido="1"))
    return redirect(url_for("listar_livros", erro="registro-nao-encontrado"))


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)
