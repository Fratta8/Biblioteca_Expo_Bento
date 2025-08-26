# python BIBLIOTECA.py
import os

livro = []
autor = []
ano = []
aluguel = []


def limpar_tela():
    os.system('cls')

def nome_livro():
    while True:
        try:
            limpar_tela()
            nome = input("Digite o nome do livro: ")# tem que consertar str, is alphanum e etc
            if nome.replace(" ", "").isalpha() or nome.replace(",","").isalpha():
                #livro.append()
                print(f"Livro '{nome}' adicionado com sucesso.")
                return nome
                #break
            else:
                print("Digite apenas letras e espaços. Não são permitidos números ou caracteres especiais.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    
def nome_escritor():
    while True:
            try:
                nome_autor = str(input("Digite o nome do autor: "))
                if nome_autor.replace(" ", "").isalpha():
                    #autor.append(nome_autor)
                    print(f"Nome do autor '{nome_autor}' adicionado com sucesso.")
                    return nome_autor
                    #break
                else:
                    print("Digite apenas letras e espaços. Não são permitidos números ou caracteres especiais.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")


def ano_lancamento():
    while True:
        try:
            ano_livro = int(input("Digite o ano de lançamento: "))
            if 1000 <= ano_livro <= 9999:
                #ano.append(ano_livro)
                return ano_livro
                #break
            else:
                print("Digite um ano válido (formato AAAA).")
        except ValueError:
            print("Digite um número válido para o ano.")
    
    
    

def adicionar_livro():
    nome = input("Nome do livro: ")
    escritor = input("Nome do autor: ")
    ano_publicacao = input("Ano de lançamento: ")
    status = "(DISPONÍVEL)"

    print(f"{nome} - {escritor} ({ano_publicacao}) {status}")


    livro.append(nome)
    autor.append(escritor)
    ano.append(ano_publicacao)
    aluguel.append(("(DISPONÍVEL)"))

    limpar_tela()
    print(f"\nLivro adicionado com sucesso:\n{nome} - {escritor} - {ano_publicacao} {status}")


def listar_livro(livro, autor, ano, aluguel): #poderia ser passado livro, autor ou ano

    if not livro:
        print("Nenhum livro cadastrado .")
            
    else:
        limpar_tela()
        for i in range(len(livro)):
            print(f"{i + 1}º. livro: {livro[i]} - autor: {autor[i]} - ano:  {ano[i]} {aluguel[i]}") #print(f"{livros[i]}, {autores[i]}, {anos[i]}")

def alterar_livro(livro, autor, ano, aluguel, listar_livro):
        if not livro:
            print("Nenhum livro cadastrado para alterar.")
        else:
            try:
                listar_livro(livro, autor, ano, aluguel)
                alterar = int(input("Qual posição está o livro que você quer alterar: "))
                if 0 < alterar <= len(livro):
                    print(f"Livro atual: {livro[alterar - 1]} - Autor atual: {autor[alterar - 1]} - Ano atual: {ano[alterar - 1]} ")
                    
                    novo_nome = nome_livro()
                    novo_autor = nome_escritor()
                    novo_ano = ano_lancamento()

                    livro[alterar - 1] = novo_nome
                    autor[alterar - 1] = novo_autor
                    ano[alterar - 1] = novo_ano
                    aluguel[alterar -1] = "(DISPONÍVEL)"

                    print("Livro alterado com sucesso.")
                    print(f"novo livro: {livro[alterar - 1]} - novo autor: {autor[alterar - 1]} - novo ano: {ano[alterar - 1]} {aluguel[alterar - 1]}")
                else:
                    print("Posição inválida .")

            except ValueError:
                print("Digite um número válido para a posição .")


def alugar(livro, aluguel, listar_livro):
    if not livro:
        print("Nenhum livro cadastrado.")
            
    else:
        try:
            listar_livro(livro, autor, ano, aluguel)
            op = int(input("Digite a posição do livro que você deseja alugar: "))
            if 0 < op <= len(livro):

                aluguel[op - 1] = "(INDISPONÍVEL)"  
                #aluguel.append[op - 1]
                print("Aluguel concluído com sucesso!! ")
            else:
                print("Posição inválida.")
        except ValueError:
            print("Digite um número válido para a posição .")


def devolver(livro, aluguel, listar_livro):
    if not livro:
        print("Nenhum livro cadastrado.")
    elif not any(aluguel):
        print("Nenhum livro está alugado.")
    else:
        try:
            listar_livro(livro, autor, ano, aluguel)
            posicao = int(input("Digite a posição do livro que deseja devolver: "))
            if 0 < posicao <= len(livro) and aluguel[posicao - 1] == "(INDISPONÍVEL)":
                aluguel[posicao - 1] = "(DISPONÍVEL)"
                print(f"Livro '{livro[posicao - 1]}' devolvido com sucesso!")
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
                    print(f"{posicao }º. livro: {livro[posicao - 1]} - autor: {autor[posicao - 1]} - ano: {ano[posicao - 1]}") 
                    del livro[posicao - 1]
                    del autor[posicao - 1]
                    del ano[posicao - 1]
                    int(input("Digite a posição do livro que você deseja alugar: "))

                        
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
                adicionar_livro(livro, autor, ano, aluguel)
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
           
