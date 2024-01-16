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
        
    def updete_narx(self,n):
        self.narxi=self.narxi+n
        
    def __repr__(self):
        return self.nomi
            
            
m1=Maxsulot("Cola",200,12000)
m2=Maxsulot("Palto",500,900000)

class Dukon:
    def __init__(self,nomi,manzili,turi):
        self.nomi=nomi
        self.manzili=manzili
        self.turi=turi
        self.Maxsulotlar=[]
        
    def get_info(self):
        return f"{self.nomi} {self.manzili} {self.turi}" 

    def add_Maxsulotlar(self,M):
        self.Maxsulotlar.append(M)
        
    def get_Maxsulotlar(self):
        return self.Maxsulotlar
    
    def remove_maxsulot(self,maxsulot):
        if maxsulot in self.Maxsulotlar:
            self.Maxsulotlar.remove(maxsulot)

    
    
d1=Dukon("Sevinch","Urganch","Kiyim") 
d2=Dukon("IDEAL SARI","Urganch","Kompyuter dukon")   
   
