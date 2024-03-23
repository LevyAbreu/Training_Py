codigo_peca1, numero_p1, valor_unitario_p1 = map(float, input().split())
codigo_peca2, numero_p2, valor_unitario_p2 = map(float, input().split())

total_pagar = (numero_p1 * valor_unitario_p1) + (numero_p2 * valor_unitario_p2)

print("VALOR A PAGAR: R$ {:.2f}".format(total_pagar))
