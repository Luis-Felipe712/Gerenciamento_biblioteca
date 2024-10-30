# views.py

from controllers import BibliotecaController

class BibliotecaView:
    def __init__(self):
        self.controller = BibliotecaController()

    def exibir_menu(self):
        print("\nMenu:")
        print("1 - Cadastrar Livro")
        print("2 - Consultar Livros")
        print("3 - Cadastrar Usuário")
        print("4 - Empréstimo de Livro")
        print("5 - Devolução de Livro")
        print("0 - Sair")

    def cadastrar_livro(self):
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        isbn = input("ISBN do livro: ")
        print(self.controller.cadastrar_livro(titulo, autor, isbn))

    def consultar_livros(self):
        termo = input("Digite o título ou autor: ")
        livros = self.controller.consultar_livros(termo)
        if livros:
            for livro in livros:
                print(livro)
        else:
            print("Nenhum livro encontrado com esse termo.")

    def cadastrar_usuario(self):
        nome = input("Nome do usuário: ")
        print(self.controller.cadastrar_usuario(nome))

    def emprestar_livro(self):
        isbn = input("ISBN do livro: ")
        usuario_nome = input("Nome do usuário: ")
        print(self.controller.emprestar_livro(isbn, usuario_nome))

    def devolver_livro(self):
        isbn = input("ISBN do livro: ")
        usuario_nome = input("Nome do usuário: ")
        print(self.controller.devolver_livro(isbn, usuario_nome))

    def iniciar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_livro()
            elif opcao == "2":
                self.consultar_livros()
            elif opcao == "3":
                self.cadastrar_usuario()
            elif opcao == "4":
                self.emprestar_livro()
            elif opcao == "5":
                self.devolver_livro()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    view = BibliotecaView()
    view.iniciar()
