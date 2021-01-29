import math


#Calcul de l'IPTCC en fonction de la température (en Celsius) et l'humidité relative (en %). Calcul développé par Predict Services
#Contact : Twitter : @covid_stat
def IPTCC_calculation(Temperature, RelativeHumidity):
    AbsoluteHumidity = (6.112 * math.exp((17.67*Temperature)/(Temperature + 243.5)) * RelativeHumidity * 2.1674 )  / (273.15 + Temperature)
    IPTCC = 100 * math.exp(-0.5 * (      (((Temperature - 7.5)*(Temperature-7.5))/196)  + (((RelativeHumidity - 75)*(RelativeHumidity - 75))/625) + (((AbsoluteHumidity-6)*(AbsoluteHumidity-6))/2.89) ))
    return IPTCC
    
# Test afin de vérifier que le comportement de la fonction est le même que ce qu'on peut constater graphiquement.    
print("Humidité fixe")
print(IPTCC_calculation(-5, 75))
print(IPTCC_calculation(273, 75))
print(IPTCC_calculation(5, 75))
print(IPTCC_calculation(8, 75))
print(IPTCC_calculation(10, 75))
print(IPTCC_calculation(15, 75))
print(IPTCC_calculation(20, 75))

print("Température fixe")
print(IPTCC_calculation(7, 100))
print(IPTCC_calculation(7, 80))
print(IPTCC_calculation(7, 75))
print(IPTCC_calculation(7, 65))
print(IPTCC_calculation(7, 55))
print(IPTCC_calculation(7, 40))
print(IPTCC_calculation(7, 30))
