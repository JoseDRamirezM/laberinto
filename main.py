def leer(nombre_archivo):
  return [line.splitlines() for line in (open(nombre_archivo, "r"))] 
  
def arreglar(lista):
  return [i[0].split() for i in lista] 

def get_laberinto(nombre_archivo):
  return arreglar(leer(nombre_archivo))

def buscar(x, y, matriz):
  if matriz[x][y] == 'Y':
      print ("Encontrado! %d,%d" % (x, y))
      return True
  elif matriz[x][y] == '1':
      print ('no puedo %d,%d' % (x, y))
      return False
  elif matriz[x][y] == '3':
      print ('ya estuve %d,%d' % (x, y))
      return False

  print ('actual %d,%d' % (x, y))
  
  matriz[x][y] = '3'
  #Aqui esta el problema de las matrices que no son cuadradas, x < len(matriz)-1 , y < len(matriz[0])-1 
  if ((x < len(matriz)-1 and buscar(x+1, y,matriz)) or (y > 0 and buscar(x, y-1,matriz)) or (x > 0 and buscar(x-1, y,matriz)) or (y < len(matriz[0])-1 and buscar(x, y+1,matriz))):
    return True
  return False

def init(lista, matriz):
  if(buscar(lista[0], lista[1], matriz)):
    print("SOLUCIONADO!")
  else : print(":(")

def buscar_x(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return ([cont,matriz[0].index("X")])
    return buscar_x(matriz[1:],cont+1)  

init(buscar_x(get_laberinto("l4.txt"),0),get_laberinto("l4.txt"))