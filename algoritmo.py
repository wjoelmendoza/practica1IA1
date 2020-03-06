from random import randint, random, uniform
from utils import *
#VARIABLES GLOBALES
_generacion = 0
_numpoblacion = 10
_numseleccionados
_maximas_generaciones = 50
_mejor_fitness = 80
__promedio_fitness = 61
#CALCULO DE fitness:

def poblacion_inicial():
    p_ini = []
    for x in range(3):
        i = uniform(-1, 1)
        p_ini.append(i)

    return p_ini

def evaluar(vec):
    signo = vec[0]
    val = vec[1]

    for i in range(2,6):
        val = val*2 + vec[i]

    if signo:
        val =  val * -1

    f = abs(val**2 + 4 * val - 192)

    return f

def poblacion(n):
    pob = []
    for i in range(n):
        v = poblacion_inicial()
        pob.append(v)

    return pob

def takeSecond(elem):
    return elem[1]

def seleccionar(m_pob, t_selec):
        v_calidad = []
        select = []

        for i in range(10):
            act = m_pob[i]
            c = evaluar(act)
            v_calidad.append((i,c))

        v_calidad.sort(reverse=False, key=takeSecond)

        for i in range(5):
            act = v_calidad[i]
            v = m_pob[act[0]]
            select.append(v)

        return select

def s_aleatorios(m_pob):
    t = len(m_pob)
    s = []
    m = t // 2
    print(m)
    for l in range(m):
        i = randint(0, t - 1)
        s.append(m_pob[i])

    return s

def s_torneo(m_pob):
    t = len(m_pob)

    if t < 16:
        return s_mejores(m_pob)

    limite = t // 4
    lim = limite;
    i = 0
    selec = []

    while i < 4:
        x = 0
        v = []

        while x < lim:
            v.append(m_pob[x])

        x += 1
        lim += limite

        s = s_mejores(v)

        selec = selec + s

        if lim > t:
            break

    return selec

def s_mejores(m_pob):
    v_calidad = []
    select = []
    t = len(m_pob)

    for i in range(t):
        act = m_pob[i]
        c = evaluar(act)
        v_calidad.append((i,c))

        v_calidad.sort(reverse=False, key=takeSecond)

    m = t // 2
    for i in range(m):
        act = v_calidad[i]
        v = m_pob[act[0]]
        select.append(v)

        return select

v = s_aleatorios([1, 2, 3, 4, 5, 6, 7, 8])
print(v)
#EMPAREJAMIENTO ALEATORIO...
def emparejar(padres):
    global _numpoblacion
    hijos = []
    tampadres = len(padres)
    for i in range(_numpoblacion - tampadres:
        index1 = randint(0,tampadres)
        index2 = randint(0,tampadres)
        while(index1 == index2):
            index2 = randint(0,tampadres)

        h1 = cruzar(padres[index1], padres[index2])
        h1 = mutar(h1)
        hijos.append(h1)
        
    
    for hijo in hijos:
        padres.append(hijo)

    return padres

def cruzar(v1, v2):
    vn = []

    if random() > .5:
        vn.append(v1[0])
    else:
        vn.append(v2[0])

    if random() > .5:
        vn.append(v1[1])
    else:
        vn.append(v2[1])

    if random() > .5:
        vn.append(v1[2])
    else:
        vn.append(v2[2])

    return vn

def mutar(hijo):

    for i in range(6):
        prob = random()
        if(prob > 0.5):
            hijo[i] = uniform(-1,1)

    return hijo

#METODO PARA EL CRITERIO DE FINALIZACION:
#1.maximo numero de generaciones(O no)
#2.el fitness promedio
#3.el mejor fitness de la poblacion

def criterio(flag,lst):
    if flag == '1':
        return criterio1(_maximas_generaciones)
    elif flag == '2':
        return criterio2(lst)
    else:
        return criterio3(lst)

def criterio3(lst):
    valbest = 77
    if valbest in lst:
        return True
    else:
        return None

def Average(lst): 
    return sum(lst) / len(lst)

def criterio2(lst):
    valpromedio = 61
    if Average(lst) >= valpromedio :
        return True
    else:
        return None

def criterio1(max):
    global _generacion
    if max == _generacion:
        return True
    else:
        return None





def main(flag_finalizacion,flag_seleccion,file_name):
    global _generacion
    global _numpoblacion
    _generacion = 0
    
    p0 = poblacion(_numpoblacion)
    print(p0)
    fin = criterio(flag_finalizacion,p0)
    while(fin == None):
        padres = seleccionar(p0,flag_seleccion)
        p0 = emparejar(padres)
        fin = criterio(flag_finalizacion,p0)
        _generacion += 1

    print(fin)
    print(_generacion)

