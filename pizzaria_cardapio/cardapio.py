# Sistema de Cardápio de Pizzaria


cardapio = {
    'Margherita': 30.0,
    'Calabresa': 32.0,
    'Quatro Queijos': 35.0,
    'Frango com Catupiry': 36.0,
    'Portuguesa': 34.0
}

pedido = []

def mostrar_cardapio():
    print("\n--- Cardápio de Pizzas ---")
    for i, (pizza, preco) in enumerate(cardapio.items(), 1):
        print(f"{i}. {pizza} - R$ {preco:.2f}")

def adicionar_pizza():
    mostrar_cardapio()
    escolha = input("Digite o número da pizza que deseja adicionar ao pedido:  ")
    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(cardapio):
            pizza = list(cardapio.keys())[escolha - 1]
            pedido.append(pizza)
            print(f"{pizza} adicionada ao pedido!")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, digite um número válido.")

def ver_pedido():
    print("\n--- Seu Pedido ---")
    if not pedido:
        print("Nenhuma pizza adicionada ainda.")
    else:
        total = 0
        for pizza in pedido:
            preco = cardapio[pizza]
            print(f"{pizza} - R$ {preco:.2f}")
            total += preco
        print(f"Total: R$ {total:.2f}")

def finalizar_pedido():
    ver_pedido()
    print("\nEscolha a forma de pagamento:")
    print("1. Dinheiro")
    print("2. Cartão")
    print("3. Pix")
    forma = input("Digite o número da forma de pagamento: ")
    if forma == '1':
        pagamento = "Dinheiro"
    elif forma == '2':
        pagamento = "Cartão"
    elif forma == '3':
        pagamento = "Pix"
    else:
        pagamento = "Não informada"
    print(f"\nForma de pagamento escolhida: {pagamento}")
    print("\nPedido finalizado! Obrigado pela preferência.")
    exit()

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Ver cardápio")
        print("2. Adicionar pizza ao pedido")
        print("3. Ver pedido")
        print("4. Finalizar pedido")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            mostrar_cardapio()
        elif opcao == '2':
            adicionar_pizza()
        elif opcao == '3':
            ver_pedido()
        elif opcao == '4':
            finalizar_pedido()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print("""
====================================
 Bem-vindo à Pizzaria Sabor da Massa!
 O melhor cardápio de pizzas da cidade.
====================================
""")
    menu() 