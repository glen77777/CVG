number = int(input("known infected: "))
realmort = 608 / 14982
print('Projected Real Mortality rate', realmort)  
realdeaths = number * realmort
print('Projected Real death count' ,round(realdeaths, 2))
fakemort = 2012 / 75201
print('News Mortality rate 2/18', fakemort)  
fakedeaths = number * fakemort
print('News death count 2/18' ,round(fakedeaths, 2)) 
fakemort2 = 2122 / 75641
print('News Mortality rate 2/19', fakemort2)  
fakedeaths2 = number * fakemort2
print('News death count 2/19' ,round(fakedeaths2, 2)) 
