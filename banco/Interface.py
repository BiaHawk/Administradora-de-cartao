from arvore import Node
from arvore import ArvoreTricolor #importação das classes Node e ArvoreTricolor

def comparahora(func, hora): #função que checa se o tempo da compra bate com o tempo de funcionamento
    print(func)
    print(hora)
    hora1 = int(func[0][0]) *60 + int(func[0][1])
    hora2 = int(func[1][0]) *60 + int(func[1][1])
    hora3 = int(hora[0]) * 60 + int(hora[1])
    if hora3 < hora1 or hora3 > hora2:
        return False
    return True



arvore_cartao = ArvoreTricolor()
arvore_loja = ArvoreTricolor()
while True:
    print('''Digite a operação que deseja realizar:

1 - Cadastrar novo cartão de credito
2 - Cadastrar nova loja
3 - Cancelar cartão de credito
4 - Cancelar cadastro de loja
5 - Realizar compra
6 - Relatoria de compras por cartão
7 - Relatorio de compras por loja
0 - Sair''')
    n = input()
    if n == '0':
        break
    
    elif n == '1':
        lista = []
        nome = input('Digite seu Nome: ')
        chave = 0
        for e in nome:
            chave += ord(e)
        numero = input('Digite o número do cartão: ')
        limiteT = input('Digite o limite total do seu cartão: ')
        limiteD = input('Digite o limite disponivel do seu cartão: ')
        if limiteD > limiteT:
            print('Erro: Limite disponivel maior que total \n')
            continue
        lista.append(nome)
        lista.append(numero)
        lista.append(int(limiteT))
        lista.append(int(limiteD))
        lista.append([])
        arvore_cartao.insert(chave, lista)
        
    elif n == '2':
        lista = []
        nome = input('Digite o nome da loja: ')
        lista.append(nome)
        chave = 0
        for e in nome:
            chave += ord(e)
        lista.append(input('Digite o endereço da loja: '))
        horafunc = input('Digite o horario de funcionamento: ').split('-')
        for op in range(2):
            horafunc[op] = horafunc[op].split(':')
        lista.append(horafunc)
        lista.append([])
        lista.append(0)
        arvore_loja.insert(chave, lista)

    elif n == '3':
        nome = input('Informe o nome do titular do cartão: ')
        numero = input('Informe o número do cartão: ')
        chave = 0
        for e in nome:
            chave += ord(e)
        no = arvore_cartao.search(chave, nome)
        if no != None:
            arvore_cartao.delete(no)
        else:
            print('Cartão não cadastrado')

    elif n == '4':
        nome = input('Informe o nome da loja: ')
        chave = 0
        for e in nome:
            chave += ord(e)
        no = arvore_loja.search(chave, nome)
        if no != None:
            arvore_loja.delete(no)
        else:
            print('Loja não cadastrada')

    elif n == '5':
        nomeC = input('Informe o nome do titular do cartão: ')
        chaveC = 0
        for e in nomeC:
            chaveC += ord(e)
        numero = input('Informe o número do cartão: ')
        nomeL = input('Informe o nome da loja onde será realizado a compra: ')
        chaveL = 0
        for e in nomeL:
            chaveL += ord(e)
        horario = input('Informe o horario da compra: ').split(':')
        valor = int(input('Informe o valor da compra: '))
        noC = arvore_cartao.search(chaveC, nomeC)
        noL = arvore_loja.search(chaveL, nomeL)
   
        if noC != arvore_cartao.vazio and noL != arvore_loja.vazio:
            if comparahora(noL.getDado()[2],horario) and valor <= noC.getDado()[3]:#Uso da função comparahora e compartação do limite do cartão com o valor
                noC.getDado()[3] -= valor
                noL.getDado()[4] += valor *0,2
                listaC = []
                listaC.append(nomeL)
                listaC.append(valor)
                listaC.append(horario)
                listaL = []
                listaL.append(nomeC)
                listaL.append(valor)
                listaL.append(horario)
                noC.getDado()[4].append(listaC)
                noL.getDado()[3].append(listaL)
                print('Transação aceita')
            else:
                print('Transação negada')
        else:
            print('Transação negada')
    elif n == '6':
        nome = input('Informe o nome do titular do cartão: ')
        chave = 0
        for e in nome:
            chave += ord(e)
        numero = input('Informe o número do cartão: ')
        no = arvore_cartao.search(chave, nome)
        if no != None:
            for e in no.getDado()[4]: #Uso do print com format e quebra de linha com \n
                print('Nome da Loja: {} \nValor da compra: R$ {} \nHorario da compra: {}:{} h \n'.format(e[0],e[1],e[2][0], e[2][1]))

    elif n == '7':
        nome = input('Informe o nome da loja: ')
        chave = 0
        for e in nome:
            chave += ord(e)
        no = arvore_loja.search(chave, nome)
        if no != None:
            for e in no.getDado()[3]:
                print('Nome da Loja: {} \nValor da compra: R$ {} \nHorario da compra: {}:{} h'.format(e[0],e[1],e[2][1], e[2][0]))
            print('Comissão: {}\n'.format(no.getDado()[4]))





            
        

