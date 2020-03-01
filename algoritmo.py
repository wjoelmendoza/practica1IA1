from random import randint, random

def poblacion_inicial():
    p_ini = []
    for x in range(6):
        i = randint(0, 1)
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

def poblacion():
    solucion = []
    for i in range(10):
        v = poblacion_inicial()
        solucion.append(v)

    return solucion

def takeSecond(elem):
    return elem[1]

def seleccionar(m_pob):
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

def emparejar(padres):
    hijos = []

    h1 = cruzar(padres[0], padres[1])
    hijos.append(h1)
    h1 = cruzar(padres[3], padres[1])
    hijos.append(h1)
    h1 = cruzar(padres[0], padres[3])
    hijos.append(h1)
    h1 = cruzar(padres[4], padres[2])
    hijos.append(h1)
    h1 = cruzar(padres[2], padres[0])
    hijos.append(h1)

    for i in range(5):
        h = hijos[i]
        h = mutar(h)
        padres.append(h)

    return padres

def cruzar(v1, v2):
    vn = []

    vn.append(v1[0])
    vn.append(v1[1])
    vn.append(v1[2])

    vn.append(v2[3])
    vn.append(v2[4])
    vn.append(v2[5])

    return vn

def mutar(hijo):

    for i in range(6):
        prob = random()
        if(prob > 0.5):
            hijo[i] = randint(0,1)

    return hijo

def criterio(vec):
    for i in vec:
        calidad = evaluar(i)
        if calidad >= -0.05 and calidad <= 0.05:
            return i

    return None

def main():
    generacion = 0
    p0 = poblacion()
    print(p0)
    fin = criterio(p0)
    while(fin == None):
        padres = seleccionar(p0)
        p0 = emparejar(padres)
        fin = criterio(p0)
        generacion += 1

    print(fin)
    print(generacion)

