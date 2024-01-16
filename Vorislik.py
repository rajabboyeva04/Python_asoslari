# Vorislik va polimorfizm
class Dukon:
    def __init__(self,nomi,manzili,turi,telefoni):
        self.nomi=nomi
        self.manzili=manzili
        self.turi=turi
        self.telefoni=telefoni
        self.tovarlar=[]
        
    def get_info(self) :
        return f"{self.nomi} {self.manzili} {self.turi} {self.telefoni}"
    
    def add_tovar(self,new):
        self.tovarlar.append(new)
    
    def get_tovarlar(self):
        return self.tovarlar
    
    def __repr__(self):
        return self.nomi
    
class Gul_dukon(Dukon):
    def __init__(self,nomi,manzili,turi,telefoni,gullar_soni):
        super.__init__(nomi,manzili,turi,telefoni)
        self.gullar_soni=gullar_soni
    
    def get_info(self):
        full=super().get_info()
        full+=self.gullar_soni
        return full 

obj1=Gul_dukon("Maftuna","Urganch","Gullar","+998933491141")    
            