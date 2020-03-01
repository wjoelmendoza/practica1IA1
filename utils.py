import datetime
import pandas as pd
#Aqui tendria que ir la logica del codigo genetico
_nombreDoc = ''
_criterioFinalizacion = ''
_valFinalizacion = 0
_metodoSeleccion = ''
_generaciones = 0
_mejorSolucion = 0
#Con este metodo inicializamos las variables globales
def init(nombre,criterio,valcriterio,metodo):
    global _nombreDoc,_criterioFinalizacion,_valFinalizacion,_metodoSeleccion,_generaciones,_mejorSolucion 
    _nombreDoc = nombre
    _criterioFinalizacion = criterio
    _valFinalizacion = int(valcriterio)
    _metodoSeleccion = metodo
    _generaciones = 0
    _mejorSolucion = 0
    print('Inicializacion-----')
    
def load_file():
    global _nombreDoc
    #data = pd.read_csv(_nombreDoc) 
    #print(data.head())
    return pd.read_csv(_nombreDoc)

def escribir_en_bitacora():
    global _nombreDoc,_criterioFinalizacion,_valFinalizacion,_metodoSeleccion,_generaciones,_mejorSolucion 
    
    f = open("bitacora.txt", "a")
    tiempo = datetime.datetime.now()
    strfinalizacion = 'Maximo numero de Generaciones-- '+str(_valFinalizacion) if _criterioFinalizacion == '1' else 'default'
    strfinalizacion = 'El mejor fitness de la poblacion-- '+str(_valFinalizacion) if _criterioFinalizacion == '2' else strfinalizacion
    strfinalizacion = 'El fitness promedio de la poblacion-- '+str(_valFinalizacion) if _criterioFinalizacion == '3' else strfinalizacion 
    
    strseleccion = 'Torneos, escojiendo el de mejor fitness' if _metodoSeleccion == '1' else 'default'
    strseleccion = 'Los mejores padres(mejor fitness)' if _metodoSeleccion == '2' else strseleccion
    strseleccion = 'Aleatorios' if _metodoSeleccion == '3' else strseleccion
    contenido = [
        
        'Fecha de ejecución: '+tiempo.date().isoformat()+'\n',
        'Hora de ejecución: '+tiempo.time().isoformat()+'\n',
        
        'Nombre del documento de datos utilizado: ',_nombreDoc+'\n',
        'Criterio de finalización utilizado: ',strfinalizacion+'\n',
        'Método de selección: ',strseleccion,'\n',
        'No. Generaciones: ',str(_generaciones)+'\n',
        'Mejor solucion: ',str(_mejorSolucion)+'\n',
        '------------------------------\n',
        ] 
    f.writelines(contenido)
    f.close()    
