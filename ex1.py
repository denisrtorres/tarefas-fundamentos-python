#Analise de Vendas
#Considere a tupla:
#Faça um programa que exiba
#a) a maior venda.
#b) a menor venda.
#c) calcule a média das vendas.
#d) informe quantas vendas ficaram acima da média.
vendas = (1500, 2300, 1800, 2900, 3200, 2100, 1700)

maior_venda = max(vendas)

menor_venda = min(vendas)

media_vendas = sum(vendas) / len(vendas)

# Exibição dos resultados
print(f"a) Maior venda: R$ {maior_venda}")
print(f"b) Menor venda: R$ {menor_venda}")
print(f"c) Média das vendas: R$ {media_vendas:.2f}")