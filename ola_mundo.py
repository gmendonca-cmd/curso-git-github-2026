print("Olá Mundo!")


def mostrar_tabuada(numero: int):
    """Exibe a tabuada de 1 a 10 para o número informado."""
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    try:
        # Solicita o número ao usuário
        entrada = input("Digite um número inteiro para ver a tabuada: ").strip()
        
        # Validação de entrada
        if not entrada.lstrip('-').isdigit():
            raise ValueError("Entrada inválida. Digite apenas números inteiros.")
        
        numero = int(entrada)
        mostrar_tabuada(numero)

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()