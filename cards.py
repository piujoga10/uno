especiais = [('transparent', '+4'), ('transparent', 'coringa')]

COLORED_CARDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+2', 'voltar', 'pular']

# class StandardCard:
#     def __init__(self, color, number):
#         self.color = color
#         self.number = number


colors = ['vermelho', 'azul', 'amarelo', 'verde']

deck = [(n, c) for n in colors for c in COLORED_CARDS]


print deck
print len(deck)
