from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_sapore = Restaurante('sapore', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'Melhor pao da cidade')
prato_paozinho.aplicar_desconto()
restaurante_sapore.adicionar_no_cardapio(bebida_suco)
restaurante_sapore.adicionar_no_cardapio(prato_paozinho)


# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Ruddy', 'Japonesa')


restaurante_sapore.alternar_estado()

def main():
    restaurante_sapore.exibir_cardapio
    
if __name__ == '__main__':
    main()