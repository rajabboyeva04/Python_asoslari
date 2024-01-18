class Ishchi:
    def __init__(self,ism,firma_raqam,staj):
        self.ism=ism
        self.firma_raqam=firma_raqam
        self.staj=staj
        
        
    def get_info(self):
        return f"{self.ism} {self.firma_raqam} {self.staj}"
        
    def updete_staji(self,s):
        self.staj=self.staj+s
        
    def __repr__(self):
        return self.ism
            
            
i1=Ishchi("Sarvar",87654322345,2)
i2=Ishchi("Komiljon",434569002,3)