import os

livro = []
autor = []
ano = []
aluguel = []
disp = "(DISPONÍVEL)"
indisp = "(INDISPONÍVEL)"


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def salvar_em_arquivo():
    with open("biblioteca.txt", "w", encoding="utf-8") as arquivo:
        for i in range(len(livro)):
            arquivo.write(f"{livro[i]} | {autor[i]} | {ano[i]} | {aluguel[i]}\n")


def nome_livro():
    while True:
        try:
            limpar_tela()
            nome = input("Digite o nome do livro: ")
            if nome.replace(" ", "").replace(",", "").isalpha():
                print(f"Livro '{nome}' adicionado com sucesso.")
                return nome
            else:
                print("Digite apenas letras e espaços. Não são permitidos números ou caracteres especiais.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


def nome_escritor():
    while True:
        try:
            nome_autor = input("Digite o nome do autor: ")
            if nome_autor.replace(" ", "").isalpha():
                print(f"Nome do autor '{nome_autor}' adicionado com sucesso.")
                return nome_autor
            else:
                print("Digite apenas letras e espaços. Não são permitidos números ou caracteres especiais.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


def ano_lancamento():
    while True:
        try:
            ano_livro = int(input("Digite o ano de lançamento: "))
            if 1400 <= ano_livro <= 2025:
                return ano_livro
            else:
                print("Digite um ano válido (entre 1400 e 2025).")
        except ValueError:
            print("Digite um número válido para o ano.")


def adicionar_livro():
    nome = nome_livro()
    escritor = nome_escritor()
    ano_publicacao = ano_lancamento()
    status = disp

    livro.append(nome)
    autor.append(escritor)
    ano.append(ano_publicacao)
    aluguel.append(status)

    limpar_tela()
    print(f"\nLivro adicionado com sucesso:\n{nome} - {escritor} - {ano_publicacao} {status}")
    salvar_em_arquivo()


def listar_livro(livro, autor, ano, aluguel):
    if not livro:
        print("Nenhum livro cadastrado. ")
    else:
        limpar_tela()
        for i in range(len(livro)):
            print(f"{i + 1}º. livro: {livro[i]} - autor: {autor[i]} - ano: {ano[i]} {aluguel[i]}")


def alterar_livro(livro, autor, ano, aluguel, listar_livro):
    if not livro:
        print("Nenhum livro cadastrado para alterar.")
    else:
        try:
            listar_livro(livro, autor, ano, aluguel)
            alterar = int(input("Qual posição está o livro que você quer alterar: "))
            if 0 < alterar <= len(livro):
                print(f"Livro atual: {livro[alterar - 1]} - Autor atual: {autor[alterar - 1]} - Ano atual: {ano[alterar - 1]}")

                novo_nome = nome_livro()
                novo_autor = nome_escritor()
                novo_ano = ano_lancamento()

                livro[alterar - 1] = novo_nome
                autor[alterar - 1] = novo_autor
                ano[alterar - 1] = novo_ano
                aluguel[alterar - 1] = disp

                print("Livro alterado com sucesso.")
                salvar_em_arquivo()
            else:
                print("Posição inválida. ")
        except ValueError:
            print("Digite um número válido para a posição. ")


def alugar(livro, aluguel, listar_livro):
    if not livro:
        print("Nenhum livro cadastrado.")
    else:
        try:
            listar_livro(livro, autor, ano, aluguel)
            op = int(input("Digite a posição do livro que você deseja alugar: "))
            if 0 < op <= len(livro):
                if aluguel[op - 1] == (indisp):
                    print("Esse livro já está alugado.")
                else:
                    aluguel[op - 1] = (indisp)
                    print("Aluguel concluído com sucesso!")
                    salvar_em_arquivo()
            else:
                print("Posição inválida.")
        except ValueError:
            print("Digite um número válido para a posição. ")


def devolver(livro, aluguel, listar_livro):
    if not livro:
        print("Nenhum livro cadastrado.")
    else:
        try:
            listar_livro(livro, autor, ano, aluguel)
            posicao = int(input("Digite a posição do livro que deseja devolver: "))
            if 0 < posicao <= len(livro) and aluguel[posicao - 1] == "(INDISPONÍVEL)":
                aluguel[posicao - 1] = disp
                print(f"Livro '{livro[posicao - 1]}' devolvido com sucesso!")
                salvar_em_arquivo()
            else:
                print("Posição inválida ou o livro não está alugado.")
        except ValueError:
            print("Digite um número válido para a posição.")


def deletar_livro(livro, autor, ano, listar_livro):
    if not livro:
        print("Nenhum livro cadastrado para deletar.")
    else:
        try:
            listar_livro(livro, autor, ano, aluguel)
            posicao = int(input("Digite a posição do livro que deseja deletar: "))
            if 0 < posicao <= len(livro):
                print(f"{posicao}º. livro: {livro[posicao - 1]} - autor: {autor[posicao - 1]} - ano: {ano[posicao - 1]}")
                del livro[posicao - 1]
                del autor[posicao - 1]
                del ano[posicao - 1]
                del aluguel[posicao - 1]
                print("Livro deletado com sucesso.")
                salvar_em_arquivo()
            else:
                print("Posição inválida.")
        except ValueError:
            print("Digite um número válido para a posição.")


def popular_livros_exemplo():
    livros_exemplo = [
        ("Dom Quixote", "Miguel de Cervantes", 1605),
        ("1984", "George Orwell", 1949),
        ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943),
        ("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
        ("A Revolução dos Bichos", "George Orwell", 1945),
        ("Orgulho e Preconceito", "Jane Austen", 1813),
        ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
        ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997),
        ("O Hobbit", "J.R.R. Tolkien", 1937),
        ("A Metamorfose", "Franz Kafka", 1915)
    ]

    for nome, escritor, ano_livro in livros_exemplo:
        livro.append(nome)
        autor.append(escritor)
        ano.append(ano_livro)
        aluguel.append(disp)

    salvar_em_arquivo()
    print("Livros de exemplo adicionados com sucesso!")


def exibir_menu():
    print("\nMENU DA BIBLIOTECA\n")
    print("1. Adicionar livros")
    print("2. Listar livros")
    print("3. Alterar livros")
    print("4. Deletar livros")
    print("5. Alugar livro")
    print("6. Devolver livro")
    print("7. Popular livros de exemplo")
    print("8. Sair")


def main():
    try:
        exibir_menu()
        opcao = int(input("Digite a opção: "))
        limpar_tela()

        match opcao:
            case 1:
                adicionar_livro()
            case 2:
                listar_livro(livro, autor, ano, aluguel)
            case 3:
                alterar_livro(livro, autor, ano, aluguel, listar_livro)
            case 4:
                deletar_livro(livro, autor, ano, listar_livro)
            case 5:
                alugar(livro, aluguel, listar_livro)
            case 6:
                devolver(livro, aluguel, listar_livro)
            case 7:
                popular_livros_exemplo()
            case 8:
                print("SAINDO...")
                return False
            case _:
                print("Opção inválida.")
    except ValueError:
        limpar_tela()
        print("Por favor, digite uma opção válida (um número inteiro).")

    return True


if __name__ == "__main__":
    while True:
        if not main():
            break
