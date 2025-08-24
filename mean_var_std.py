import numpy as np

def calculate(list):
        if len(list) != 9:
            raise ValueError ("List must contain nine numbers.")
            #convertendo array para numpy
        
        array_np = np.array(list)
        #transformando em uma matriz 3x3
        matriz = array_np.reshape(3, 3)

        calculations = {        
                'mean': [matriz.mean(axis=0).tolist(), # colunas
                        matriz.mean(axis=1).tolist(), # linhas
                        matriz.mean() # total
                        ],
                'variance': [matriz.var(axis=0).tolist(), 
                            matriz.var(axis=1).tolist(), 
                            matriz.var()],
                'standard deviation': [matriz.std(axis=0).tolist(), 
                                        matriz.std(axis=1).tolist(), 
                                        matriz.std()],
                'max': [matriz.max(axis=0).tolist(),
                        matriz.max(axis=1).tolist(), 
                        matriz.max()],
                'min': [matriz.min(axis=0).tolist(), 
                        matriz.min(axis=1).tolist(), 
                        matriz.min()],
                'sum': [matriz.sum(axis=0).tolist(),
                        matriz.sum(axis=1).tolist(), 
                        matriz.sum()]
        }

        return calculations
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8]
resultado = calculate(numeros)
print(resultado)