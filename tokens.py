class DFA : 

    def __init__(self,Q,Sigma,delta,q0,F,name) :
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as a dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states
        self.name = name
            
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F},\n\t{self.name})"
    
    def recognize_lexeme (self,w) :
        q = self.q0
    
        for symbol in w:
            if (q,symbol) in self.delta:
                q = self.delta[(q,symbol)] #manejamos las keys del dict como tuplas :)
            else:
                return False
        
        return q in self.F #devuelve boolean que dice si estan en los finales
    
si_sino = DFA(
        {0,1,2,3,4},
        {"s","i","n","o"},
        {(0,"s"):1,(1,"i"):2,(2,"n"):3,(3,"o"):4},
        0,
        {2,4},
        'si_sino'
)


entonces = DFA(
        {0,1,2,3,4,5,6,7,8},
        {"e","n","t","o","c","s"},
        {(0,"e"):1,(1,"n"):2,(2,"t"):3,(3,"o"):4,(4,"n"):5,(5,"c"):6,(6,"e"):7,(7,"s"):8},
        0,
        {8},
        'entonces'
)


finsi = DFA(
        {0,1,2,3,4,5},
        {"f","i","n","s"},
        {(0,"f"):1,(1,"i"):2,(2,"n"):3,(3,"s"):4,(4,"i"):5},
        0,
        {5},
        'finsi'
)


repetir = DFA(
        {0,1,2,3,4,5,6,7},
        {"r","e","p","t","i"},
        {(0,"r"):1,(1,"e"):2,(2,"p"):3,(3,"e"):4,(4,"t"):5,(5,"i"):6,(6,"r"):7},
        0,
        {7},
        'repetir'
)


hasta = DFA(
        {0,1,2,3,4,5},
        {"h","a","s","t"},
        {(0,"h"):1,(1,"a"):2,(2,"s"):3,(3,"t"):4,(4,"a"):5},
        0,
        {5},
        'hasta'
)


leer = DFA(
        {0,1,2,3,4},
        {"l","e","r"},
        {(0,"l"):1,(1,"e"):2,(2,"e"):3,(3,"r"):4},
        0,
        {4},
        'leer'
)


mostrar = DFA(
        {0,1,2,3,4,5,6,7},
        {"m","o","s","t","r","a"},
        {(0,"m"):1,(1,"o"):2,(2,"s"):3,(3,"t"):4,(4,"r"):5,(5,"a"):6,(6,"r"):7},
        0,
        {7},
        'mostrar'
)

numero = DFA(
    {0, 1},
    {chr(digit) for digit in range(10)},
    {(0,str(x)):1 for x in range(10)} | {(1,str(x)):1 for x in range(10)},
    0,
    {1},
    'numero'
)
var = DFA(
        {0,1},
        {chr(letter) for letter in range(128) if chr(letter).isalnum()},
        {(0, chr(letter)): 1 for letter in range(128) if chr(letter).isalpha()} | {(1, chr(letter)): 1 for letter in range(128) if chr(letter).isalnum()},
        0,
        {1},
        'var'
)

oprel = DFA(
        {0,1,2,3,4,5,6,7,8},
        {"<","=","!",">"},
        {(0,"!"):7,(0,'<'):1,(0,'='):3,(0,'>'):5,(1,'='):2,(3,'='):4,(5,'='):6,(7,'='):8},
        0,
        {1,2,4,5,6,8},
        'oprel'
)

func = DFA(
    {0,1,2,3,4},
    {"f","u","n","c"},
    {(0,"f"):1,(1,"u"):2,(2,"n"):3,(3,"c"):4},
    0,
    {4},
    'func'
)

finfunc = DFA(
     {0,1,2,3,4,5,6,7},
     {"f","i","u","n","c"},
     {(0,"f"):1,(1,"i"):2,(2,"n"):3,(3,"f"):4,(4,"u"):5,(5,"n"):6,(6,"c"):7},
     0,
     {7},
     'finfunc'
 )

parentesis = DFA(
    {0,1},
    {"(",")"},
    {(0,"("):1,(0,")"):1},
    0,
    {1},
    'parentesis'
)

equal = DFA(
    {0},
    {"="},
    {(0,"="):1},
    0,
    {1},
    'equal'
)

punto_coma = DFA(
    {0,1},
    {";"},
    {(0,";"):1},
    0,
    {1},
    'punto_coma'
)

#########################
# falta opsuma y opmult #
#########################

if numero.recognize_lexeme('123'):
    print('true')
else:
    print('false')


if var.recognize_lexeme("var123"):#true
    print('true')
else:
    print('false')
if var.recognize_lexeme("1var123"):#false
    print('true')
else:
    print('false')

# funcion lexer
def lexer(w):
    automatas = [si_sino, entonces, finsi, repetir, hasta, equal, leer, mostrar, func, finfunc, numero, parentesis, punto_coma, oprel, opsuma, opmult, var]
    lista = w.split()
    listlexema = []
    for p in lista:
        for a in automatas:
            if a.recognize_lexeme(p):
                listlexema.append((a.name,p))
                break
