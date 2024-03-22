class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
restaurante_sapore = Restaurante('Praca', 'Gourmet')
restaurante_carninha = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_sapore, restaurante_carninha]

print(restaurante_sapore)
print(restaurante_carninha)