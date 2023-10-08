from Lexer import *

VT = list(tokens.keys()) # importa tokens

VN = [
    'Program',
    'ListaSentencias',
    'Sentencia',
    'SentenciaSi',
    'SentenciaRepetir',
    'SentenciaAsig',
    'SentenciaLeer',
    'SentenciaMostrar',
    'SentenciaFun',
    'Proc',
    'ListaPar',
    'Expresion',
    'Expresion2',
    'Termino',
    'Factor',
    'ListaSentencias_Prime',
    'ListaPar_Prime',
    'Expresion2_Prime',
    'Termino_Prime',
    'SentenciaSi_Prime',
    'Expresion_Prime'
    
]

P = {
    'Program': [
        ['ListaSentencias']
    ],
    'ListaSentencias': [
        ['Sentencia','ListaSentencias_Prime']
    ],
    'ListaSentencias_Prime' :[
        [';', 'Sentencia','ListaSentencias_Prime'],['λ']
    ],
    'Sentencia': [
        ['SentenciaSi'],
        ['SentenciaRepetir'],
        ['SentenciaAsig'],
        ['SentenciaLeer'],
        ['SentenciaMostrar'],
        ['SentenciaFun']
    ],
    'SentenciaSi': [ 
        ['si', 'Expresion', 'entonces', 'ListaSentencias', 'SentenciaSi_Prime'] 
    ],
    'SentenciaSi_Prime' : [ 
        ['sino', 'ListaSentencias', 'finsi'], ['finsi'] 
    ],
    'SentenciaRepetir': [
        ['repetir', 'ListaSentencias', 'hasta', 'Expresion']
    ],
    'SentenciaAsig': [
        ['id', 'equal', 'Expresion']
    ],
    'SentenciaLeer': [
        ['leer', 'id']
    ],
    'SentenciaMostrar': [
        ['mostrar', 'Expresion']
    ],
    'SentenciaFun': [
        ['func', 'Proc', 'finfunc']
    ],
    'Proc': [
        ['id', '(', 'ListaPar', ')', 'ListaSentencias']
    ],
    'ListaPar': [
        ['id','ListaPar_Prime']
    ],
    'ListaPar_Prime':[
        [';', 'id','ListaPar_Prime'],['λ']
    ],
    'Expresion': [
        ['Expresion2', 'Expresion_Prime']
    ],
    'Expresion_Prime' : [
        ['oprel', 'Expresion2'],['λ']
    ],
    'Expresion2': [
        ['Termino','Expresion2_Prime']
    ],
    'Expresion2_Prime':[
        ['opsuma', 'Termino','Expresion2_Prime'],['λ']
    ],
    'Termino': [
        ['Factor','Termino_Prime']
    ],
    'Termino_Prime':[
        ['opmult', 'Factor','Termino_Prime'],['λ']     
    ],
    'Factor': [
        ['(', 'Expresion', ')'],
        ['numero'],
        ['id']
    ]
}

# SD = {
#     'Program' : {token:[Pn] }
# }
SD = { 
    'Program' : {"si" : ['ListaSentencias'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['ListaSentencias'], "repetir" : ['ListaSentencias'], "hasta" : [], "leer" : ['ListaSentencias'],
                "mostrar" : ['ListaSentencias'], "equal" : [], "id" : ['ListaSentencias'], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'ListaSentencias' : {"si" : ['Sentencia','ListaSentencias_Prime'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['Sentencia','ListaSentencias_Prime'], "repetir" : ['Sentencia','ListaSentencias_Prime'], "hasta" : [],
                "leer" : ['Sentencia','ListaSentencias_Prime'], "mostrar" : ['Sentencia','ListaSentencias_Prime'], "equal" : [], 
                "id" : ['Sentencia','ListaSentencias_Prime'], "numero" : [], "oprel" : [], "(" : [], ")" : [],
                ";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Sentencia' : {"si" : ['SentenciaSi'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['SentenciaFun'], "repetir" : ['SentenciaRepetir'], "hasta" : [], "leer" : ['SentenciaLeer'],
                "mostrar" : ['SentenciaMostrar'], "equal" : [], "id" : ['SentenciaAsig'], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},
    
    'SentenciaSi' : {"si" : ['si', 'Expresion', 'entonces', 'ListaSentencias', 'SentenciaSi_Prime'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},
    
    'SentenciaSi_Prime' : {"si" : [], "sino" : ['sino', 'ListaSentencias', 'finsi'], "entonces" : [], "finsi" : ['finsi'], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]}, 
    
    'SentenciaRepetir' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : ['repetir', 'ListaSentencias', 'hasta', 'Expresion'], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaAsig' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id', 'equal', 'Expresion'], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaLeer' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : ['leer', 'id'],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaMostrar' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : ['mostrar', 'Expresion'], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaFun' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['func', 'Proc', 'finfunc'], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Proc' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id', '(', 'ListaPar', ')', 'ListaSentencias'], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'ListaPar' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id','ListaPar_Prime'], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},
                
    'Expresion' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['Expresion2', 'Expresion_Prime'], "numero" : ['Expresion2', 'Expresion_Prime'], "oprel" : [],
                "(" : ['Expresion2', 'Expresion_Prime'], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Expresion2' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['Termino','Expresion2_Prime'], "numero" : ['Termino','Expresion2_Prime'], "oprel" : [],
                "(" : ['Termino','Expresion2_Prime'], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Termino' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['Factor','Termino_Prime'], "numero" : ['Factor','Termino_Prime'], "oprel" : [],
                "(" : ['Factor','Termino_Prime'], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Factor' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id'], "numero" : ['numero'], "oprel" : [],
                "(" : ['(', 'Expresion', ')'], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'ListaSentencias_Prime' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [';','Sentencia','ListaSentencias_Prime'] , "opsuma" : [], "opmult" : [],'#':[]},

    'ListaPar_Prime' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [';','id','ListaPar_Prime'] , "opsuma" : [], "opmult" : [],'#':[]},

    'Expresion_Prime' :{"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : ['oprel', 'Expresion2'],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Expresion2_Prime' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : ['opsuma','Termino','Expresion2_Prime'], "opmult" : [],'#':[]},

    'Termino_Prime' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "numero" : [], "oprel" : [],
                "(" : [], ")" : [],";" : [] , "opsuma" : [], "opmult" : ['opmult', 'Factor','Termino_Prime'],'#':[]} 
}

