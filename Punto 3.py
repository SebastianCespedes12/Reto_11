def tran_matr(A): #Se crea una función que recibe una matriz
  B=[] #Se crea una matriz vacia para almacenar los resultados
  for i in range(len(A[0])): #Se recorre las columnas de la matriz
    fila_res=[]   # Se crea una lista vacia para almacenar los resultados
    for j in range(len(A)): #Se recorre las filas de la matriz
      fila_res.append(A[j][i]) #Se añade a la lista vacia los elementos de la matriz A en la posición j,i
    B.append(fila_res) #Se añade la lista con los resultados a la matriz B
  return B #Se retorna la matriz B

A=[[1,2],[3,4],[5,6]] #B=[[1,3,5],[2,4,6]]
tran_matr(A)