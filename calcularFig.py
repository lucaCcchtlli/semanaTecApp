import math
import pandas as pd

from figuras import rectangulo, triangulo, circulo


df = pd.read_csv("figuras.csv")
print("El archivo ha sido leído")

for index, row in df.iterrows():
        print(f"Fila {index}: FIGURA={row['FIGURA']}, MEDIDA1={row['MEDIDA1']}, MEDIDA2={row['MEDIDA2']}")
        if (row['FIGURA'] == 'r'):
                print(rectangulo(row['MEDIDA1'], row['MEDIDA2']))
        elif (row['FIGURA'] == 't'):
                print(triangulo(row['MEDIDA1'], row['MEDIDA2']))
        elif (row['FIGURA'] == 'c'):
        	print(circulo(row['MEDIDA1'], row['MEDIDA2']))
