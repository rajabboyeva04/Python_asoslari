class Avtosalon:
    def __init__(self,nomi,soni,turi,narxi):
        self.nomi=nomi
        self.soni=soni
        self.turi=turi
        self.narxi=narxi
        
    def get_info(self):
        return f"{self.nomi} {self.soni} {self.narxi} {self.turi}"
        
    def updete_narx(self,n):
        self.narxi=self.narxi+n
        
    
            
a1=Avtosalon("Asaka",900,"Jentra","170 mln")
a2=Avtosalon("Hyundai",1000,"Malibu","250mln")

class Avto:
    def __init__(self,nomi,manzili,xizmat_korsatish):
        self.nomi=nomi
        self.manzili=manzili
        self.xizmat_korsatish=xizmat_korsatish
        self.avtomobillar=[]
        
    def get_info(self):
        return f"{self.nomi} {self.manzili} {self.xizmat_korsatish}" 


    def __repr__(self):
        return self.nomi
         
    def __call__(self,avt):
        self.avtomobillar.append(avt)
        
    def __getitem__(self,index):
        return self.avtomobillar[index]
        
    def get_avtomobil(self):
        return self.avtomobillar
    
d1=Avto("Avtomoyka","Urganch","Avtomobil yuvish")    
d2=Avto("Zapravka","Xiva","Moy yangilash")            






