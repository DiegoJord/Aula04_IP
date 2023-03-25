q_atual = 100
q_maxima = 300
q_minima = 50

q_média = (q_maxima + q_minima) / 2

if q_atual > q_média:
    print("não efetuar a compra")
else:
    print("efetuar a compra")