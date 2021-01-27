# Input
# 0,0,100 omdat elke team tegen zich zelf speelt, kan gelezen worden als verlies.
ajax_thuis = [[0, 0, 100], [65, 17, 18], [54, 21, 25], [74, 14, 12], [78, 13, 9]]
feyenoord_thuis = [[30, 21, 49], [0, 0, 100], [37, 24, 39], [51, 22, 27], [60, 21, 19]]
psv_thuis = [[39, 22, 39], [54, 22, 24], [0, 0, 100], [62, 20, 18], [62, 22, 16]]
utrecht_thuis = [[25, 14, 61], [37, 23, 40], [29, 24, 47], [0, 0, 100], [52, 23, 25]]
willem_thuis = [[17, 18, 65], [20, 26, 54], [23, 24, 53], [37, 25, 38], [0, 0, 100]]
team_uit = ["Ajax", "Feyenoord", "PSV", "FC Utrecht", "Willem II"]

# Mijn idee was om het te veranderen in een cumulatief is, zodat ik
# met mijn randomizer alleen maar 0 tot 100 hoef te doen.
# dus dat ik krijg(voorbeeld ajaxthuis feyenoord uit:)
# random getal tussen 1 en 100, kansen zijn [65,17,18]
# win = 1 - 65, gelijk = 65 - 82(65+17), velies = 82 - 100








# basisprincipe grenzen
for i in ajax_thuis:
    grens1 = i[0]
    grens2 = (i[0] + i[1])

# basisprincipe punten
scoreajax = 0
for i in ajax_thuis:
    grens1 = i[0]
    grens2 = (i[0] + i[1])
    if rnggen < grens1:
        scoreajax += 3
    elif rnggen < grens2:
        scoreajax += 1
    else:
        scoreajax += 0
