contatos = []

def mostrar_menu():
    print("MENU")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contatos")
    print("4. Deletar contato")
    print("5. Sair")
    print("--------------------")

while True:
    mostrar_menu()
    
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == '1':
        print("\nVocê escolheu (Adicionar contato).")

        while True:
            novo_nome = input("Adicione o nome do contato: ")
            if novo_nome:
                break
            else:
                print("ERRO: O nome não pode ser vazio. Tente novamente.")
        
        while True:
            novo_numero = input("Adicione o número: ")
            if novo_numero:
                break
            else:
                print("ERRO: O número não pode ser vazio. Tente novamente.")

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
        input("Pressione Enter para continuar.")

    elif escolha == '3':
        print("\nEDITAR CONTATO")

        if not contatos:
            print("Nenhum contato para editar.")
            input("\nPressione Enter para continuar.")
            continue

        for i, contato in enumerate(contatos):
            print(f"ID: {i} | Nome: {contato['nome']}")
        print("--------------------")

        try:
            id_para_editar = int(input("Digite o ID do contato que deseja editar: "))

            if 0 <= id_para_editar < len(contatos):
                contato_a_editar = contatos[id_para_editar]
                print(f"\nEditando o contato: {contato_a_editar['nome']}")

                novo_nome = input(f"Novo nome (ou Enter para manter '{contato_a_editar['nome']}'): ")
                novo_numero = input(f"Novo número (ou Enter para manter '{contato_a_editar['numero']}'): ")
                novo_email = input(f"Novo email (ou Enter para manter '{contato_a_editar['email']}'): ")

                if novo_nome:
                    contato_a_editar['nome'] = novo_nome
                if novo_numero:
                    contato_a_editar['numero'] = novo_numero
                if novo_email:
                    contato_a_editar['email'] = novo_email
                
                print("\nContato atualizado com sucesso!")
            else:
                print("ID inválido! Por favor, escolha um ID da lista.")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas o número do ID.")
        
        input("\nPressione Enter para continuar.")
        
    elif escolha == '4':
        print("\nDELETAR CONTATO")

        if not contatos:
            print("Nenhum contato para deletar.")
            input("\nPressione Enter para continuar.")
            continue

        for i, contato in enumerate(contatos):
            print(f"ID: {i} | Nome: {contato['nome']}")
        print("--------------------")

        try:
            id_para_deletar = int(input("Digite o ID do contato que deseja deletar: "))

            if 0 <= id_para_deletar < len(contatos):

                contato_removido = contatos[id_para_deletar]
                confirmacao = input(f"Tem certeza que deseja remover o contato '{contato_removido['nome']}'? (s/n): ")
                
                if confirmacao.lower() == 's':

                    contatos.pop(id_para_deletar)
                    print("Contato removido com sucesso!")
                else:
                    print("Operação cancelada.")
            else:
                print("ID inválido! Por favor, escolha um ID da lista.")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas o número do ID.")

        input("\nPressione Enter para continuar.")
        
    elif escolha == '5':
        print("\nSaindo do programa. Até logo!")
        break
        
    else:
        print("\nOpção inválida! Por favor, escolha uma opção do menu.")
        input("Pressione Enter para tentar novamente.")
