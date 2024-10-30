# models.py

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) - {status}"


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def __str__(self):
        return f"Usuário: {self.nome}, Livros emprestados: {[livro.titulo for livro in self.livros_emprestados]}"
