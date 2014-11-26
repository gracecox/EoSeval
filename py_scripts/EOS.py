from scipy.optimize import curve_fit

class EOS():
    
    def __init__(self, function):
        
        self.function = function
        self.parameters = None
    
    def fit(self, Pdata, Vdata, initparams):   
        "Function to fit EoS functions to data"
        popt, pcov = curve_fit(func, Pdata, Vdata, initparams)

        self.optparams = popt
        self.cov = pcov
        
         
    def evaluate(self, V):
        
        if len(self.optparams) == 1:
            P = self.function(V, self.optparams[0])
            
        elif len(self.optparams) == 2:
            P = self.function(V, self.optparams[0], self.optparams[1])

        elif len(self.optparams) == 3:
            P = self.function(V, self.optparams[0], self.optparams[1],self.optparams[2])
        else:
            P = 0
            print "ERROR BROKEN!"

        return P

        
    def evaluate_list(self, V):
        
        P=[]
        
        for volume in V:
            
            P.append(self.evaluate(volume))
        
        return P
        
        