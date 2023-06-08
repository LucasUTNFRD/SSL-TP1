class DFA : 

    def __init__(self,Q,Sigma,delta,q0,F) :
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as a dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states 
            
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    
    def run (self,w) :
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
        {2,4}
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
    {0,1},
    {"0","1","2","3","4","5","6","7","8","9"},
    {(0,"0"):1,(0,"1"):1,(0,"2"):1,(0,"3"):1,(0,"4"):1,(0,"5"):1,(0,"6"):1,(0,"7"):1,(0,"8"):1,(0,"9"):1,
     (1,"0"):1,(1,"1"):1,(1,"2"):1,(1,"3"):1,(1,"4"):1,(1,"5"):1,(1,"6"):1,(1,"7"):1,(1,"8"):1,(1,"9"):1},
     0,
     {1}
)

if numero.run("98"):
    print("valid")
else :
    print("cagada")