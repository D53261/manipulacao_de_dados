import numpy as np

class Arrays:
    def __init__(self):
        self.arrays = []
        self.escolhido = 0

    def cria_arrays(self):
        self.arrays.append(np.random.randint(low=1, high=101, size=(np.random.randint(1, 10), np.random.randint(1, 10))))

    def mede_media_linhas(self):
        medias_linhas = [np.mean(self.escolhido[i]) for i in range(len(self.escolhido))]
        print(f'O indice da maior media das linhas da array é {medias_linhas.index(max(medias_linhas))}!')
        print(f'O indice da menor media das linhas da array é {medias_linhas.index(min(medias_linhas))}!')
    
    def mede_media_colunas(self):
        medias_colunas = [np.mean(self.escolhido.T[i]) for i in range(len(self.escolhido.T))]
        print(f'O indice da maior media das colunas da array é {medias_colunas.index(max(medias_colunas))}!')
        print(f'O indice da menor media das colunas da array é {medias_colunas.index(min(medias_colunas))}!')

if __name__ == "__main__":
    array = Arrays()
    array.cria_arrays()
    while True:
        for i in array.arrays:
            print(f'\n{i}')
        s_n = input("Deseja criar mais uma opção de array? \n(Digite 'S' para sim e 'N' para não) ").title()
        if s_n == "S":
            array.cria_arrays()
        elif s_n == "N":
            break
    escolhido = int(input('Digite a numeração do array que voce deseja: (ex: 1, 2, 3, ...) '))
    array.escolhido = array.arrays[escolhido-1]
    array.mede_media_linhas()
    array.mede_media_colunas()
    array.arrays.clear()
        
        
    

        

