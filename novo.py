# python BIBLIOTECA.py
# ️⃣
import os

livro = []
autor = []
ano = []
aluguel = []

def salvar_livros_txt():
    with open("livros.txt", "w", encoding="utf-8") as arquivo:
        for i in range(len(livro)):
            linha = f"{livro[i]} - {autor[i]} - {ano[i]} {aluguel[i]}\n"
            arquivo.write(linha)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def nome_livro():
    while True:
        try:
            nome = input("Digite o nome do livro: ")
            if nome.replace(" ", "").isalpha():
                print(f"Livro '{nome}' adicionado com sucesso.")
                return nome
            else:
                print("Digite apenas letras e espaços. Não são permitidos números ou caracteres especiais.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


def nome_escritor():
    while True:
        try:
            nome_autor = str(input("Digite o nome do autor: "))
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
            if 1800 <= ano_livro <= 9999:
                return ano_livro
            else:
                print("Digite um ano válido (formato AAAA).")
        except ValueError:
            print("Digite um número válido para o ano.")


def adicionar_livro():
    nome = nome_livro()
    escritor = nome_escritor()
    ano_publicacao = ano_lancamento()
    status = "(DISPONÍVEL) "

    livro.append(nome)
    autor.append(escritor)
    ano.append(ano_publicacao)
    aluguel.append(status)

    salvar_livros_txt()

    limpar_tela()
    print(f"\nLivro adicionado com sucesso:\n{nome} - {escritor} - {ano_publicacao} {status}")


def listar_livro():
    if not livro:
        print("Nenhum livro cadastrado. ")
    else:
        limpar_tela()
        for i in range(len(livro)):
            print(f"{i + 1}º. livro: {livro[i]} - autor: {autor[i]} - ano: {ano[i]} {aluguel[i]}")


def alterar_livro():
    if not livro:
        print("Nenhum livro cadastrado para alterar.")
    else:
        try:
            listar_livro()
            alterar = int(input("Qual posição está o livro que você quer alterar: ")) - 1
            if 0 <= alterar < len(livro):
                print(f"Livro atual: {livro[alterar]} - Autor atual: {autor[alterar]} - Ano atual: {ano[alterar]}")
                
                novo_nome = nome_livro()
                novo_autor = nome_escritor()
                novo_ano = ano_lancamento()

                livro[alterar] = novo_nome
                autor[alterar] = novo_autor
                ano[alterar] = novo_ano
                aluguel[alterar] = "(DISPONÍVEL)"

                salvar_livros_txt()

                print("Livro alterado com sucesso.")
                print(f"Novo livro: {livro[alterar]} - Novo autor: {autor[alterar]} - Novo ano: {ano[alterar]} {aluguel[alterar]}")
            else:
                print("Posição inválida. ")
        except ValueError:
            print("Digite um número válido para a posição. ")


def alugar():
    if not livro:
        print("Nenhum livro cadastrado.")
    else:
        try:
            listar_livro()
            op = int(input("Digite o a posição do livro que você deseja alugar: ")) - 1
            if aluguel[op] == "(INDISPONÍVEL) ":
                print(f"Livro {livro[op]} está indisponível.")
            elif 0 <= op < len(livro):
                aluguel[op] = "(INDISPONÍVEL)"
                salvar_livros_txt()
                print(f"Aluguel do livro {livro[op]} concluído com sucesso, status: {aluguel[op]}")
            else:
                print("Posição inválida.")
        except ValueError:
            print("Digite um número válido para a posição. ")


def devolver():
    if not livro:
        print("Nenhum livro cadastrado.")
    elif not any(aluguel):
        print("Nenhum livro está alugado.")
    else:
        try:
            listar_livro()
            posicao = int(input("Digite a posição do livro que deseja devolver: ")) - 1
            if 0 <= posicao < len(livro) and aluguel[posicao] == "(INDISPONÍVEL)":
                aluguel[posicao] = "(DISPONÍVEL)"
                salvar_livros_txt()
                print(f"Livro '{livro[posicao]}' devolvido com sucesso!")
            else:
                print("Posição inválida ou o livro não está alugado.")
        except ValueError:
            print("Digite um número válido para a posição.")


def deletar_livro():
    if not livro:
        print("Nenhum livro cadastrado para deletar.")
    else:
        try:
            listar_livro()
            posicao = int(input("Digite a posição do livro que deseja deletar: ")) - 1
            if 0 <= posicao < len(livro):
                print(f"Livro {livro[posicao]} deletado com sucesso.")
                del livro[posicao]
                del autor[posicao]
                del ano[posicao]
                del aluguel[posicao]
                salvar_livros_txt()
            
            else:
                print("Posição inválida.")
        except ValueError:
            print("Digite um número válido para a posição.")


def exibir_menu():
    print("\nMENU DA BIBLIOTECA\n")
    print("1. Adicionar livros")
    print("2. Listar livros")
    print("3. Alterar livros")
    print("4. Deletar livros")
    print("5. Alugar livro")
    print("6. Devolver livro")
    print("7. Sair")


def main():
    try:
        exibir_menu()
        opcao = int(input("Digite a opção: "))
        limpar_tela()

        match opcao:
            case 1:
                adicionar_livro()
            case 2:
                listar_livro()
            case 3:
                alterar_livro()
            case 4:
                deletar_livro()
            case 5:
                alugar()
            case 6:
                devolver()
            case 7:
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
