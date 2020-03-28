from random import randint, random, uniform
from utils import *
#VARIABLES GLOBALES
_generacion = 0
_numpoblacion = 15
_numseleccionados = 10
_maximas_generaciones = 50
_mejor_fitness = 80
__promedio_fitness = 61
#CALCULO DE fitness:

def poblacion_inicial():
    #print("Entre a poblacion_inicial().........")
    p_ini = []
    for x in range(3):
        i = uniform(-1, 1)
        p_ini.append(i)

    return p_ini
def poblacion(n):
    print("Entre a poblacion().........")
    pob = []
    for i in range(n):
        v = poblacion_inicial()
        pob.append(v)

    return pob

def takeSecond(elem):
    #print("Entre a takeSecond().........")
    return elem[1]

def seleccionar(m_pob, t_selec,filename):

    print("seleccionar().........")
    #v_calidad = []
    #select = []
    
    if t_selec == '3':
        return s_aleatorios(m_pob)
    elif t_selec == '1':
        return s_torneo(m_pob,filename)
    else:
        return s_mejores(m_pob,filename)

def s_aleatorios(m_pob):
    print("Entre a s_aleatorios().........")
    t = len(m_pob)
    s = []
    m = t // 2
    print(m)
    for l in range(m):
        i = randint(0, t - 1)
        s.append(m_pob[i])

    return s

def s_torneo(m_pob,filename):
    print("Entre a s_torneo().........")
    t = len(m_pob)

    if t < 16:
        return s_mejores(m_pob,filename)

    limite = t // 4
    lim = limite
    i = 0
    selec = []

    while i < 4:
        x = 0
        v = []

        while x < lim:
            v.append(m_pob[x])

        x += 1
        lim += limite

        s = s_mejores(v,filename)

        selec = selec + s

        if lim > t:
            break

    return selec

def s_mejores(m_pob,filename):
    select = []
    print("Entre a s_mejores().........")
    v_calidad = get_fitness_poblacion(m_pob,filename)
    #print("Vector de calidad:",v_calidad)
    #v_calidad = mejor_solucion(lfits)
    v_calidad.sort(reverse=False, key=takeSecond)
    #print("(2)Vector de calidad:",v_calidad)
    t = len(m_pob)
    '''
    for i in range(t):
        act = m_pob[i]
        c = evaluar(act)
        v_calidad.append((i,c))

        v_calidad.sort(reverse=False, key=takeSecond)
    '''
    m = t // 2
    for i in range(m):
        #act = v_calidad[i]
        v = v_calidad[i][0]
        select.append(v)

    return select   

#v = s_aleatorios([1, 2, 3, 4, 5, 6, 7, 8])
#print(v)
#EMPAREJAMIENTO ALEATORIO...
def emparejar(padres):
    print("Entre a emparejar().........")
    print("Padres: ",padres)
    global _numpoblacion
    hijos = []
    tampadres = len(padres)
    for i in range(_numpoblacion - tampadres):
        index1 = randint(0,tampadres-1)
        index2 = randint(0,tampadres-1)
        #print("alv: ",index1,index2)
        while(index1 == index2):
            
            index2 = randint(0,tampadres-1)

        h1 = cruzar(padres[index1], padres[index2])
        h1 = mutar(h1)
        hijos.append(h1)
        
    
    for hijo in hijos:
        padres.append(hijo)

    return padres

def cruzar(v1, v2):
    #print("Entre a cruzar().........")
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
    #print("Entre a mutar().........")
    pos = randint(0,2)
    valrand = uniform(-0.3,0.3)
    valrand = round(valrand,3)
    hijo[pos] = valrand
    return hijo

#METODO PARA EL CRITERIO DE FINALIZACION:
#1.maximo numero de generaciones(O no)
#2.el fitness promedio
#3.el mejor fitness de la poblacion

def criterio(flag,lst,filename):
    print("Entre a criterio().........")
    if flag == '1':
        return criterio1(_maximas_generaciones,lst,filename)
    elif flag == '2':
        return criterio2(lst,filename)
    else:
        return criterio3(lst,filename)

def get_fitness_poblacion(lst,filedata):
    print("get_fitness_poblacion().........")
    lfits = []
    for s in lst:
        lfits.append((s,get_fitness(filedata,s)))
    return lfits
     
def mejor_solucion(lfits):
    print("Entro a mejor_solucion()")
    #print(lfits)
    best = lfits[0]
    valbest = lfits[0][1]
    print(valbest)
    for v in lfits:
        #print(v)
        #print(v[0])
        #print(v[1])
        if v[1] < valbest:
            best = v
            valbest = v[1]
    print(best)
    return best
def criterio2(lst,filename):
    print("Entre a criterio3().........")
    contsbest = 200
    lfits = get_fitness_poblacion(lst,filename)
    valbest = mejor_solucion(lfits)
    print("Mejor solucion encontrada: ",valbest)
    if valbest[1] <=  contsbest:
        return valbest
    else:
        return None
   

def my_sum(lfits):
    sum=0
    for item in lfits:
        sum+=item[1]
    return sum

def criterio3(lst,filename):
    print("Entre a criterio2().........")
    valpromedio = 150
    masmenos = 150
    lfits = get_fitness_poblacion(lst,filename) 
    avg = my_sum(lfits) / len(lfits)
    print("Promedio: ",avg)
    if avg <= valpromedio+masmenos or valpromedio-masmenos >= avg :
        valbest = mejor_solucion(lfits)
        return valbest
    else:
        return None

def criterio1(max,lst,filename):
    print("Entre a criterio1().........")
    global _generacion
    if max == _generacion:
        lfits = get_fitness_poblacion(lst,filename)
        return mejor_solucion(lfits)
    else:
        return None





def main(flag_finalizacion,flag_seleccion,file_name):
    print("Entre a main().........")
    global _generacion
    global _numpoblacion
    
    
    p0 = poblacion(_numpoblacion)
    print(p0)
    fin = criterio(flag_finalizacion,p0,file_name)
    _generacion = 1
    while(fin == None):
        padres = seleccionar(p0,flag_seleccion,file_name)
        p0 = emparejar(padres)
        #print("Termino de emparejar")
        fin = criterio(flag_finalizacion,p0,file_name)
        _generacion += 1

    
    print(fin)
    print(_generacion)
    escribir_en_bitacora(flag_finalizacion,flag_seleccion,file_name,_generacion,fin)
    return fin