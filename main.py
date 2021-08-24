class Nodo:
    def __init__(self, nombre):
        self.explorado = 0
        self.nombre = nombre
        self.vecinos = {}

#definimos las variables
nodos = {} #lista
inicio = 'Arad'
objetivo = 'Bucharest'
explorado = [] #tuplas //para caminos
frontera = [] #las fronteras
camino = []
f = open("/media/dliebel/DatosLinux/Universidad/ia/algoritmo_busqueda_profundidad/input.txt", "rb")
for line in f:
    linea = line.decode('UTF-8')
    c1, c2, distancia = linea.split(",")
    if c1 not in nodos:
        nodos[c1] = Nodo(c1)
    if c2 not in nodos:
        nodos[c2] = Nodo(c2)
    nodos[c1].vecinos[c2] = distancia
    nodos[c2].vecinos[c1] = distancia


def initFrontera():
    ''' Inicia la frontera 
    '''
    frontera.append(inicio)
    nodos[inicio].padre = ''

def elegirNodo():
    ''' se eliege el nodo
    '''
    node = frontera.pop()
    if testObjetivo(node):
        print (objetivo)
        caminoCosto = calculoCamino(objetivo)
        print ("el Costo del camino es {}", caminoCosto)
        print ("el camino seleccionado es {}",camino)
        exit() ## se encuenta el camino costo mas bajo y salimos 
    return node

def calculoCamino(cnode):
    '''Calcula el costo del camino
    '''
    camino.append(cnode)
    if nodos[cnode].padre == '':
        return 0
    else:
        cpadre = nodos[cnode].padre
        caminoCosto = calculoCamino(cpadre)+int(nodos[cnode].vecinos[cpadre])
        return caminoCosto

def testObjetivo(curnode):
    '''comprueba el objetivo 
    '''
    if curnode == objetivo:
        return True
    return False

def busqueda():
    if not frontera:
        print ("failure")
        exit()
    curnode = elegirNodo()
    nodos[curnode].explorado = 1
    explorado.append(curnode)
    for vecino in nodos[curnode].vecinos.keys():
        if vecino in frontera:
            continue
        if vecino in explorado:
            continue
        frontera.append(vecino)
        nodos[vecino].padre = curnode



initFrontera()

while True:
    busqueda()
    print (frontera)
  

