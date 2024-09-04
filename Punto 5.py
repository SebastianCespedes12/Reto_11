def sum_filas(A): #Se crea una función que recibe una matriz
  B=[] #Se crea una lista vacia para almacenar los resultados
  for i in range(len(A)): # Se recorre las filas de la matriz
    sum=0 #Se inicializa la variable sum en 0
    for j in range(len(A[i])): # Se recorre las columnas de la matriz
      sum+=A[i][j] #Se suman los elementos de las filas de la matriz A
    B.append(sum) #Se añade el resultado a la lista vacia
  return B #Se retorna la lista B

A=[[1,2,3],[4,5,6],[7,8,9]] #B=[6,15,24]
sum_filas(A)