# Classe que representa um produto no estoque
class Produto:
    def __init__(self, nome, categoria, quantidade, preco, setor):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.setor = setor

# Função para cadastrar um novo produto
def cadastro():
    nome = input("Nome do produto: ")
    # Verifica se o nome do produto existe
    for produto in estoque:
        if produto.nome.lower() == nome.lower():
            print(f"O produto '{nome}' já está cadastrado no estoque.")
            return
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    setor = input("Setor: ")
    novo_produto = Produto(nome, categoria, quantidade, preco, setor)
    estoque.append(novo_produto)
    print("\nProduto adicionado com sucesso!\n")
    # Adiciona uma entrada na movimentação.
    movimentacao.append(f"Entrada de {quantidade} unidades do produto {nome}. Totalizando {quantidade} unidades.")

# Função para atualizar os dados de um produto
def atualizar():
    nome = input("Nome do produto que deseja atualizar: ")
    for produto in estoque:
        if nome == produto.nome:
            opcao = input("1. Atualizar nome\n2. Atualizar categoria\n3. Atualizar quantidade\n4. Atualizar preco\n5. Atualizar setor\n")
            if opcao == "1":
                novo_nome = input("Novo nome: ")
                produto.nome = novo_nome
                print("Produto atualizado com sucesso!")
            elif opcao == "2":
                nova_categ = input("Nova categoria: ")
                produto.categoria = nova_categ
                print("Produto atualizado com sucesso!")
            elif opcao == "3":
                nova_quant = int(input("Nova quantidade: "))
                # Verifica se a nova quantidade é menor/maior que a existente
                if nova_quant < produto.quantidade:
                    diferenca = produto.quantidade - nova_quant
                    movimentacao.append(f"Saida de {diferenca} unidades do produto {nome}.Totalizando {nova_quant} unidades.")
                elif nova_quant > produto.quantidade:
                    diferenca = nova_quant - produto.quantidade
                    movimentacao.append(f"Entrada de {diferenca} unidades do produto {nome}. Totalizando {nova_quant} unidades.")          
                produto.quantidade = nova_quant
                print("Produto atualizado com sucesso!")
            elif opcao == "4":
                novo_preco = float(input("Novo preço: "))
                produto.preco = novo_preco
                print("Produto atualizado com sucesso!")
            elif opcao == "5":
                novo_setor = input("Novo setor: ")
                produto.setor = novo_setor
                print("Produto atualizado com sucesso!")
            else:
                print("Opção inválida")
                return

# Função para buscar dados de um produto
def buscar():
    nome = input("Nome do produto que deseja buscar: ")
    for produto in estoque:
        if nome == produto.nome:
            print(f"Nome: {produto.nome}")
            print(f"Categoria: {produto.categoria}")
            print(f"Quantidade: {produto.quantidade}")
            print(f"Preço: {produto.preco}")
            print(f"Setor: {produto.setor}")
        return
    print("Produto não encontrado") 

# Função para gerar relatórios
def relatorio_movimentacao():
    print("\nRelatório de Movimentação de Produtos:\n")
    for log in movimentacao:
        print(log)

# Função para gerar de relatorio de estoque baixo
def relatorio_estoque_baixo():
    print("\nRelatório de Estoque Baixo (<= 5 unidades):\n")
    for produto in estoque:
        if produto.quantidade <= 5:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")

# Função para gerar relatórios de estoque excedente
def relatorio_excesso_estoque():
    print("\nRelatório de Excesso de Estoque (>= 100 unidades):\n")
    for produto in estoque:
        if produto.quantidade >= 100:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")

# Função para mostrar o menu de relatórios
def menu_relatorios():
    print("\n1. Relatório de Movimentação\n2. Relatório de Estoque Baixo\n3. Relatório de Excesso de Estoque\n4. Sair\n")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        relatorio_movimentacao()
    elif opcao == 2:
        relatorio_estoque_baixo()
    elif opcao == 3:
        relatorio_excesso_estoque()
    elif opcao == 4:
        print("Saindo...")
    else:
        print("Opção inválida")



estoque = []
movimentacao = []