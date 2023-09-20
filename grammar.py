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
    'Factor',
    'Termino',
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
}

