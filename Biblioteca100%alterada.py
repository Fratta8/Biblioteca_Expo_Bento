# ️⃣

import os

RESET   = "\033[0m"
VERDE   = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL    = "\033[94m"
NEGRITO = "\033[1m"



livro = []
autor = []
ano = []
aluguel = []



def salvar_livros_txt():
    with open("livros.txt", "w", encoding="utf-8") as arquivo:
        for i in range(len(livro)):
            linha = f"{livro[i]} - {autor[i]} - {ano[i]} {aluguel[i]}\n"
            arquivo.write(linha)



def carregar_livros_txt():
    if not os.path.exists("livros.txt"):
        return
    with open("livros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().rsplit(" - ", 2)
            if len(partes) == 3:
                nome_livro, nome_autor, restante = partes
                try:
                    ano_info, status = restante.rsplit(" ", 1)
                    livro.append(nome_livro)
                    autor.append(nome_autor)
                    ano.append(int(ano_info))
                    aluguel.append(status)
                except ValueError:
                    continue



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



def nome_livro():
    while True:
        try:
            nome = input("Digite o nome do livro: ")
            if nome.replace(" ", "").isalpha():
                print(f"{VERDE}✅ Livro '{nome}' adicionado com sucesso.{RESET}")
                return nome
            else:
                print(f"{VERMELHO}❌ Use apenas letras e espaços.{RESET}")
        except Exception as e:
            print(f"{VERMELHO}❌ Erro: {e}{RESET}")



def nome_escritor():
    while True:
        try:
            nome_autor = input("Digite o nome do autor: ")
            if nome_autor.replace(" ", "").isalpha():
                print(f"{VERDE}✅ Autor '{nome_autor}' adicionado com sucesso.{RESET}")
                return nome_autor
            else:
                print(f"{VERMELHO}❌ Use apenas letras e espaços.{RESET}")
        except Exception as e:
            print(f"{VERMELHO}❌ Erro: {e}{RESET}")



def ano_lancamento():
    while True:
        try:
            ano_livro = int(input("Digite o ano de lançamento: "))
            if 1800 <= ano_livro <= 9999:
                return ano_livro
            else:
                print(f"{VERMELHO}❌ Ano inválido.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Digite um número válido.{RESET}")



def adicionar_livro():
    nome = nome_livro()
    escritor = nome_escritor()
    ano_publicacao = ano_lancamento()
    status = "(DISPONÍVEL)"

    livro.append(nome)
    autor.append(escritor)
    ano.append(ano_publicacao)
    aluguel.append(status)

    salvar_livros_txt()
    limpar_tela()
    print(f"{VERDE}{NEGRITO}✅ Livro adicionado:{RESET}")
    print(f"{AZUL}📘 {nome} - ✍️  {escritor} - 📅 {ano_publicacao} {status}{RESET}")

    

def listar_livro():
    if not livro:
        print(f"{AMARELO}⚠️ Nenhum livro cadastrado.{RESET}")
    else:
        limpar_tela()
        print(f"{AZUL}{NEGRITO}📚 LIVROS:{RESET}")
        for i in range(len(livro)):
            print(f"{AZUL}{i + 1}️⃣  {livro[i]} - Autor: {autor[i]} - Ano: {ano[i]} - {aluguel[i]}{RESET}")



def alterar_livro():
    if not livro:
        print(f"{AMARELO}⚠️ Nenhum livro para alterar.{RESET}")
    else:
        try:
            listar_livro()
            alterar = int(input("Número do livro para alterar: ")) - 1
            if 0 <= alterar < len(livro):
                print(f"{AZUL}📘 Atual: {livro[alterar]} - ✍️  {autor[alterar]} - 📅 {ano[alterar]}{RESET}")
                novo_nome = nome_livro()
                novo_autor = nome_escritor()
                novo_ano = ano_lancamento()

                livro[alterar] = novo_nome
                autor[alterar] = novo_autor
                ano[alterar] = novo_ano
                aluguel[alterar] = "(DISPONÍVEL)"

                salvar_livros_txt()
                print(f"{VERDE}✅ Livro alterado!{RESET}")
            else:
                print(f"{VERMELHO}❌ Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Número inválido.{RESET}")



def alugar():
    if not livro:
        print(f"{AMARELO}⚠️ Nenhum livro cadastrado.{RESET}")
    else:
        try:
            listar_livro()
            op = int(input("Número do livro para alugar: ")) - 1
            if 0 <= op < len(livro):
                if aluguel[op] == "(INDISPONÍVEL)":
                    print(f"{AMARELO}⚠️ Já está alugado.{RESET}")
                else:
                    aluguel[op] = "(INDISPONÍVEL)"
                    salvar_livros_txt()
                    print(f"{VERDE}📦  Aluguel de '{livro[op]}' feito com sucesso.{RESET}")
            else:
                print(f"{VERMELHO}❌ Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Número inválido.{RESET}")



def devolver():
    if not livro:
        print(f"{AMARELO}⚠️ Nenhum livro cadastrado.{RESET}")
    else:
        try:
            listar_livro()
            posicao = int(input("Número do livro para devolver: ")) - 1
            if 0 <= posicao < len(livro):
                if aluguel[posicao] == "(INDISPONÍVEL)":
                    aluguel[posicao] = "(DISPONÍVEL)"
                    salvar_livros_txt()
                    print(f"{VERDE}✅  Livro '{livro[posicao]}' devolvido.{RESET}")
                else:
                    print(f"{AMARELO}⚠️   Livro já disponível.{RESET}")
            else:
                print(f"{VERMELHO}❌ Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Número inválido.{RESET}")



def deletar_livro():
    if not livro:
        print(f"{AMARELO}⚠️ Nenhum livro cadastrado.{RESET}")
    else:
        try:
            listar_livro()
            posicao = int(input("Número do livro para deletar: ")) - 1
            if 0 <= posicao < len(livro):
                print(f"{VERDE}🗑️  Livro '{livro[posicao]}' deletado.{RESET}")
                del livro[posicao]
                del autor[posicao]
                del ano[posicao]
                del aluguel[posicao]
                salvar_livros_txt()
            else:
                print(f"{VERMELHO}❌ Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Número inválido.{RESET}")



def exibir_menu():
    print(f"{AZUL}{NEGRITO}╔════════════════════════════╗")
    print("║     📚 MENU DA BIBLIOTECA  ║")
    print("╚════════════════════════════╝")
    print("1️⃣  Adicionar livros")
    print("2️⃣  Listar livros")
    print("3️⃣  Alterar livros")
    print("4️⃣  Deletar livros")
    print("5️⃣  Alugar livro")
    print("6️⃣  Devolver livro")
    print("7️⃣  Sair")
    print(f"══════════════════════════════{RESET}")



def main():
    try:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
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
                print(f"{AMARELO}{NEGRITO}👋  Encerrando o sistema...{RESET}")
                return False
            case _:
                print(f"{VERMELHO}❌ Opção inválida.{RESET}")
    except ValueError:
        limpar_tela()
        print(f"{VERMELHO}❌ Digite uma opção válida.{RESET}")
    
    return True



if __name__ == "__main__":
    carregar_livros_txt()
    while True:
        if not main():
            break
