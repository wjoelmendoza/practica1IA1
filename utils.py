import datetime
import pandas as pd

'''
_nombreDoc = ''
_criterioFinalizacion = ''
_valFinalizacion = 0
_metodoSeleccion = ''
_generaciones = 0
_mejorSolucion = 0
Con este metodo inicializamos las variables globales

def init(nombre,criterio,metodo):
    global _nombreDoc,_criterioFinalizacion,_valFinalizacion,_metodoSeleccion,_generaciones,_mejorSolucion 
    _nombreDoc = nombre
    _criterioFinalizacion = criterio
    _valFinalizacion = int(valcriterio)
    _metodoSeleccion = metodo
    _generaciones = 0
    _mejorSolucion = 0
    print('Inicializacion-----')
'''    
def load_file(file):
    return pd.read_csv(
<<<<<<< HEAD
        file,
        dtype= {'P1':'float64','P2':'float64','P3':'float64','NF':'float64'}
        )
def get_fitness(file,ls):
=======
        './temporales/'+file,
        dtype= {'P1':'float64','P2':'float64','P3':'float64','NF':'float64'}
        )
def get_fitness(file,ls):
    print("Entre a get_fitness().........")
>>>>>>> bj
    df = load_file(file)
    #print(df.head())
    #print(df.index)
    #print(df.sum())#SUMA POR COLUMNA
    #print(df.cumsum())#suma acumulada
    df['M1'] = df['P1']* ls[0]
    df['M2'] = df['P2']* ls[1]
    df['M3'] = df['P3']* ls[2]
    df['NC'] = df['M1']+ df['M2'] + df['M3'] 
    df['E'] = (df['NF'] - df['NC'])**2

<<<<<<< HEAD
    print(df.head())
=======
    #print(df.head())
>>>>>>> bj
    #print(df.shape[0])
    fit = df['E'].sum()/df.shape[0]
    fit = round(fit,2)
    print('FITNES CALCULADO::',fit)
    return fit

def escribir_en_bitacora(flagcriterio,seleccion,file,generaciones,solucion):
<<<<<<< HEAD
    
=======
>>>>>>> bj
    
    print("Entre a escribir_en_bitacora().........")
    f = open("bitacora.txt", "a")
    tiempo = datetime.datetime.now()
    strfinalizacion = 'Maximo numero de Generaciones-- '+str(flagcriterio) if flagcriterio == '1' else 'default'
    strfinalizacion = 'El mejor fitness de la poblacion-- '+str(flagcriterio) if flagcriterio == '2' else strfinalizacion
    strfinalizacion = 'El fitness promedio de la poblacion-- '+str(flagcriterio) if flagcriterio == '3' else strfinalizacion 
    
    strseleccion = 'Torneos, escojiendo el de mejor fitness' if seleccion == '1' else 'default'
    strseleccion = 'Los mejores padres(mejor fitness)' if seleccion == '2' else strseleccion
    strseleccion = 'Aleatorios' if seleccion == '3' else strseleccion
    contenido = [
        
        'Fecha de ejecución: '+tiempo.date().isoformat()+'\n',
        'Hora de ejecución: '+tiempo.time().isoformat()+'\n',
        
        'Nombre del documento de datos utilizado: ',file+'\n',
        'Criterio de finalización utilizado: ',strfinalizacion+'\n',
        'Método de selección: ',strseleccion,'\n',
        'No. Generaciones: ',str(generaciones)+'\n',
        'Mejor solucion: ',str(solucion)+'\n',
        '------------------------------\n',
        ] 
    f.writelines(contenido)
    f.close()    
