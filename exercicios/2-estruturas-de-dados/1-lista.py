# Crie uma lista apenas com elementos numéricos
lista = []
numerica = [1, 2 ,3, 4, 5, 6]
print (numerica)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['python', 4, [1,2,3,4], True]
print (mista)
# Imprima na tela apenas os 5 primeiros elementos da lista
linguagens = ['python', 'r', 'julia']
print (linguagens)
linguagens_adicionais = ['c++','java', 'javascript','sql']
print (linguagens_adicionais)
linguagens.extend(linguagens_adicionais)
print (linguagens)
linguagens [:5]
print (linguagens)
# Crie um slice na lista para que imprima na tela os elementos de índice par
linguagens [0:2]
print (linguagens)
# Remova da lista o último item
linguagens.pop()
print (linguagens)
# Insira na lista um novo item
linguagens.append ('fortran')
print (linguagens)
# Remova da lista um item específico
linguagens.remove ('python')
print (linguagens)