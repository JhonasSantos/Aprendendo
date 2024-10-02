import Commom

print("Estoque Queiroz")
# print("\n1. Adicionar produto\n2. Atualizar dados de um produto\n3. Buscar dados de um produto\n4. Relatórios\n5. Sair")

while True:
    print("\n1. Adicionar produto\n2. Atualizar dados de um produto\n3. Buscar dados de um produto\n4. Relatórios\n5. Sair")
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        Commom.cadastro()
        
    elif opcao == 2:
        Commom.atualizar()
        
    elif opcao == 3:
        Commom.buscar()
        
    elif opcao == 4:
        Commom.menu_relatorios()
        
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida")