class DFA : 

    def __init__(self,Q,Sigma,delta,q0,F) :
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as a dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states
            
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    

    def recognize_lexeme (self,w) :
        q = self.q0
    
        for symbol in w:
            if (q,symbol) in self.delta:
                q = self.delta[(q,symbol)] #manejamos las keys del dict como tuplas :)
            else:
                return "Trampa"
        
        if q in self.F:#devuelve boolean que dice si estan en los finales
                return "Final"
        else:
                return "No final"
    

sino = DFA(
        {0,1,2,3,4},
        {"s","i","n","o"},
        {(0,"s"):1,(1,"i"):2,(2,"n"):3,(3,"o"):4},
        0,
        {4}
)

si = DFA(
        {0,1,},
        {"s","i"},
        {(0,"s"):1,(1,"i"):2},
        0,
        {2}
)

entonces = DFA(
        {0,1,2,3,4,5,6,7,8},
        {"e","n","t","o","c","s"},
        {(0,"e"):1,(1,"n"):2,(2,"t"):3,(3,"o"):4,(4,"n"):5,(5,"c"):6,(6,"e"):7,(7,"s"):8},
        0,
        {8}
)

finsi = DFA(
        {0,1,2,3,4,5},
        {"f","i","n","s"},
        {(0,"f"):1,(1,"i"):2,(2,"n"):3,(3,"s"):4,(4,"i"):5},
        0,
        {5}
)

repetir = DFA(
        {0,1,2,3,4,5,6,7},
        {"r","e","p","t","i"},
        {(0,"r"):1,(1,"e"):2,(2,"p"):3,(3,"e"):4,(4,"t"):5,(5,"i"):6,(6,"r"):7},
        0,
        {7}
)

hasta = DFA(
        {0,1,2,3,4,5},
        {"h","a","s","t"},
        {(0,"h"):1,(1,"a"):2,(2,"s"):3,(3,"t"):4,(4,"a"):5},
        0,
        {5}
)

leer = DFA(
        {0,1,2,3,4},
        {"l","e","r"},
        {(0,"l"):1,(1,"e"):2,(2,"e"):3,(3,"r"):4},
        0,
        {4}
)

mostrar = DFA(
        {0,1,2,3,4,5,6,7},
        {"m","o","s","t","r","a"},
        {(0,"m"):1,(1,"o"):2,(2,"s"):3,(3,"t"):4,(4,"r"):5,(5,"a"):6,(6,"r"):7},
        0,
        {7}
)

numero = DFA(
        {0, 1},
        {chr(digit) for digit in range(10)},
        {(0,str(x)):1 for x in range(10)} | {(1,str(x)):1 for x in range(10)},
        0,
        {1}
)

var = DFA(
        {0,1},
        {chr(letter) for letter in range(128) if chr(letter).isalnum()},
        {(0, chr(letter)): 1 for letter in range(128) if chr(letter).isalpha()} | {(1, chr(letter)): 1 for letter in range(128) if chr(letter).isalnum()},
        0,
        {1}
)

oprel = DFA(
        {0,1,2,3,4,5,6,7,8},
        {"<","=","!",">"},
        {(0,"!"):7,(0,'<'):1,(0,'='):3,(0,'>'):5,(1,'='):2,(3,'='):4,(5,'='):6,(7,'='):8},
        0,
        {1,2,4,5,6,8}
)

func = DFA(
        {0,1,2,3,4},
        {"f","u","n","c"},
        {(0,"f"):1,(1,"u"):2,(2,"n"):3,(3,"c"):4},
        0,
        {4}
)

finfunc = DFA(
        {0,1,2,3,4,5,6,7},
        {"f","i","u","n","c"},
        {(0,"f"):1,(1,"i"):2,(2,"n"):3,(3,"f"):4,(4,"u"):5,(5,"n"):6,(6,"c"):7},
        0,
        {7}
 )

parentesisApertura = DFA(
        {0,1},
        {"("},
        {(0,"("):1},
        0,
        {1}
)

parentesisCerrado= DFA(
        {0,1},
        {"(",")"},
        {(0,")"):1},
        0,
        {1}
)

equal = DFA(
        {0,1,2,3,4,5},
        {"e","q","u","a","l"},
        {(0,"e"):1,(1,"q"):2,(2,"u"):3,(3,"a"):4,(4,"l"):5},
        0,
        {5}
)

punto_coma = DFA(
        {0,1},
        {";"},
        {(0,";"):1},
        0,
        {1}
)

opsuma = DFA(
        {0,1},
        {"+","-"},
        {(0,"+"):1,(0,"-"):1},
        0,
        {1}
)

opmult = DFA(
        {0,1},
        {"*","/"},
        {(0,"*"):1,(0,"/"):1},
        0,
        {1}
)


