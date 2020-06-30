import matplotlib.pyplot as plt

class Sketcher:
    def __init__(self):
        self.results = None
        self.vals = None
        
    def setPairs(self,vals,res):
        self.vals = self._clean(vals)
        self.results = self._clean(res)
        print(self.vals,self.results)

    def plot(self,xlabel,ylabel,title):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.plot(self.vals,self.results)
        plt.show()
    
    def plot_cons(self):
        plt.xlabel(input("X label: "))
        plt.ylabel(input("y label: "))
        plt.title(input("title: "))
        plt.plot(self.vals,self.results)
        plt.show()
        

    def _clean(self,string):
        string = string.replace(","," ").split()
        string = [i for i in string if i != " "]
        return [float(i) for i in string]
        