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


    def __repr__(self):
        return self.nomi
         
    def __call__(self,komp):
        self.kompyuterlar.append(komp)
        
    def __getitem__(self,index):
        return self.kompyuterlar[index]
        
    def get_kompyuter(self):
        return self.kompyuterlar
    
dokon=Kompyuter_dokon("IBM","Urganch 5 blok","+99891234444")    
dokon=Kompyuter_dokon("Ideal Sari","Urganch ","+998973331221")            







