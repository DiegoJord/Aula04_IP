n_da_conta = 20201010
saldo = 1100
debito = 500
credito = 1000

saldo_atual = (saldo - debito) + credito

if saldo_atual >= 0:
    print(f"seu saldo de R${saldo_atual} é positivo")
else:
    print(f"seu saldo de R${saldo_atual} é negativo")

