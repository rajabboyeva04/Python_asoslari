class Ishchi:
    def __init__(self,ismi,guruh_raqami,staji):
        self.ismi=ismi
        self.guruh_raqami=guruh_raqami
        self.staji=staji
        
    def get_info(self):
        return f"{self.ismi} {self.guruh_raqami} {self.staji}"
        
    def updete_malaka(self,m):
        self.staji=self.staji+m
        
    def __repr__(self):
        return self.ismi
            
            
i1=Ishchi("Sarvar",6,2)
i2=Ishchi("Komiljon",4,3)

class Korxona:
    def __init__(self,nomi,firma_raqami,manzili):
        self.nomi=nomi
        self.firma_raqami=firma_raqami
        self.manzili=manzili
        self.Ishchilar=[]
        
    def get_info(self):
        return f"{self.nomi} {self.firma_raqami} {self.manzili} " 

    def add_Ishchilar(self,I):
        self.Ishchilar.append(I)
        
    def get_Ishchilar(self):
        return self.Ishchilar
    
    def remove_ishchi(self,ishchi):
        if ishchi in self.Ishchilar:
            self.Ishchilar.remove(ishchi)

    
    
k1=Korxona("Avtosalon",897899900,"Xorazm viloyati") 
k2=Korxona("Neft zavodi",12345668,"Navoiy viloyati")   
   



