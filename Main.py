import Mersenne

def match_chances():
    # Zet alle wedstrijdkansen van een ronde in een lijst
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
    #Zet alle wedstrijden van een ronde in een lijst
    matching = []
    for i in teams:
        for j in teams:
            match = [i, j]
            matching.append(match)
    return matching


def play_all():
    #Maakt de hele scorelijst van een ronde
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
    #Geeft punten aan het thuisteam en uitteam als ze spelen
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
    teams = ["Ajax", "Feyenoord", "PSV", "FC Utrecht", "Willem II"]
    temp_teams = teams
    #Firstplacelist
    temp_leadingnumber, secondary_index, saving_index = 0, 0, 0
    for i in totaal:
        if i > temp_leadingnumber:
            temp_leadingnumber = i
            winning_team = teams[secondary_index]
            saving_index = secondary_index
        secondary_index += 1
    temp_teams.remove(temp_teams[saving_index])
    totaal.remove(totaal[saving_index])

    #Secondplacelist
    temp_leadingnumber, secondary_index, saving_index = 0, 0, 0
    for i in totaal:
        if i > temp_leadingnumber:
            temp_leadingnumber = i
            second_team = teams[secondary_index]
            saving_index = secondary_index
        secondary_index += 1
    temp_teams.remove(temp_teams[saving_index])
    totaal.remove(totaal[saving_index])

    #Thirdplacelist
    temp_leadingnumber, secondary_index, saving_index = 0, 0, 0
    for i in totaal:
        if i > temp_leadingnumber:
            temp_leadingnumber = i
            third_team = teams[secondary_index]
            saving_index = secondary_index
        secondary_index += 1
    temp_teams.remove(temp_teams[saving_index])
    totaal.remove(totaal[saving_index])

    #Fourthplacelist
    temp_leadingnumber, secondary_index, saving_index = 0, 0, 0
    for i in totaal:
        if i > temp_leadingnumber:
            temp_leadingnumber = i
            fourth_team = teams[secondary_index]
            saving_index = secondary_index
        secondary_index += 1
    temp_teams.remove(temp_teams[saving_index])
    totaal.remove(totaal[saving_index])

    #Fifthplacelist:
    fifth_team = temp_teams[0]
    return winning_team,second_team,third_team,fourth_team,fifth_team



def batchrunner(rounds):
    winlist = []
    secondlist = []
    thirdlist = []
    fourthlist = []
    fifthlist = []
    #Maakt tabel van grote batch aan rondes
    for i in range(0, rounds):
        winner,second,third,fourth,fifth = final_results()
        winlist.append(winner)
        secondlist.append(second)
        thirdlist.append(third)
        fourthlist.append(fourth)
        fifthlist.append(fifth)
    print ('Ajax      | 1st', round((winlist.count('Ajax')/rounds)*100,2), '%| 2nd', round((secondlist.count('Ajax')/rounds)*100,2), '%| 3rd', round((thirdlist.count('Ajax')/rounds)*100,2), '%| 4th', round((fourthlist.count('Ajax')/rounds)*100,2), '%| 5th', round((fifthlist.count('Ajax')/rounds)*100,2)),'%'
    print ('Feyenoord | 1st', round((winlist.count('Feyenoord')/rounds)*100,2), '%| 2nd', round((secondlist.count('Feyenoord')/rounds)*100,2), '%| 3rd', round((thirdlist.count('Feyenoord')/rounds)*100,2), '%| 4th', round((fourthlist.count('Feyenoord')/rounds)*100,2), '%| 5th', round((fifthlist.count('Feyenoord')/rounds)*100,2)),'%'
    print ('PSV       | 1st', round((winlist.count('PSV')/rounds)*100,2), '%| 2nd', round((secondlist.count('PSV')/rounds)*100,2), '%| 3rd', round((thirdlist.count('PSV')/rounds)*100,2), '%| 4th', round((fourthlist.count('PSV')/rounds)*100,2), '%| 5th', round((fifthlist.count('PSV')/rounds)*100,2)),'%'
    print ('FC Utrecht| 1st', round((winlist.count('FC Utrecht') / rounds) * 100, 2), '%| 2nd',round((secondlist.count('FC Utrecht') / rounds) * 100, 2), '%| 3rd',round((thirdlist.count('FC Utrecht') / rounds) * 100, 2), '%| 4th',round((fourthlist.count('FC Utrecht') / rounds) * 100, 2), '%| 5th',round((fifthlist.count('FC Utrecht') / rounds) * 100, 2)),'%'
    print ('Willem II | 1st', round((winlist.count('Willem II') / rounds) * 100, 2), '%| 2nd',round((secondlist.count('Willem II') / rounds) * 100, 2), '%| 3rd',round((thirdlist.count('Willem II') / rounds) * 100, 2), '%| 4th',round((fourthlist.count('Willem II') / rounds) * 100, 2), '%| 5th',round((fifthlist.count('Willem II') / rounds) * 100, 2)),'%'


rng = Mersenne.PRNG_Mersenne()
rng.seed= int(input("Vul een seed in"))
rounds = int(input("Hoeveel rondes moeten er gerund worden?"))
teams = ["Ajax", "Feyenoord", "PSV", "FC Utrecht", "Willem II"]
chances = match_chances()
batchrunner(rounds)

