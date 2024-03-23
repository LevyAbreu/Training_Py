nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = 0.15 * total_vendas

total_receber = salario_fixo + comissao

print("TOTAL = R$ {:.2f}".format(total_receber))
