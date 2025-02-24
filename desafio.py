### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ").title()

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
        exit()
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
        exit()
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)
    exit()


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a usuario para um número de ponto flutuante

while True:
    try:
        salario = float(input("Digite seu salário: "))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido.")

#print(f"Salário registrado: R$ {salario:.2f}")


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a usuario para um número de ponto flutuante

while True:
    try:
        bonus = float(input("Digite seu Bonus: "))
        break
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido.")
#print(f"Bonus registrado:  {bonus:.2f}")

# 4) Calcule o valor do bônus final
bonus_final = salario * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Parabéns {nome} voce teve um bonus de {bonus:.2f} e ira receber ao final R$ {bonus_final:.2f}')
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?