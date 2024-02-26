class Boar:

    fur = "коричневый"
    boar_name = "Кабанчик"
    fur_type = "гладкая"
 
    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def info(self):    
        fur = "коричневый"
        boar_name = "Кабанчик"
        fur_type = "гладкая"
        print("Цвет шерсти : ", fur, ". Имя кабана:", boar_name,". Шерсть кабана", fur_type)

my_boar = Boar()

my_boar.info()
