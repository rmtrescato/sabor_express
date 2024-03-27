from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_sapore = Restaurante('sapore', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.0, 'Melhor pao da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_gelatina = Sobremesa('Gelatina', 3.0, 'Pote', 'grande', 'Teste')
sobremesa_gelatina.aplicar_desconto()
restaurante_sapore.adicionar_no_cardapio(bebida_suco)
restaurante_sapore.adicionar_no_cardapio(prato_paozinho)
restaurante_sapore.adicionar_no_cardapio(sobremesa_gelatina)

# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Ruddy', 'Japonesa')


restaurante_sapore.alternar_estado()

def main():
    restaurante_sapore.exibir_cardapio
    
if __name__ == '__main__':
    main()