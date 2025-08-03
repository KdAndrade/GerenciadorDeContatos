nomes = []

def mostrar_menu():
    print("MENU")
    print("1. Adicionar contato")
    print("2. Listar itens")
    print("3. Editar item")
    print("4. Sair")
    print("--------------------")

while True:
    mostrar_menu()
    
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == '1':
        novo_nome = input("Digite o nome do novo contato: ")
        
        nomes.append(novo_nome)
        
        print(f"Contato '{novo_nome}' adicionado com sucesso!")
        input("Pressione Enter para continuar...")

    elif escolha == '2':
        print("\nVocê escolheu (Listar contatos).")
        print(f"Contatos: {nomes}")
        input("Pressione Enter para continuar...")

    elif escolha == '3':
        print("\nVocê escolheu 'Editar item'.")
        input("Pressione Enter para continuar...")
        
    elif escolha == '4':
        print("\nSaindo do programa. Até logo!")
        break
        
    else:
        print("\nOpção inválida! Por favor, escolha uma opção do menu.")
        input("Pressione Enter para tentar novamente...")