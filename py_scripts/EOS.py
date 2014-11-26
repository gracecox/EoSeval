class EOS():
    
    def __init__(self, function):
        
        self.function = function
        self.parameters = None
    
    def fit(self, Pdata, Vdata):
        pass
        
        #Put some fitting stuff in here
        
        #self.parameters = define these here after fit
        
    def evaluate(self, V):
        
        return self.function(V, self.parameters)
        
    def evaluate_list(self, V):
        
        P=[]
        
        for volume in V:
            
            P.append(self.function(volume, self.parameters))
        
        

