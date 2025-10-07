#Funções 
def escolha_modelo(): #Preço do modelo 
    while True: 
        print('')  # Espaço 
        print('Entre com o modelo desejado: ') 
        print('MCS - Manga Curta Simples ') 
        print('MLS - Manga Longa Simples') 
        print('MCE - Manga Curta com Estampa') 
        print('MLE - Manga Longa com Estampa') 
        modelo = input('Escolha o modelo desejado: ') 
        if modelo == 'MCS': 
            preco = 1.80 
            return preco 
        elif modelo == 'MLS': 
            preco = 2.10 
            return preco 
        elif modelo == 'MCE': 
            preco = 2.90 
            return preco 
        elif modelo == 'MLE': 
            preco = 3.20 
            return preco 
        else: 
            print('Escolha inválida, entre com o modelo novamente. ') 
 
def num_camisetas(): #Quantidade de camisetas com desconto 
    while True: 
        try: 
            qtd_camisetas = int(input('Entre com o número de camisetas: ')) 
        except ValueError: # 
            print('Oops! Número inválido, tente novamente.') 
            print('')  #Espaço 
 
        else: 
 
            if qtd_camisetas < 20: #Menor que 20 não há desconto na venda 
                return qtd_camisetas 
 
            elif 20 <= qtd_camisetas < 200: #Igual ou maior que 20 e menor que 200 
                qtd_camisetas = qtd_camisetas - (qtd_camisetas * (5/100)) #Desconto de 5% 
                return qtd_camisetas 
 
            elif 200 <= qtd_camisetas < 2000: #Igual ou maior que 200 e menor que 2000 
                qtd_camisetas = qtd_camisetas - (qtd_camisetas * (7/100)) #Desconto de 7% 
                return qtd_camisetas 
 
            elif 2000 <= qtd_camisetas <= 20000: #Igual ou maior que 2000 e menor ou igual que 20000 
                qtd_camisetas = qtd_camisetas - (qtd_camisetas * (12/100)) #Desconto de 12% 
                return qtd_camisetas 
 
            else: #Maior que 20000, não é aceito pedidos nessa quantidade de camisetas 
                print('Não aceitamos tantas camisetas de uma vez') 
                print('Por favor, entre com o número de camisetas novamente.') 
                print('')  # Espaço 
 
def frete(): #Valor do frete 
    print('')  # Espaço 
    print('Escolha o tipo de frete: ') 
    print('Frete por transportadora (1) - R$100.00') 
    print('Frete por Sedex (2) - R$200.00') 
    print('Retirar pedido na fábrica (0) - R$0.00') 
    while True: 
        try: 
            valor = int(input('Digite a opção desejada: ')) 
        except ValueError:  # 
            print('Oops! Número inválido, tente novamente.') 
            print('')  #Espaço 
        else: 
            if valor == 0: #É cobrado um valor extra de 0 reais 
                return valor 
 
            if valor == 1: #É cobrado um valor extra de 100 reais 
                valor = 100.00 
                return valor 
 
            if valor == 2: #É cobrado um valor extra de 200 reais 
                valor = 200.00 
                return valor 
            else: 
                print('Escolha inválida, tente novamente. ') 
                print('') #Espaço 
 
#Programa Principal 
print('Bem vindo a fábrica de camisetas do Jason L. Frazão de Almeida!') #Tela de boas-vindas 
 
preco_modelo = escolha_modelo() #Executar a função e armazenar o preço retornado 
numero_camisetas = num_camisetas() #Executar a função e armazenar quantidade retornada 
frete = frete() #Executar a função e armazenar o valor do frete retornado 
total = (preco_modelo * numero_camisetas) + frete # Equivalente ao total = (modelo * num_camisetas) + frete 
 
print(f'Total: R${total} (Modelo:R${preco_modelo} * Quantidade (com desconto): {numero_camisetas} + frete R${frete}') 