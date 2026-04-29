contatos = []

print('Bem-vindo ao seu gerenciador de contatos!')

while True:
    print('\n--- MENU AGENDA ---')
    print('1 - Adicionar contato')
    print('2 - Editar contato existente')
    print('3 - Listar contatos')
    print('4 - Marcar/Desmarcar favorito')
    print('5 - Listar contatos favoritos')
    print('6 - Deletar contato')
    print('7 - Sair')

    escolha = input('Digite a opção desejada: ')

    if escolha == '1':
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        contatos.append({'nome': nome, 'telefone': telefone, 'email': email, 'favorito': False})
        print(f'✓ Contato {nome} adicionado!')

    elif escolha == '3' or escolha == '2' or escolha == '4' or escolha == '6':
        if not contatos:
            print('! Sua agenda está vazia.')
        else:
            print('\n--- LISTA DE CONTATOS ---')
            for i, contato in enumerate(contatos, start=1):
                fav = "★" if contato['favorito'] else " "
                print(f"{i}. [{fav}] {contato['nome']} - {contato['telefone']}")
            
            if escolha in ['2', '4', '6']:
                try:
                    indice = int(input('\nDigite o número do contato para realizar a ação: ')) - 1
                    if 0 <= indice < len(contatos):
                        if escolha == '2':
                            contatos[indice]['nome'] = input('Novo nome (Enter para manter): ') or contatos[indice]['nome']
                            contatos[indice]['telefone'] = input('Novo tel (Enter para manter): ') or contatos[indice]['telefone']
                            print('✓ Atualizado!')
                        elif escolha == '4':
                            contatos[indice]['favorito'] = not contatos[indice]['favorito']
                            status = "favoritado" if contatos[indice]['favorito'] else "removido dos favoritos"
                            print(f'✓ Contato {status}!')
                        elif escolha == '6':
                            removido = contatos.pop(indice)
                            print(f'✓ Contato {removido["nome"]} deletado!')
                    else:
                        print('! Número inválido.')
                except ValueError:
                    print('! Por favor, digite apenas números.')

    elif escolha == '5':
        favoritos = [c for c in contatos if c['favorito']]
        if favoritos:
            print('\n--- MEUS FAVORITOS ★ ---')
            for c in favoritos:
                print(f"• {c['nome']} ({c['telefone']})")
        else:
            print('! Nenhum favorito marcado.')

    elif escolha == '7':
        print('Encerrando agenda... Até logo!')
        break
    else:
        print('! Opção inválida.')