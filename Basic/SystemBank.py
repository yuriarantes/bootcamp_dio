saldo = 1000.00
MAXIMO_SAQUES = 3
VALOR_MAXIMO = 500.00

extrato_dia = {
    "saque": {
        "value":0.0,
        "qtd": 0
    },
    "deposito":{
        "value":0.0,
        "qtd": 0
    }
}

menu = """================= MENU =================
1 - Sacar
2 - Depositar
3 - Visualizar Extrato """

def depositar(value):
    global saldo

    if value < 0:
        print(f'Erro - Valor negativo')
    else:
        saldo += value
        extrato_dia['deposito']['qtd'] += 1
        extrato_dia['deposito']['value'] += value

def sacar(value):
    global saldo

    saques_realizados = extrato_dia['saque']['qtd']

    if value > saldo:
        print(f'Erro - Valor ultrapassa o saldo')
    elif value > VALOR_MAXIMO:
        print(f'Erro - Valor ultrapassa o máximo permitido (R$ {VALOR_MAXIMO})')
    elif saques_realizados >= MAXIMO_SAQUES:
        print(f'Erro - Quantidade máxima de saques atingida (Max: {MAXIMO_SAQUES})')
    else:
        saldo -= value
        extrato_dia['saque']['qtd'] += 1
        extrato_dia['saque']['value'] += value

        print(f'Sucesso - Saque realizado')

def exibe_extrato():
    for tipo, dados in extrato_dia.items():
        if dados['qtd'] == 0:
            print(f'{tipo.title()} - Não foi localizada movimentação')
        else:
            print(f"{tipo.title()} - R$ {dados['value']:.2f} - Quantidade - {dados['qtd']}")
    print(f"\nSaldo - R$ {saldo:.2f}")

while True:
    action = int(input(f'{menu}'))

    match action:
        case 1:
            print('========================================')
            value = float(input("Valor - R$"))
            sacar(value)
            continue
        case 2:
            print('========================================')
            value = float(input("Valor - R$"))
            depositar(value)
            continue
        case 3:
            print('========================================')
            exibe_extrato()
            continue