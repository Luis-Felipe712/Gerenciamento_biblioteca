# controllers.py

from models import Livro, Usuario

class BibliotecaController:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, titulo, autor, isbn):
        novo_livro = Livro(titulo, autor, isbn)
        self.livros.append(novo_livro)
        return "Livro cadastrado com sucesso!"

    def consultar_livros(self, termo):
        return [livro for livro in self.livros if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower()]

    def cadastrar_usuario(self, nome):
        novo_usuario = Usuario(nome)
        self.usuarios.append(novo_usuario)
        return "Usuário cadastrado com sucesso!"

    def emprestar_livro(self, isbn, usuario_nome):
        livro = next((l for l in self.livros if l.isbn == isbn and l.disponivel), None)
        usuario = next((u for u in self.usuarios if u.nome == usuario_nome), None)

        if livro and usuario:
            livro.disponivel = False
            usuario.livros_emprestados.append(livro)
            return "Empréstimo realizado com sucesso!"
        return "Livro indisponível ou usuário não encontrado."

    def devolver_livro(self, isbn, usuario_nome):
        usuario = next((u for u in self.usuarios if u.nome == usuario_nome), None)
        livro = next((l for l in usuario.livros_emprestados if l.isbn == isbn), None) if usuario else None

        if livro and usuario:
            livro.disponivel = True
            usuario.livros_emprestados.remove(livro)
            return "Devolução realizada com sucesso!"
        return "Livro ou usuário não encontrado."
