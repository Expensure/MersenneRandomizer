import Mersenne


def match_chances():
    ajax_thuis = [[0, 0, 100], [65, 17, 18], [54, 21, 25], [74, 14, 12], [78, 13, 9]]
    feyenoord_thuis = [[30, 21, 49], [0, 0, 100], [37, 24, 39], [51, 22, 27], [60, 21, 19]]
    psv_thuis = [[39, 22, 39], [54, 22, 24], [0, 0, 100], [62, 20, 18], [62, 22, 16]]
    utrecht_thuis = [[25, 14, 61], [37, 23, 40], [29, 24, 47], [0, 0, 100], [52, 23, 25]]
    willem_thuis = [[17, 18, 65], [20, 26, 54], [23, 24, 53], [37, 25, 38], [0, 0, 100]]
    all_chances = (ajax_thuis, feyenoord_thuis, psv_thuis, utrecht_thuis, willem_thuis)
    chances = []
    for i in all_chances:
        for j in i:
            chances.append(j)
    return chances


def all_matches():
    matching = []
    for i in teams:
        for j in teams:
            match = [i, j]
            matching.append(match)
    return matching


def play_all():
    all_chances = match_chances()
    scorelijst = [0, 0, 0, 0, 0]
    matches = all_matches()
    matchnumber = 1
    for i in matches:
        propability = all_chances[matchnumber - 1]
        random_number = rng.randint(1, 100)
        t_thuis = i[0]
        t_uit = i[1]
        matchnumber += 1
        grens1 = propability[0]
        grens2 = (propability[0] + propability[1])
        if t_thuis != t_uit:
            if random_number < grens1:
                code = 1
            elif random_number < grens2:
                code = 0
            else:
                code = 2
        else:
            code = 3
        result_of_match(code, t_thuis, t_uit, scorelijst)
    return (scorelijst)


def result_of_match(code, thuisploeg, uitploeg, scorelijst):
    #
    if code == 1:
        thuisteamscore = 3
        uitteamscore = 0
    if code == 0:
        thuisteamscore = 1
        uitteamscore = 1
    if code == 2:
        thuisteamscore = 0
        uitteamscore = 3
    if code == 3:
        thuisteamscore = 0
        uitteamscore = 0
    if thuisploeg != uitploeg:
        if thuisploeg == "Ajax":
            scorelijst[0] = (int(scorelijst[0] + thuisteamscore))
        if uitploeg == "Ajax":
            scorelijst[0] = (int(scorelijst[0] + uitteamscore))

        if thuisploeg == "Feyenoord":
            scorelijst[1] = (int(scorelijst[1] + thuisteamscore))
        if uitploeg == "Feyenoord":
            scorelijst[1] = (int(scorelijst[1] + uitteamscore))

        if thuisploeg == "PSV":
            scorelijst[2] = (int(scorelijst[2] + thuisteamscore))
        if uitploeg == "PSV":
            scorelijst[2] = (int(scorelijst[2] + uitteamscore))

        if thuisploeg == "FC Utrecht":
            scorelijst[3] = (int(scorelijst[3] + thuisteamscore))
        if uitploeg == "FC Utrecht":
            scorelijst[3] = (int(scorelijst[3] + uitteamscore))

        if thuisploeg == "Willem II":
            scorelijst[4] = (int(scorelijst[4] + thuisteamscore))
        if uitploeg == "Willem II":
            scorelijst[4] = (int(scorelijst[4] + uitteamscore))
    return scorelijst


def final_results():
    #Geeft de winnaar van een ronde
    totaal = play_all()
    temp_leadingnumber = 0
    secondary_index = 0
    for i in totaal:
        if i > temp_leadingnumber:
            temp_leadingnumber = i
            winning_team = teams[secondary_index]
        secondary_index += 1
    return winning_team

def batchrunner(rounds):
    resultlist = []
    for i in range(0, rounds):
        winner = final_results()
        resultlist.append(winner)
    print("Total Number of Times 'Ajax' won = ", resultlist.count('Ajax'), " winning ", round((resultlist.count('Ajax')/rounds)*100,2), " percent of rounds")
    print("Total Number of Times 'Feyenoord' won = ", resultlist.count('Feyenoord'), " winning ", round((resultlist.count('Feyenoord')/rounds)*100,2), " percent of rounds")
    print("Total Number of Times 'PSV' won = ", resultlist.count('PSV'), " winning ", round((resultlist.count('PSV')/rounds)*100,2), " percent of rounds")
    print("Total Number of Times 'FC Utrecht' won = ", resultlist.count('FC Utrecht'), " winning ", round((resultlist.count('FC Utrecht')/rounds)*100,2), " percent of rounds")
    print("Total Number of Times 'Willem II' won = ", resultlist.count('Willem II'), " winning ", round((resultlist.count('Willem II')/rounds)*100,2), " percent of rounds")


rng = Mersenne.PRNG_Mersenne()
rng.seed= int(input("Vul een seed in"))
rounds = int(input("Hoeveel rondes moeten er gerund worden?"))
teams = ["Ajax", "Feyenoord", "PSV", "FC Utrecht", "Willem II"]
chances = match_chances()
batchrunner(rounds)

