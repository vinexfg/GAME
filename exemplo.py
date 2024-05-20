vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]


print('2019_________________________________________________________________2019')
vendas_2019 = []
vendas_2020 = []


for produto, valor_2019, valor_2020 in vendas_produtos:
    vendas_2019.append((produto, valor_2019))

for produto, unidade in vendas_2019:
    print(f'O produto {produto} vendeu {unidade} unidades')
    print('__________________________________________')

print('2020_____________________________________________________________________2020')

for produto2, valor_2019, valor_2020 in vendas_produtos:
    vendas_2020.append((produto2, valor_2020))

for produto2, unidade2 in vendas_2020:
    print(f'O Produto {produto2} vendeu {unidade2} unidades')
    print('__________________________________________')


produto_mais_vendido_2019, unidade_mais_vendida_2019 = max(vendas_2019, key= lambda x: x[1])
print(f'O produto mais vendido em 2019 foi {produto_mais_vendido_2019} com {unidade_mais_vendida_2019} unidades vendidas.')
