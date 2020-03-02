from random import randint, random, uniform

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

