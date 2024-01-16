class Kompyuter:
    def __init__(self,nomi,xotirasi,protsessori,narxi):
        self.nomi=nomi
        self.xotirasi=xotirasi
        self.protsessori=protsessori
        self.narxi=narxi
        
    def get_info(self):
        return f"{self.nomi} {self.xotirasi} {self.narxi}"
        
    def updete_narx(self,n):
        self.narxi=self.narxi+n
        
    def __repr__(self):
        return self.nomi
            
            
obj1=Kompyuter("Tecno","512 GB","Intel Core i5",6000000)
obj2=Kompyuter("Ases","256 GB","Intel Core i5",5500000)

class Kompyuter_dokon:
    def __init__(self,nomi,manzili,telefon):
        self.nomi=nomi
        self.manzili=manzili
        self.telefon=telefon
        self.kompyuterlar=[]
        
    def get_info(self):
        return f"{self.nomi} {self.manzili} {self.telefon}" 

    def add_kompyuter(self,komp):
        self.kompyuterlar.append(komp)
        
    def get_kompyuter(self):
        return self.kompyuterlar
    
dokon=Kompyuter_dokon("IBM","Urganch 5 blok","+99891234444")    
            