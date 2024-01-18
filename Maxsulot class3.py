class Maxsulot:
    def __init__(self,nomi,soni,narxi,mamlakat):
        self.nomi=nomi
        self.soni=soni
        self.narxi=narxi
        self.mamlakat=mamlakat
        Maxsulot.soni+=1
        self.__id=Maxsulot.soni
        
        def get_info(self):
            return f"{self.nomi} {self.soni} {self.narxi} {self.mamlakat}"
            
    def get_id(self):
        return self.__id        
        
    def set_narx(self,x):
        self.narxi=self.narxi+x
        
    def __repr__(self):
        return self.nomi
            
            
m1=Maxsulot("Cola",200,12000)
m2=Maxsulot("Palto",500,900000)