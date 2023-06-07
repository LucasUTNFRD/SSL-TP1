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
        while w!="" :
            q = self.delta[(q,w[0])]
            w = w[1:]
        if q in self.F:
            return True
        else:
            return False

D0 = DFA(
        {0,1,2,3,4,5,6,7,8},
        {"<","=","!",">"},
        {(0,"<"):1,(0,"="):5,(0,">"):6,(1,"="):2,(0,"!"):9,(1," "):4,(6,"="):7,(6," "):8,(9,"="):10},
        0,
        {2,3,4,5,7,8,10}
        )
print(D0.run("!="))
