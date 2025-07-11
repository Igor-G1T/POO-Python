from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.recive_aval('Gui', 10)
restaurante_praca.recive_aval('Gui', 10)
restaurante_praca.recive_aval('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()