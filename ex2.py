#Dada a tupla: numeros = (5, 2, 8, 2, 9, 2, 5, 7, 8, 5)
#Crie um programa que:
#a) Descubra todos os números que aparecem mais de uma vez.
#b) Mostre quantas vezes cada um deles aparece.
#Exemplo de saída
#5 aparece 3 vezez
#2 aparece 3 vezes
#8 aparece 2 vezes

numeros = (5, 2, 8, 2, 9, 2, 5, 7, 8, 5)

exibidos = set()

#Loop para verificar cada número na tupla
for num in numeros:
    #Conta a frequência do número
    quantidade = numeros.count(num)
    
    #Verifica se aparece mais de uma vez e se ainda não foi exibido
    if quantidade > 1 and num not in exibidos:
        print(f"{num} aparece {quantidade} vezes")
        exibidos.add(num)