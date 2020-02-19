number = int(input("known infected: "))
realmort = 608 / 14982
print('Real Mortality rate', realmort)  
realdeaths = number * realmort
print('real death count' ,round(realdeaths, 2))
fakemort = 2012 / 75201
print('Fake Mortality rate', fakemort)  
fakedeaths = number * fakemort
print('fake death count' ,round(fakedeaths, 2)) 
