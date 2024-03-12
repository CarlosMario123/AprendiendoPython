import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

datos = []
datos1 = []
for i in range(100000):
    data = random.randint(1200,1800)
    datos.append(data)
    data1 = random.randint(1200,2800)
    datos1.append(data1)
    

# Datos de ventas mensuales para dos productos en una tienda
ventas_producto_a = np.array(datos)
ventas_producto_b = np.array(datos1)    


# Calcular la desviación estándar para cada producto
desviacion_producto_a = np.std(ventas_producto_a)
desviacion_producto_b = np.std(ventas_producto_b)

# Imprimir las desviaciones estándar
print(f'Desviación Estándar Ventas Producto A: {desviacion_producto_a:.2f}')
print(f'Desviación Estándar Ventas Producto B: {desviacion_producto_b:.2f}')

# Visualizar la distribución de ventas mediante un boxplot
sns.boxplot(data=[ventas_producto_a, ventas_producto_b], notch=True)
plt.xticks([0, 1], ['Producto A', 'Producto B'])
plt.title('Variabilidad en Ventas Mensuales por Producto')
plt.ylabel('Ventas')
plt.show()
