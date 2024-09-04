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

A=[[1,2],[3,4]]
B=[[4,5],[6,9]]
C=[]
suma_matrices(A,B)
resta_matrices(A,B)