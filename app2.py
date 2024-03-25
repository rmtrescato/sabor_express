from modelos.restaurantes import Restaurante

restaurante_sapore = Restaurante('sapore', 'Gourmet')
restaurante_sapore.receber_avaliacao('Gui', 10)
restaurante_sapore.receber_avaliacao('Lari', 8)
restaurante_sapore.receber_avaliacao('Maria', 7.7)

# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Ruddy', 'Japonesa')


restaurante_sapore.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
    
if __name__ == '__main__':
    main()