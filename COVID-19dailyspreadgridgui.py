import matplotlib.pyplot as plt
from tkinter import *
window = Tk()
window.title('COVID-19 Spread')
label = Label(window, text = 'Graphical representation of rate of spread by day')
label.grid(row =1)
day1 = jan21 = 329
day2 = jan22 = 561
day3 = jan23 = 672
day4 = jan24 = 672 + 174 + 3 + 4 + 21 + 1 + 2 + 16 + 6 + 105 + 7 + 4 + 18 + 3 + 15 + 2 + 1 + 1 + 4 + 6 + 1 + 3 + 3 + 2 + 1 + 2 + 5 + 1 + 2 + 2 + 1 + 1 + 1 + 3 + 10 + 3 + 2 + 11 + 180 + 5 + 8 + 1
day5 = jan25 = jan24 + 175 + 13 + 1 + 6 + 9 + 1 + 1 + 6 + 19 + 25 + 23 + 24 + 30 + 1 + 19 + 5 + 9 + 13 + 3 + 3 + 6 + 1 + 1 + 8 + 10 + 1 + 3 + 1 + 1 + 1 + 1 + 1 + 5 + 6 + 1 + 31 + 10 + 10 + 18 + 1 + 1 + 3 + 292 + 7
day6 = jan26 = jan25 + 51 + 12 + 181 + 1 + 26 + 21 + 13 + 20 + 6 + 42 + 5 + 5 + 3 + 18 + 16 + 3 + 3 + 3 + 3 + 3 + 7 + 11 + 7 + 1 + 1 + 1 + 1 + 2 + 3 + 13 + 1 + 6 + 1 + 9 + 1 + 5 + 1 + 3 + 2 + 5 + 3 + 1 + 1 + 12 + 2 + 1 + 1 + 4 + 371 + 302  
day7 = jan27 = jan26 + 10 + 4 + 13 + 45 + 31 + 17 + 14 + 10 + 35 + 35 + 5 + 3 + 2 + 7 + 1 + 24 + 5 + 25 + 2 + 1 + 1 + 13 + 1 + 9 + 3 + 21 + 12 + 1 + 4 + 4 + 1 + 3 + 7 + 5 + 2 + 1 + 1 + 2 + 1 + 3 + 8 + 5 + 7 + 1 + 24 + 1
day8 = jan28 = jan27 + 13 + 6 + 40 + 12 + 1291 + 2 + 23 + 36 + 22 + 21 + 9 + 5 + 5 + 45 + 15 + 37 + 4 + 2 + 2 + 7 + 43 + 1 + 3 + 14 + 6 + 18 + 2 + 11 + 2 + 8 + 11 + 2 + 2 + 19 + 4 + 7 + 37 + 1 + 7 + 3 + 840 + 1 + 1 + 1 + 3 + 1
day9 = jan29 = jan28 + 14 + 2 + 7 + 469 + 38 + 3 + 26 + 29 + 46 + 123 + 18 + 78 + 15 + 1 + 7 + 5 + 34 + 3 + 2 + 15 + 1 + 1 + 1 + 10 + 7 + 1 + 4 + 11 + 2 + 1 + 16 + 9 + 2 + 31 + 1 + 4 + 2 + 3 + 1 + 9 + 2 + 1 + 1032 + 53 + 8 + 18 + 536
day10 = jan30 = jan29 + 3 + 5 + 17 + 20 + 34 + 48 + 15 + 72 + 3 + 30 + 1 + 5 + 56 + 132 + 39 + 6 + 3 + 2 + 15 + 17 + 1 + 7 + 2 + 3 + 5 + 2 + 1 + 1 + 11 + 13 + 1 + 1 + 17 + 43 + 2 + 3 + 1 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 3 + 1 + 6 + 1 + 317 + 7 + 3 + 2 + 1 + 1 + 2 + 1 + 903 + 4 + 24 + 622
day11 = feb1 = jan30 + 1 + 4 + 9 + 16 + 17 + 36 + 78 + 37 + 20 + 39 + 74 + 3 + 109 + 39 + 15 + 3 + 55 + 4 + 3 + 1 + 24 + 2 + 11 + 4 + 7 + 19 + 3 + 4 + 6 + 3 + 5 + 7 + 43 + 14 + 2 + 5 + 1 + 3 + 2 + 1 + 1 + 1 + 2 + 1 + 12 + 6 + 1 + 1 + 1 + 1347 + 1 + 27 + 8
day12 = feb2 = feb1 + 11 + 8 + 9  + 71 + 3 + 1 + 1 + 1 + 3 + 24 + 19 + 34 + 43 + 69 + 47 + 62 + 15 + 2 + 74 + 8 + 2 + 1 + 7 + 5 + 15 + 15 + 15 + 4 + 6 + 6 + 28 + 8 + 5 + 5 + 13 + 2 + 6 + 1 + 1 + 11 + 1 + 2103 + 10 + 25 + 593 + 11
day13 = feb3 = feb2 + 16 + 9 + 8 + 2 + 68 + 73 + 23 + 8 + 35 + 16 + 3 + 63 + 59 + 23 + 51 + 58 + 2 + 3 + 3 + 12 + 6 + 7 + 20 + 1 + 2 + 3 + 10 + 4 + 1 + 13 + 12 + 5 + 42 + 24 + 1 + 4 + 4 + 1 + 1 + 1 + 2345 + 8 + 25 + 750 + 5 + 13
day14 = feb4 = feb3 + 11 + 12 + 72 + 37 + 10 + 109 + 7 + 11 + 37 + 28 + 5 + 105 + 2 + 85 + 72 + 72 + 3 + 14 + 1 + 1 + 1 + 1 + 1 + 6 + 15 + 1 + 5 + 11 + 5 + 1 + 3 + 2 + 7 + 1 + 16 + 1 + 2 + 6 + 2 + 6 + 1 + 16 + 1 + 1 + 4 + 2 + 1 + 1 + 1 + 1 + 1 + 3156 + 10 + 675 + 3 + 7 + 22 + 14
day15 = feb5 = feb4 + 11 + 9 + 12 + 2 + 19 + 23 + 89 + 50 + 68 + 2 + 33 + 6 + 35 + 66 + 72 + 7 + 57 + 3 + 11 + 11 + 23 + 2 + 1 + 25 + 10 + 3 + 9 + 2 + 1 + 2 + 4 + 7 + 10 + 1 + 1 + 1 + 1 + 1 + 1 + 10 + 2987 + 4 + 660 + 4 + 9 + 13 + 11 + 10
day16 = feb6 = feb5 + 22 + 5 + 36 + 18 + 87 + 5 + 20 + 61 + 4 + 50 + 32 + 37 + 6 + 1 + 59 + 52 + 74 + 6 + 4 + 8 + 21 + 10 + 2 + 1 + 2 + 2 + 2 + 5 + 26 + 11 + 1 + 1 + 9 + 3 + 4 + 2 + 1 + 1 + 3 + 2 + 2 + 3 + 1 + 5 + 6 + 1 + 2447 + 2 + 1 + 2 + 11 + 12
day17 = feb7 = feb6 + 625 + 32 + 4 + 6 + 14 + 1 + 23 + 63 + 41 + 74 + 35 + 11 + 52 + 61 + 61 + 48 + 2 + 3 + 3 + 3 + 4 + 11 + 23 + 9 + 6 + 8 + 50 + 1 + 7 + 1 + 3 + 1 + 16 + 4 + 1 + 1 + 4 + 1 + 1 + 3 + 4 + 1 + 8 + 1 + 2841 + 11 + 2 + 4 + 2
day18 = feb8 = feb7 + 498 + 24 + 11 + 4 + 3 + 21 + 19 + 31 + 31 + 68 + 18 + 67 + 42 + 37 + 8 + 41 + 9 + 2 + 11 + 7 + 18 + 2 + 15 + 3 + 1 + 1 + 7 + 5 + 4 + 9 + 2 + 20 + 5 + 1 + 1 + 8 + 7 + 12 + 2147 + 18 + 6
day19 = feb9 = feb8 + 441 + 11 + 2 + 9 + 12 + 26 + 23 + 53 + 35 + 29 + 7 + 27 + 1 + 46 + 3 + 42 + 4 + 25 + 19 + 2 + 13 + 1 + 11 + 11 + 1 + 2 + 1 + 1 + 6 + 1 + 9 + 2 + 1 + 1 + 1 + 3 + 7 + 3 + 2531 + 419
day20 = feb10 = feb9 + 1 + 65 + 4 + 2 + 2 + 4 + 1 + 2097
day21 = feb11 = feb10 + 370 + 1 + 1 + 2 + 2 + 7 + 2 + 1 + 1638 + 39
day22 = feb12 = feb11 + 377 + 1 + 3 + 1 + 1 + 14840
day23 = feb13 = feb12 + 1 + 44 + 1 + 312 + 1 + 1 + 1 + 8 + 1 + 1 + 3 + 4823
day24 = feb14 = feb13 + 1 + 267 + 1 + 4 + 3 + 3 + 2 + 9 + 1 + 1 + 1 + 1 + 1 + 2420 + 5 + 7 + 8
day25 = feb15 = feb14 + 193 + 33 + 28 + 7 + 13 + 16 + 13 + 11 + 7 + 1 + 1 + 3 + 2 + 1 + 2 + 67 + 8 + 1 + 1 + 2 + 1 + 5 + 1 + 1 + 1843 + 6
day26 = feb16 = feb15 + 5 + 19 + 11 + 20 + 100 + 1 + 1 + 2 + 22 + 5 + 3 + 12 + 12 + 70 + 13 + 5 + 3 + 2 + 1 + 5 + 1 + 2 + 3 + 1 + 1933 + 4 + 3 + 12
day27 = feb17 = feb16 + 4 + 15 + 14 + 11 + 1 + 2 + 34 + 9 + 1 + 5 + 4 + 6 + 1 + 1 + 1 + 1 + 14 + 4 + 85 + 2 + 3 + 1 + 2 + 1 + 1 + 1807 + 1 + 77
day28 = feb18 = feb17 + 9 + 1 + 1 + 3 + 6 + 1 + 11 + 3 + 2 + 13 + 7 + 1 + 6 + 2 + 1 + 1 + 88 + 4 + 3 + 1 + 3 + 1 + 1 + 1 + 1 + 1 + 1693 + 2 + 4
day29 = feb19 = feb18 + 47 + 1 + 6 + 2 + 5 + 1 + 1 + 6 + 1 + 2 + 4 + 6 + 2 + 15 + 3 + 1 + 1 + 1 + 1 + 2 + 2 + 1 + 1 + 4 + 1 + 1 + 79 + 1 + 2 + 1 + 3 + 3 + 1 + 1 + 1 + 2 + 2 + 2 + 2 + 349 + 5
day30 = feb20 = feb19 + 24 + 1 + 4 + 2 + 2 + 1 + 1 + 5 + 2 + 6 + 6 + 2 + 1 + 1 + 1 + 3 + 5 + 2 + 1 + 1 + 1 + 1 + 2 + 5 + 17 + 1 + 3 + 1 + 1 + 1 + 1 + 1 + 13 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 411 + 1 + 4 + 1 + 4 + 2
day31 = feb21 = feb20 + 1 + 45 + 1 + 477 + 1 + 2 + 28 + 1 + 1 + 7 + 5 + 3 + 1 + 1 + 1 + 3 + 202 + 1 + 3 + 2 + 48 + 1 + 1 + 2 + 13 + 1 + 1 + 1 + 1 + 1 + 3 + 3 + 1 + 2 + 1 + 1 + 2 + 2 + 426 + 8 + 2 + 18 + 1 + 1 + 1 + 1 + 1 + 2 + 1
day32 = feb22 = feb21 + 366 + 31 + 1 + 142 + 1 + 2 + 1 + 1 + 87 + 10 + 1 + 9 + 1 + 4 + 1 + 1 + 1 + 4 + 3 + 2 + 33 + 1 + 1 + 1 + 7 + 1 + 16 + 630 + 3
day33 = feb23 = feb22 + 25 + 95 + 18 + 1 + 2 + 1 + 46 + 1 + 4 + 34 + 2 + 15 + 8 + 1 + 16 + 1 + 57 + 1 + 4 + 1 + 23 + 1 + 1
day34 = feb24 = feb23 + 161 + 409 + 1 + 3 + 1 + 1 + 70 + 4 + 38 + 1 + 7 + 2 + 1 + 19 + 1 + 7 + 3 + 4 + 2 + 1 + 12 + 1 + 18 + 5 + 14 + 1 + 2 + 1 + 1
day35 = feb25 = feb24 + 499 + 9 + 60 + 2 + 1 + 1 + 2 + 1 + 1 + 2 + 3 + 6 + 1 + 84 + 1 + 14 + 4 + 34 + 28 + 1 + 2 + 9 + 1 + 1 + 1 + 2 + 4 + 1 + 6 + 1 + 39 + 1 + 4 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 2 + 10
day36 = feb26 = feb25 + 169 + 401 + 5 + 1 + 3 + 1 + 1 + 3 + 1 + 1 + 115 + 1 + 32 + 3 + 6 + 44 + 1 + 4 + 1 + 1 + 7 + 1 + 1 + 14 + 17 + 1 + 1 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 27 + 3 + 1 + 7 + 1 + 1 + 54 + 7 + 1 + 17
day37 = feb27 = feb26 + 334 + 433 + 1 + 1 + 1 + 1 + 1 + 17 + 3 + 1 + 1 + 171 + 3 + 13 + 2 + 2 + 1 + 104 + 1 + 2 + 2 + 75 + 1 + 3 + 1 + 1 + 2 + 1 + 1 + 6 + 1 + 1 + 127 + 14 + 4 + 5 + 20 + 1 + 6 + 3 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 7 + 1 + 2
day38 = feb28 = feb27 + 327 + 1 + 256 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 1 + 2 + 2 + 315 + 2 + 2 + 12 + 1 + 1 + 1 + 1 + 1 + 2 + 1 + 143 + 1 + 1 + 6 + 3 + 2 + 1 + 2 + 1 + 233 + 1 + 1 + 2 + 2 + 1 + 1 + 16 + 2 + 4 + 1 + 1 + 1 + 2 + 1 + 1 + 7 + 3 + 2 + 1 + 1 + 1 + 1 + 1 
day39 = feb29 = feb28 + 1 + 423 + 4 + 594 + 1 + 1 + 1 + 1 + 1 + 1 + 5 + 1 + 219 + 8 + 4 + 205 + 1 + 3 + 3 + 1 + 1 + 1 + 1 + 1 + 2 + 4 + 16 + 3 + 2 + 1 + 3 + 1 + 2 + 5 + 8 + 10 + 239 + 3 + 1 + 2 + 27 + 1 + 3 + 1 + 3 + 1 + 1 + 1 + 570 + 3
itday1 = ijan30 = 2
itday2 = ifeb6 = itday1 + 1
itday3 = ifeb20 = itday2 + 1
itday4 = ifeb21 = itday3 + 2 + 3 + 8 + 2 + 1
itday5 = ifeb22 = itday4 + 1 + 33 + 1 + 7 + 1 + 16
itday6 = ifeb23 = itday5 + 34 + 16 + 1 + 23
itday7 = ifeb24 = itday6 + 1 + 38 + 7 + 19 + 3 + 4 + 5 + 1
itday8 = ifeb25 = itday7 + 2 + 14 + 38 + 39 + 2 + 2
itday9 = ifeb26 = itday8 + 32 + 17 + 27 + 54
itday10 = ifeb27 = itday9 + 75 + 127
itday11 = ifeb28 = itday10 + 233 + 1
itday12 = ifeb29 = itday11 + 239
it1i = itday2 / itday1
it2i = itday3 / itday2
it3i = itday4 / itday3
it4i = itday5 / itday4
it5i = itday6 / itday5
it6i = itday7 / itday6
it7i = itday8 / itday7
it8i = itday9 / itday8
it9i = itday10 / itday9
it10i = itday11 / itday10
it11i = itday12 / itday11
itav = (it1i + it2i + it3i + it4i + it5i + it6i + it7i + it8i + it9i + it10i + it11i)/11
it1ia = (it1i + itav)/2
it2ia = (it2i + itav)/2
it3ia = (it3i + itav)/2
it4ia = (it4i + itav)/2
it5ia = (it5i + itav)/2
it6ia = (it6i + itav)/2
it7ia = (it7i + itav)/2
it8ia = (it8i + itav)/2
it9ia = (it9i + itav)/2
it10ia = (it10i + itav)/2
it11ia = (it11i + itav)/2
korday1 = kjan24 = 1
korday2 = kjan26 = korday1 + 1
korday3 = kjan27 = korday2 + 1
korday4 = kjan30 = korday3 + 2
korday5 = kjan31 = korday4 + 1 + 4
korday6 = kfeb1 = korday5 + 1
korday7 = kfeb2 = korday6 + 3
korday8 = kfeb4 = korday7 + 1
korday9 = kfeb5 = korday8 + 2 + 1 + 4
korday10 = kfeb7 = korday9 + 1
korday11 = kfeb9 = korday10 + 1 + 2
korday12 = kfeb11 = korday11 + 1
korday13 = kfeb16 = korday12 + 1
korday14 = kfeb17 = korday13 + 1
korday15 = kfeb18 = korday14 + 1
korday16 = kfeb19 = korday15 + 15 + 1 + 4 + 2 + 5
korday17 = kfeb20 = korday16 + 24 + 5 + 17 + 1 + 2 + 1 + 4
korday18 = kfeb21 = korday17 + 45 + 48 + 1 + 1 + 2
korday19 = kfeb22 = korday18 + 142 + 87 + 3
korday20 = kfeb23 = korday19 + 25 + 95 + 46
korday21 = kfeb24 = korday20 + 161 + 70
korday22 = kfeb25 = korday21 + 60 + 84
korday23 = kfeb26 = korday22 + 169 + 115
korday24 = kfeb27 = korday23 + 334 + 171
korday25 = kfeb28 = korday24 + 256 + 315
korday26 = kfeb29 = korday25 + 594 + 219
k1i = korday2 / korday1
k2i = korday3 / korday2
k3i = korday4 / korday3
k4i = korday5 / korday4
k5i = korday6 / korday5
k6i = korday7 / korday6
k7i = korday8 / korday7
k8i = korday9 / korday8
k9i = korday10 / korday9
k10i = korday11 / korday10
k11i = korday12 / korday11
k12i = korday13 / korday12
k13i = korday14 / korday13
k14i = korday15 / korday14
k15i = korday16 / korday15
k16i = korday17 / korday16
k17i = korday18 / korday17
k18i = korday19 / korday18
k19i = korday20 / korday19
k20i = korday21 / korday20
k21i = korday22 / korday21
k22i = korday23 / korday22
k23i = korday24 / korday23
k24i = korday25 / korday24
k25i = korday26 / korday25
kav = (k1i + k2i + k3i + k4i + k5i + k6i + k7i + k8i + k9i + k10i + k11i + k12i + k13i + k14i + k15i + k16i + k17i + k18i + k19i + k20i + k21i + k22i + k23i + k24i + k25i)/25
k1ia = (k1i + kav)/2
k2ia = (k2i + kav)/2
k3ia = (k3i + kav)/2
k4ia = (k4i + kav)/2
k5ia = (k5i + kav)/2
k6ia = (k6i + kav)/2
k7ia = (k7i + kav)/2
k8ia = (k8i + kav)/2
k9ia = (k9i + kav)/2
k10ia = (k10i + kav)/2
k11ia = (k11i + kav)/2
k12ia = (k12i + kav)/2
k13ia = (k13i + kav)/2
k14ia = (k14i + kav)/2
k15ia = (k15i + kav)/2
k16ia = (k16i + kav)/2
k17ia = (k17i + kav)/2
k18ia = (k18i + kav)/2
k19ia = (k19i + kav)/2
k20ia = (k20i + kav)/2
k21ia = (k21i + kav)/2
k22ia = (k22i + kav)/2
k23ia = (k23i + kav)/2
k24ia = (k24i + kav)/2
k25ia = (k25i + kav)/2
day2inc = day2 / day1
day3inc = day3 / day2
day4inc = day4 / day3
day5inc = day5 / day4
day6inc = day6 / day5
day7inc = day7 / day6
day8inc = day8 / day7
day9inc = day9 / day8
day10inc = day10 / day9
day11inc = day11 / day10
day12inc = day12 / day11
day13inc = day13 / day12
day14inc = day14 / day13
day15inc = day15 / day14
day16inc = day16 / day15
day17inc = day17 / day16
day18inc = day18 / day17
day19inc = day19 / day18
day20inc = day20 / day19
day21inc = day21 / day20
day22inc = day22 / day21
day23inc = day23 / day22
day24inc = day24 / day23
day25inc = day25 / day24
day26inc = day26 / day25
day27inc = day27 / day26
day28inc = day28 / day27
day29inc = day29 / day28
day30inc = day30 / day29
day31inc = day31 / day30
day32inc = day32 / day31
day33inc = day33 / day32
day34inc = day34 / day33
day35inc = day35 / day34
day36inc = day36 / day35
day37inc = day37 / day36
day38inc = day38 / day37
day39inc = day39 / day38
addedinc = day2inc + day3inc + day4inc + day5inc + day6inc + day7inc + day8inc + day9inc + day10inc + day11inc + day12inc + day13inc + day14inc + day15inc + day16inc + day17inc + day18inc + day19inc + day20inc + day21inc + day22inc + day23inc + day24inc + day25inc + day26inc + day27inc + day28inc + day29inc + day30inc + day31inc + day32inc + day33inc + day34inc + day35inc + day36inc + day37inc + day38inc + day39inc
avinc = addedinc / 38
adjinc2 = ((avinc+day2inc) / 2)
adjinc3 = ((avinc+day3inc) / 2)
adjinc4 = ((avinc+day4inc) / 2)
adjinc5 = ((avinc+day5inc) / 2)
adjinc6 = ((avinc+day6inc) / 2)
adjinc7 = ((avinc+day7inc) / 2)
adjinc8 = ((avinc+day8inc) / 2)
adjinc9 = ((avinc+day9inc) / 2)
adjinc10 = ((avinc+day10inc) / 2)
adjinc11 = ((avinc+day11inc) / 2)
adjinc12 = ((avinc+day12inc) / 2)
adjinc13 = ((avinc+day13inc) / 2)
adjinc14 = ((avinc+day14inc) / 2)
adjinc15 = ((avinc+day15inc) / 2)
adjinc16 = ((avinc+day16inc) / 2)
adjinc17 = ((avinc+day17inc) / 2)
adjinc18 = ((avinc+day18inc) / 2)
adjinc19 = ((avinc+day19inc) / 2)
adjinc20 = ((avinc+day20inc) / 2)
adjinc21 = ((avinc+day21inc) / 2)
adjinc22 = ((avinc+day22inc) / 2)
adjinc23 = ((avinc+day23inc) / 2)
adjinc24 = ((avinc+day24inc) / 2)
adjinc25 = ((avinc+day25inc) / 2)
adjinc26 = ((avinc+day26inc) / 2)
adjinc27 = ((avinc+day27inc) / 2)
adjinc28 = ((avinc+day28inc) / 2)
adjinc29 = ((avinc+day29inc) / 2)
adjinc30 = ((avinc+day30inc) / 2)
adjinc31 = ((avinc+day31inc) / 2)
adjinc32 = ((avinc+day32inc) / 2)
adjinc33 = ((avinc+day33inc) / 2)
adjinc34 = ((avinc+day34inc) / 2)
adjinc35 = ((avinc+day35inc) / 2)
adjinc36 = ((avinc+day36inc) / 2)
adjinc37 = ((avinc+day37inc) / 2)
adjinc38 = ((avinc+day38inc) / 2)
adjinc39 = ((avinc+day39inc) / 2)
adj2inc2 = ((avinc+avinc+day2inc) / 3)
adj2inc3 = ((avinc+avinc+day3inc) / 3)
adj2inc4 = ((avinc+avinc+day4inc) / 3)
adj2inc5 = ((avinc+avinc+day5inc) / 3)
adj2inc6 = ((avinc+avinc+day6inc) / 3)
adj2inc7 = ((avinc+avinc+day7inc) / 3)
adj2inc8 = ((avinc+avinc+day8inc) / 3)
adj2inc9 = ((avinc+avinc+day9inc) / 3)
adj2inc10 = ((avinc+avinc+day10inc) / 3)
adj2inc11 = ((avinc+avinc+day11inc) / 3)
adj2inc12 = ((avinc+avinc+day12inc) / 3)
adj2inc13 = ((avinc+avinc+day13inc) / 3)
adj2inc14 = ((avinc+avinc+day14inc) / 3)
adj2inc15 = ((avinc+avinc+day15inc) / 3)
adj2inc16 = ((avinc+avinc+day16inc) / 3)
adj2inc17 = ((avinc+avinc+day17inc) / 3)
adj2inc18 = ((avinc+avinc+day18inc) / 3)
adj2inc19 = ((avinc+avinc+day19inc) / 3)
adj2inc20 = ((avinc+avinc+day20inc) / 3)
adj2inc21 = ((avinc+avinc+day21inc) / 3)
adj2inc22 = ((avinc+avinc+day22inc) / 3)
adj2inc23 = ((avinc+avinc+day23inc) / 3)
adj2inc24 = ((avinc+avinc+day24inc) / 3)
adj2inc25 = ((avinc+avinc+day25inc) / 3)
adj2inc26 = ((avinc+avinc+day26inc) / 3)
adj2inc27 = ((avinc+avinc+day27inc) / 3)
adj2inc28 = ((avinc+avinc+day28inc) / 3)
adj2inc29 = ((avinc+avinc+day29inc) / 3)
adj2inc30 = ((avinc+avinc+day30inc) / 3)
adj2inc31 = ((avinc+avinc+day31inc) / 3)
adj2inc32 = ((avinc+avinc+day32inc) / 3)
adj2inc33 = ((avinc+avinc+day33inc) / 3)
adj2inc34 = ((avinc+avinc+day34inc) / 3)
adj2inc35 = ((avinc+avinc+day35inc) / 3)
adj2inc36 = ((avinc+avinc+day36inc) / 3)
adj2inc37 = ((avinc+avinc+day37inc) / 3)
adj2inc38 = ((avinc+avinc+day38inc) / 3)
adj2inc39 = ((avinc+avinc+day39inc) / 3)
print('Day 1 (Jan 21) reported infections:' , day1)
print('Day 2 (Jan 22) increase' , day2inc)
print('Day 3 (Jan 23) increase' , day3inc)
print('Day 4 (Jan 24) increase' , day4inc)
print('Day 5 (Jan 25) increase' , day5inc)
print('Day 6 (Jan 26) increase' , day6inc)
print('Day 7 (Jan 27) increase' , day7inc)
print('Day 8 (Jan 28) increase' , day8inc)
print('Day 9 (Jan 29) increase' , day9inc)
print('Day 10 (Jan 30) increase' , day10inc)
print('Day 11 (Feb 1) increase' , day11inc)
print('Day 12 (Feb 2) increase' , day12inc)
print('Day 13 (Feb 3) increase' , day13inc)
print('Day 14 (Feb 4) increase' , day14inc)
print('Day 15 (Feb 5) increase' , day15inc)
print('Day 16 (Feb 6) increase' , day16inc)
print('Day 17 (Feb 7) increase' , day17inc)
print('Day 18 (Feb 8) increase' , day18inc)
print('Day 19 (Feb 9) increase' , day19inc)
print('Day 20 (Feb 10) increase' , day20inc)
print('Day 21 (Feb 11) increase' , day21inc)
print('Day 22 (Feb 12) increase' , day22inc)
print('Day 23 (Feb 13) increase' , day23inc)
print('Day 24 (Feb 14) increase' , day24inc)
print('Day 25 (Feb 15) increase' , day25inc)
print('Day 26 (Feb 16) increase' , day26inc)
print('Day 27 (Feb 17) increase' , day27inc)
print('Day 28 (Feb 18) increase' , day28inc)
print('Day 29 (Feb 19) increase' , day29inc)
print('Day 30 (Feb 20) increase' , day30inc)
print('Day 31 (Feb 21) increase' , day31inc)
print('Day 32 (Feb 22) increase' , day32inc)
print('Day 33 (Feb 23) increase' , day33inc)
print('Day 34 (Feb 24) increase' , day34inc)
print('Day 35 (Feb 25) increase' , day35inc)
print('Day 36 (Feb 26) increase' , day36inc)
print('Day 37 (Feb 27) increase' , day37inc)
print('Day 38 (Feb 28) increase' , day38inc)
print('Day 39 (Feb 29) increase' , day39inc)
y = [day2inc,day3inc,day4inc,day5inc,day6inc,day7inc,day8inc,day9inc,day10inc,day11inc,day12inc,day13inc,day14inc,day15inc,day16inc,day17inc,day18inc,day19inc,day20inc,day21inc,day22inc,day23inc,day24inc,day25inc,day26inc,day27inc,day28inc,day29inc,day30inc,day31inc,day32inc,day33inc,day34inc,day35inc,day36inc,day37inc,day38inc,day39inc]
y2 = [adjinc2,adjinc3,adjinc4,adjinc5,adjinc6,adjinc7,adjinc8,adjinc9,adjinc10,adjinc11,adjinc12,adjinc13,adjinc14,adjinc15,adjinc16,adjinc17,adjinc18,adjinc19,adjinc20,adjinc21,adjinc22,adjinc23,adjinc24,adjinc25,adjinc26,adjinc27,adjinc28,adjinc29,adjinc30,adjinc31,adjinc32,adjinc33,adjinc34,adjinc35,adjinc36,adjinc37,adjinc38,adjinc39]
y3 = [adj2inc2,adj2inc3,adj2inc4,adj2inc5,adj2inc6,adj2inc7,adj2inc8,adj2inc9,adj2inc10,adj2inc11,adj2inc12,adj2inc13,adj2inc14,adj2inc15,adj2inc16,adj2inc17,adj2inc18,adj2inc19,adj2inc20,adj2inc21,adj2inc22,adj2inc23,adj2inc24,adj2inc25,adj2inc26,adj2inc27,adj2inc28,adj2inc29,adj2inc30,adj2inc31,adj2inc32,adj2inc33,adj2inc34,adj2inc35,adj2inc36,adj2inc37,adj2inc38,adj2inc39]
y4 = [k1i,k2i,k3i,k4i,k5i,k6i,k7i,k8i,k9i,k10i,k11i,k12i,k13i,k14i,k15i,k16i,k17i,k18i,k19i,k20i,k21i,k22i,k23i,k24i,k25i]
y7 = [k1ia,k2ia,k3ia,k4ia,k5ia,k6ia,k7ia,k8ia,k9ia,k10ia,k11ia,k12ia,k13ia,k14ia,k15ia,k16ia,k17ia,k18ia,k19ia,k20ia,k21ia,k22ia,k23ia,k24ia,k25ia]
y5 = [it1i,it2i,it3i,it4i,it5i,it6i,it7i,it8i,it9i,it10i,it11i]
y6 = [it1ia,it2ia,it3ia,it4ia,it5ia,it6ia,it7ia,it8ia,it9ia,it10ia,it11ia]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
x2 = [4,5,8,9,10,11,13,14,16,18,20,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
x3 = [15,29,30,31,32,33,34,35,36,37,38]
maxinc = max(y)
mininc = min(y)
p1=('World-Lowest delta for spread of infection:' , mininc)
p2=('World-Average delta for spread of infection: ' , avinc)
p3=('World-Highest delta for spread of infection:', maxinc)
p4=('Korea-Lowest delta for spread of infection:' , min(y4))
p5=('Korea-Average delta for spread of infection: ' , kav)
p6=('Korea-Highest delta for spread of infection:', max(y4))
p7=('Italy-Lowest delta for spread of infection:' , min(y5))
p8=('Italy-Average delta for spread of infection: ' , itav)
p9=('Italy-Highest delta for spread of infection:', max(y5))
people = 1
day = 0
while ( people < 7500000000):
    day = day + 1
    people = people * mininc
print('at the minimum growth rate of' , mininc , 'we gotta bout' , day + 1 , 'days, or' , day / 365 , 'years')
people = 1
day = 0
while ( people < 7500000000):
    day = day + 1
    people = people * avinc
print('at the average growth rate of' , avinc , 'we gotta bout' , day + 1 , 'days, or' , day / 30 , 'months')
people = 1
day = 0
while ( people < 7500000000):
    day = day + 1
    people = people * maxinc
print('at the maximum growth rate of' , maxinc , 'we gotta bout' , day + 1 , 'days, or' , day / 30 , 'months')
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()
var_6 = IntVar()
var_7 = IntVar()
line_1 = Checkbutton(window, text = 'world',\
                     variable = var_1, onvalue = 1, offvalue = 0)
line_2 = Checkbutton(window, text = 'normailzed-world',\
                     variable = var_2, onvalue = 1, offvalue = 0)
line_3 = Checkbutton(window, text = 'extreme normalized-world',\
                     variable = var_3, onvalue = 1, offvalue = 0)
line_4 = Checkbutton(window, text = 'korea',\
                     variable = var_4, onvalue = 1, offvalue = 0)
line_5 = Checkbutton(window, text = 'korea-normalized',\
                     variable = var_5, onvalue = 1, offvalue = 0)
line_6 = Checkbutton(window, text = 'italy',\
                     variable = var_6, onvalue = 1, offvalue = 0)
line_7 = Checkbutton(window, text = 'italy-normalized',\
                     variable = var_7, onvalue = 1, offvalue = 0)
def dialog():
    if var_1.get()==1:plt.plot(x, y, label = "reported values - world (BNONEWS)")
    if var_2.get()==1:plt.plot(x, y2, label = "in respect to average change - world")
    if var_3.get()==1:plt.plot(x, y3, label = "extreme normalization - world")
    if var_4.get()==1:plt.plot(x2, y4, label = "korea (BNONEWS)")
    if var_5.get()==1:plt.plot(x2, y7, label = "korea-normalized")
    if var_6.get()==1:plt.plot(x3, y5, label = "italy (BNONEWS)")
    if var_7.get()==1:plt.plot(x3, y6, label = "italy-normalized")
    plt.ylabel('rate of increase in respect to previous day')
    plt.xlabel('days (Jan21-Feb29)')
    plt.title('Rate of COVID-19 spread')
    plt.show()
btn = Button(window, text = 'graph selected lines' , command = dialog)
btn.grid(row = 11)
label2 = Label(window, text = p1)
label2.grid(row = 13)
label3 = Label(window, text = p2)
label3.grid(row = 15)
label4 = Label(window, text = p3)
label4.grid(row = 17)
label5 = Label(window, text = p4)
label5.grid(row = 19)
label6 = Label(window, text = p5)
label6.grid(row = 21)
label7 = Label(window, text = p6)
label7.grid(row = 23)
label8 = Label(window, text = p7)
label8.grid(row = 25)
label9 = Label(window, text = p8)
label9.grid(row = 27)
label10 = Label(window, text = p9)
label10.grid(row = 29)
line_1.grid(row = 4)
line_2.grid(row = 5)
line_3.grid(row = 6)
line_4.grid(row = 7)
line_5.grid(row = 8)
line_6.grid(row = 9)
line_7.grid(row = 10)
window.mainloop()
