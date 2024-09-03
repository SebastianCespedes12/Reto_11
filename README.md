# Reto_11

>#### 1.Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación. 
```python
def filas_colum(a:int,b:int)->int: #Se crea una función que recibe dos matrices
  if len(a) == len(b) and len(a[0]) == len(b[0]):  #Se verifica que la cantidad de filas y columnas de las dos matrices sean iguales
    return True #Si se cumple la condición se retorna True
  else: 
    return False #Si no se cumple la condición se retorna False

def suma_matrices(A,B):
  C=[] #Se crea una matriz vacia para almacenar los resultados
  if filas_colum(A,B): #Se verifica que la cantidad de columnas y filas de las dos matrices sean iguales(condicion para ejecutar una suma/resta de matrices)
    for i in range(len(A)): #Se recorre las filas 
      fila_res=[] #Se crea una lista vacia para almacenar los resultados
      for j in range(len(A[i])): #Se recorre las columnas
        num=A[i][j]+B[i][j] #Se suman los números de las matrices, se suman los números de la misma posición
        fila_res.append(num) #Se agrega el resultado a la lista vacia
      C.append(fila_res) #Se agrega la lista con los resultados a la matriz C
    return C #Se retorna la matriz C
  else:
    print("Las matrices son de distinto tamaño")

def resta_matrices(A,B):
  C=[] #Se crea una matriz vacia para almacenar los resultados
  if filas_colum(A,B):
    for i in range(len(A)): #Se recorre las filas
      fila_res=[] #Se crea una lista vacia para almacenar los resultados
      for j in range(len(A[i])): # Se recorre las columnas
        num=A[i][j]-B[i][j] #Se restan los números de las matrices, se restan los números de la misma posición
        fila_res.append(num) #Se agrega el resultado a la lista vacia
      C.append(fila_res) #Se agrega la lista con los resultados a la matriz C
    return C #Se retorna la matriz C
  else:
    print("Las matrices son de distinto tamaño")
```
>#### 2.Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación. 
```python
def col1_fil2 (a,b):
  if len(a[0]) == len(b): # Se verifica que el numero de columnas de la primera matriz , sea igual al numero de filas de la segunda matriz(condicion paara producto de matrices)
    return True 
  else:
    return False

#fila i de A,por colmn j de B
def prod_matr(A,B):
  if col1_fil2(A,B):   
    C=[] #Se crea una matriz vacia para almacenar los resultados                     
    for i in range(len(A)): #Se recorre las filas de la matriz A            
      fila_res=[] #Se crea una lista vacia para almacenar las filas con los resultados
      for j in range(len(B[0])): #Se recorre las columnas de la matriz B
        num = 0 # Se inicializa la variable num en 0
        for k in range(len(B)): #Se recorre las filas de la matriz B     
          num += A[i][k] * B[k][j] #Se multiplica la fila i de la matriz A por la columna j de la matriz B y se suma el resultado total
        fila_res.append(num) #Se añade el resultado a la lista vacia de la fila                         
      C.append(fila_res)  #Se añade la lista de filas con los resultados a la matriz C
    return C #Se retorna la matriz C
  else:
    print("El numero de columnas de la primera matriz es diferente al numero de filas de la segunda matriz")

```
>#### 3.Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
def tran_matr(A): #Se crea una función que recibe una matriz
  B=[] #Se crea una matriz vacia para almacenar los resultados
  for i in range(len(A[0])): #Se recorre las columnas de la matriz
    fila_res=[]   # Se crea una lista vacia para almacenar los resultados
    for j in range(len(A)): #Se recorre las filas de la matriz
      fila_res.append(A[j][i]) #Se añade a la lista vacia los elementos de la matriz A en la posición j,i
    B.append(fila_res) #Se añade la lista con los resultados a la matriz B
  return B #Se retorna la matriz B
```
>#### 4.Desarrollar un programa que sume los elementos de una columna dada de una matriz.
```python
def sum_colm(A): # Se crea una función que recibe una matriz
  B=[] #Se crea una lista vacia para almacenar los resultados
  for i in range(len(A[0])): #Se recorre las columnas de la matriz
    sum=0 #Se inicializa la variable sum en 0
    for j in range(len(A)): #Se recorre las filas de la matriz
      sum+=A[j][i] #Se suma los elementos de las columnas de la matriz A 
    B.append(sum) #Se añade el resultado a la lista vacia
  return B #Se retorna la lista B
```
>#### 5.Desarrollar un programa que sume los elementos de una fila dada de una matriz. 
```python
def sum_filas(A): #Se crea una función que recibe una matriz
  B=[] #Se crea una lista vacia para almacenar los resultados
  for i in range(len(A)): # Se recorre las filas de la matriz
    sum=0 #Se inicializa la variable sum en 0
    for j in range(len(A[i])): # Se recorre las columnas de la matriz
      sum+=A[i][j] #Se suman los elementos de las filas de la matriz A
    B.append(sum) #Se añade el resultado a la lista vacia
  return B #Se retorna la lista B
```
