class Shahar:
    def __init__(self,tuman_nomi,huquqiy_holati):
        self.tuman_nomi=tuman_nomi
        self.huquqiy_holati=huquqiy_holati
        Shahar.soni+=1
        self.__id=Shahar.soni
        
        def get_info(self):
            return f"{self.tuman_nomi} {self.huquqiy_holati} "
            
    def get_id(self):
        return self.__id        
        
    def updete_holat(self,h):
        self.huquqiy_holati=self.huquqiy_holati+h
        
    def __repr__(self):
        return self.tuman_nomi
            
            
sh1=Shahar("Xiva","Yaxshi")
sh2=Shahar("Toshkent","Yaxshi")

class Viloyat:
    def __init__(self,nomi,yer_maydon,aholisi,respublika):
        self.nomi=nomi
        self.yer_maydon=yer_maydon
        self.aholisi=aholisi
        self.respublika=respublika
        self.Viloyatlar=[]
        
    def get_info(self):
        return f"{self.nomi} {self.yer_maydon} {self.aholisi} {self.respublika}" 

    def add_Viloyatlar(self,V):
        self.Viloyatlar.append(V)
        
    def get_Viloyatlar(self):
        return self.Viloyatlar
    
    def remove_viloyat(self,viloyat):
        if viloyat in self.Viloyatlar:
            self.Viloyatlar.remove(viloyat)
            
v1=Viloyat("Xorazm","6.1 ming km^2","1958.2 ming kishi","O'zbekiston") 
v2=Viloyat("Toshkent","15.3 ming km^2","3mln","O'zbekiston")           
            
