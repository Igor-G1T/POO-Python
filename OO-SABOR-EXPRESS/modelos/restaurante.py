class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

#print(dir(vars(restaurante_praca)),'\n')

#1#
restaurante_praca.categoria = 'Italiana'

#2#
print(f'O nome do restaurante é:',restaurante_praca.nome,'\n')

#3#
def verify(restaurante):
    if (restaurante.ativo == False):
        print('O restaurante está: Inativo\n')
    else:
        print('O restaurante está: Ativado\n')
verify(restaurante_praca)

#4# 
categoria = Restaurante().categoria
if(categoria == ''):
    print('categoria está vazia\n')
else:
    print(categoria,'\n')

#5#
restaurante_praca.nome = 'Bistrô'
print(f'Nome alterado: ',restaurante_praca.nome,'\n')

#6#
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

#7#
print(restaurante_pizza.categoria, '\n')

#8#
restaurante_pizza.ativo = True
verify(restaurante_pizza)

#9#
print(f'Nome: ',restaurante_praca.nome, '\nCategoria: ',restaurante_praca.categoria)

'''Exercícios
        1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

        2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

        3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

        4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

        5. Altere o valor do atributo nome para 'Bistrô'.

        6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

        7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

        8. Mude o estado da instância restaurante_pizza para ativo.

        9. Imprima no console o nome e a categoria da instância restaurante_praca.

'''