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
    'ListaSentecias_Prime',
    'ListaPar_Prime',
    'Expresion2_Prime',
    'Termino_Prime'
]

P = {
    'Program': [
        ['ListaSentencias']
    ],
    'ListaSentencias': [
        ['Sentencia','ListaSentecias_Prime']
    ],
    'ListaSentecias_Prime' :[
        [';', 'Sentencia'],['λ']
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
        ['si', 'Expresion', 'entonces', 'ListaSentencias', 'sino', 'ListaSentencias', 'finsi'],
        ['si', 'Expresion', 'entonces', 'ListaSentencias', 'finsi']
    ],

    ## sugerencia
    ## 'SentenciaSi': [ ['si', 'Expresion', 'entonces', 'ListaSentencias', 'SentenciaSi_Prime'] ],
    ## 'SentenciaSi_Prime : [ ['sino', 'ListaSentencias', 'finsi'], ['λ'] ],


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
        ['Expresion2', 'oprel', 'Expresion2'],
        ['Expresion2']
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
        [ 'opmult', 'Factor','Termino_Prime'],['λ']     
    ],
    'Factor': [
        ['(', 'Expresion', ')'],
        ['num'],
        ['id']
    ]
}

# SD = {
#     'Program' : {token:[Pn] }
# }
SD = { 
    'Program' : {"si" : ['ListaSentencias'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['ListaSentencias'], "repetir" : ['ListaSentencias'], "hasta" : [], "leer" : ['ListaSentencias'],
                "mostrar" : ['ListaSentencias'], "equal" : [], "id" : ['ListaSentencias'], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'ListaSentencias' : {"si" : ['Sentencia','ListaSentecias_Prime'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['Sentencia','ListaSentecias_Prime'], "repetir" : ['Sentencia','ListaSentecias_Prime'], "hasta" : [],
                "leer" : ['Sentencia','ListaSentecias_Prime'], "mostrar" : ['Sentencia','ListaSentecias_Prime'], "equal" : [], 
                "id" : ['Sentencia','ListaSentecias_Prime'], "num" : [], "oprel" : [], "parentesis1" : [], "parentesis2" : [],
                "puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Sentencia' : {"si" : ['SentenciaSi'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['SentenciaFun'], "repetir" : ['SentenciaRepetir'], "hasta" : [], "leer" : ['SentenciaLeer'],
                "mostrar" : ['SentenciaMostrar'], "equal" : [], "id" : ['SentenciaAsig'], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},
    ############################### chusmear esto con linea 50 ###########################
    'SentenciaSi' : {"si" : ['si', 'Expresion', 'entonces', 'ListaSentencias', 'sino', 'ListaSentencias', 'finsi'], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},
    ######################################################################################
    'SentenciaRepetir' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : ['repetir', 'ListaSentencias', 'hasta', 'Expresion'], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaAsig' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id', 'equal', 'Expresion'], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaLeer' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : ['leer', 'id'],
                "mostrar" : [], "equal" : [], "id" : [], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaMostrar' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : ['mostrar', 'Expresion'], "equal" : [], "id" : [], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'SentenciaFun' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : ['func', 'Proc', 'finfunc'], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Proc' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id', '(', 'ListaPar', ')', 'ListaSentencias'], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'ListaPar' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id','ListaPar_Prime'], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},
                
    'Expresion' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['Expresion2'], "num" : ['Expresion2'], "oprel" : [],
                "parentesis1" : ['Expresion2'], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Expresion2' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['Termino','Expresion2_Prime'], "num" : ['Termino','Expresion2_Prime'], "oprel" : [],
                "parentesis1" : ['Termino','Expresion2_Prime'], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Termino' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['Factor','Termino_Prime'], "num" : ['Factor','Termino_Prime'], "oprel" : [],
                "parentesis1" : ['Factor','Termino_Prime'], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},

    'Factor' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : ['id'], "num" : ['num'], "oprel" : [],
                "parentesis1" : ['(', 'Expresion', ')'], "parentesis2" : [],"puntoycoma" : [] , "opsuma" : [], "opmult" : [],'#':[]},


############################### falta ##################################################
    'ListaSentecias_Prime' : {"si" : [], "sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "func" : [], "repetir" : [], "hasta" : [], "leer" : [],
                "mostrar" : [], "equal" : [], "id" : [], "num" : [], "oprel" : [],
                "parentesis1" : [], "parentesis2" : [],"puntoycoma" : [';', 'Sentencia'] , "opsuma" : [], "opmult" : [],'#':[]},
}

