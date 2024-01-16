class Talaba:
    number=0
    def __init__(self,ism,familiya,guruh,shartnoma="Kontrakt"):
        self.ism=ism
        self.familiya=familiya
        self.guruh=guruh
        self.shartnoma=shartnoma
        Talaba.number+=1
        self.__id=Talaba.number
        
        def get_id(self):
            return  self.__id
    
        
    def malumot(self):
        full=f"Ma'lumot:{self.ism} {self.familiya} {self.guruh}"   
        return full  
    def guruh_yangi(self,qiymat):
        self.guruh=qiymat
        
        
a1=Talaba("Muxlisa","Rajabboyeva","941-22") 
a2=Talaba("Fotima","Nurmetova","941-22")
a3=Talaba("Nafosat","Rustambekova","941-22")

print(a1.ism())   
a1.guruh_yangi("942-22")        
print(a1.guruh)
