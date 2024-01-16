class Shaxs:
    number=0
    def __init__(self,ism,familiya,ish_joyi,JSHSHIR,passport="AD0463725"):
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        self.passport=passport
        self.JSHSHIR=JSHSHIR
        Shaxs.number+=1
        self.__id=Shaxs.number
        
    def get_id(self):
        return self.__id        
        
    def malumot(self):
        full=f"Ma'lumot:{self.ism} {self.familiya} {self.ish_joyi}"   
        return full 
    
    def ish_joyi_yangi(self,qiymat):
        self.ish_joyi=qiymat
        
        
a1=Shaxs("Muxlisa","Rajabboyeva","Ishsz") 
a2=Shaxs("Fotima","Nurmetova","Ishsz")
a3=Shaxs("Nafosat","Rustambekova","Ishsz")

print(a2.ism())   
a2.ish_joyi_yangi("Universitet")        
print(a2.ish_joyi)
