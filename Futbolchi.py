class Futbolchi:
    def __init__(self,ismi,yoshi,kim_bolib_oynaydi,gollar_soni):
        self.ismi=ismi
        self.yoshi=yoshi
        self.kim_bolib_oynaydi=kim_bolib_oynaydi
        self.gollar_soni=gollar_soni
        Futbolchi.gollar_soni+=1
        self.__id=Futbolchi.gollar_soni
        
        
    def get_info(self):
        return f"{self.ismi} {self.yoshi} {self.kim_bolib_oynaydi} {self.gollar_soni}"
        
    def updete_gollar(self,g):
        self.gollar_soni=self.gollar_soni+g
        
    def __repr__(self):
        return self.ismi
            
            
f1=Futbolchi("Ranoldo",38,"Hujumchi",757)
f2=Futbolchi("Messi",36,"Hujumchi",671)

class Jamoa:
    def __init__(self,nomi,galaba_soni,maglubiyat_soni):
        self.nomi=nomi
        self.galaba_soni=galaba_soni
        self.maglubiyat_soni=maglubiyat_soni
        self.Futbolchilar=[]
        
    def get_info(self):
        return f"{self.nomi} {self.galaba_soni} {self.maglubiyat_soni} " 

    def add_Futbolchilar(self,F):
        self.Futbolchilar.append(F)
        
    def get_Futbolchilar(self):
        return self.Futbolchilar
    
    def remove_futbolchi(self,futbolchi):
        if futbolchi in self.Futbolchilar:
            self.Futbolchilar.remove(futbolchi)
            
j1=Jamoa("Real Madrid",95,2)            
j2=Jamoa("Barselona",91,3)            
            
            