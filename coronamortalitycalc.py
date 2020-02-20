number = int(input("known infected: "))
realmort = 608 / 14982
print('Projected Real Mortality rate:\n', realmort)  
realdeaths = number * realmort
print('Projected Real death count:\n' ,round(realdeaths, 2))
fakemort = 2012 / 75201
print('News Mortality rate 2/18:\n', fakemort)  
fakedeaths = number * fakemort
print('News death count 2/18:\n' ,round(fakedeaths, 2)) 
fakemort2 = 2122 / 75641
print('News Mortality rate 2/19:\n', fakemort2)  
fakedeaths2 = number * fakemort2
print('News death count 2/19:\n' ,round(fakedeaths2, 2)) 
combrate = realmort + fakemort + fakemort2
combdeath = realdeaths + fakedeaths + fakedeaths2
avrate = combrate / 3
avdeath = combdeath / 3
print('Running Averages:' ,'\nAverage Mortality Rate:', avrate ,'\nAverage of Deaths:', avdeath)
