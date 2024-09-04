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
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
prod_matr(A,B)
