contatos = []

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
        print("\nVocê escolheu (Adicionar contato).")
        novo_nome = input("Adicione o nome do contato: ")
        novo_numero = input("Adicione o número: ")
        novo_email = input("Adicione o email: ")

        novo_contato = {
            "nome": novo_nome,
            "numero": novo_numero,
            "email": novo_email
        }

        contatos.append(novo_contato)

        print(f"\nContato '{novo_nome}' adicionado com sucesso!")
        input("Pressione Enter para continuar...")
        
      elif escolha == '2':
        print("\nVocê escolheu (Listar contatos).")
        print(f"Contatos: {contatos}")
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
