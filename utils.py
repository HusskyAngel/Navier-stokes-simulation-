
class Utils():
    @staticmethod
    def getX(punto:str):
       aux=punto.split(',') 
       return int(aux[0])
        
    @staticmethod
    def getY(punto:str):
       aux=punto.split(',') 
       return int(aux[1])

    @staticmethod
    def transform(x:int,y:int,y_max:int):
       return (x,y_max-y)


