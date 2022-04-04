class Trabajador:

    def __init__(self,nom ,cat , he, tar,pro):

         self.nombre = nom
         self.horas = he
         self.tardanza = tar
         self.categoria = cat
         self.profesion = pro
    def Nombre (self):
        n = ""
        
        if (self.nombre == 1):
           n= "ROBERTO CARLOS"
        elif(self.nombre == 2):
           n= "MARIA SALAZAR"
        elif(self.nombre ==3):
           n= "JUAN PEREZ"
        
        return n
    
    def Categoria(self):
        return self.categoria

    def Sueldo_basico (self):

        e=0
        if(self.categoria== "A"):
          e= 3000
        elif(self.categoria== "B"):
          e= 2500
        elif(self.categoria== "C"):
          e= 2000

        return e

    def Profesion(self):
       p = ""

       if(self.profesion == 1):
           p = "GERENTE"
       elif(self.profesion == 2):
           p = "ARQUITECTO"
       elif(self.profesion == 3):
           p = "ING.CIVIL"
       elif(self.profesion == 4):
           p = "RECURSOS HUMANOS"
       elif(self.profesion == 5):
           p = "SUPERVISOR DE OBRA"
       return p

    def Descuento(self):
        return round (self.Sueldo_basico()/240/60*self.tardanza)
    def Horas_extras(self):
        return round (self.Sueldo_basico()/240*self.horas)
    def Sueldo_neto(self):
        return round(self.Sueldo_basico()-self.Descuento()+self.Horas_extras())
    def DNI(self):
       e =""
       if(self.nombre==1):
           e= "76333687"
       elif(self.nombre==2):
           e= "84434432"
       elif(self.nombre==3):
           e= "45354332"

       return e