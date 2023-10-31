import random
import copy
def importance_weight(listofmuscles):
    total = sum(listofmuscles)
    finalweights = []
    for x in listofmuscles:
        weight = int((x/total) * 21)
        finalweights.append(weight)
    return finalweights
def loopuntilright(musclename, upbound, lowbound):
    invalid = 0
    upbound1 = int(upbound)
    lowbound1 = int(lowbound)
    while invalid == 0:
        muscle = int(input(f'{musclename}: '))
        if (muscle < upbound1) and (muscle >= lowbound1):
            invalid += 1
        else:
            print('invalid response')
    return muscle        
def muscleimportance(listmus):
    importance = []
    for x in listmus:
        final = loopuntilright(x,11,0)
        importance.append(final)
    return importance
def setsperweek(weightlist):
    initialamt = 21
    finallist = []
    for x in weightlist:
        setsperweek = int(x * 21.00)
        finallist.append(setsperweek)
    return finallist
def make_plan(setsweek, intensify,spit):
    chestex = [['Incline Dumbbell Fly', 'Pec Dec', 'Cable Lower-Upper Fly'], ['Hammerstreangth incline Press', 'Incline Dumbell Bench Press', 'Barbell Benchpress'], ['Weighted Dips', 'Upper-Lower Cable Fly', 'Incline Barbell Benchpress'] ]
    backex = [['Lat Pulldown', 'V Grip Lat Pulldown', 'Chest Supported Incline Dumbbell Row'], ['Lat Pullover', 'Single Arm Dumbbell Row', 'Barbell Row'], ['Bentover Barbell Row', 'Weighted Pullup', 'Seated Cable Row'] ]
    bicepex = [['Seated Hammer Curl', 'Spider Hammer Curl', 'Zottman Curl'], ['Incline Curls', 'Seated Curls', 'Standing Curls'], ['Machine Preacher Curl', 'Spider Curls', 'Arm Blaster Curl']]
    tricepex = [['Cable Tricep Extension', 'EZ Bar Skullcrusher', 'EZ Bar Skullcrusher'], ['Cable Overhead Tricep Extension', 'Close-grip Benchpress', 'Cable Overhead Tricep Extension' ], ['Cable Katana Extension', 'Cable Katana Extension', 'Weighted Tricep Dips']]
    shoulderex = [['Seated Lateral raise', 'Shoulder Press', 'Seated Lateral raise'], ['Closegrip Shoulder Benchpress', 'Dumbbell Front Raise', 'Cable Front Raise'], ['Reverse Pec Dec', 'Dummbell Y Raise', 'Reverse Pec Dec']]
    quadex = [['Barbell Squat', 'Barbell Squat', 'Barbell Squat'], ['Leg Extension','Leg Extension', 'Leg Extension' ], ['Front Squat', 'Front Squat', 'Front Squat']]
    hamex = [['Romanian Deadlift', 'Romanian Deadlift', 'Romanian Deadlift'], ['Leg Curl', 'Leg Curl', 'Leg Curl'], ['Leg Press', 'Leg Press', 'Leg Press']]
    def equal3(musclelist):
        plan = []
        for i in range(0,3):
            ran = random.randint(0, 2)
            excersize11 = musclelist[i][ran]
            plan.append(excersize11)
        return plan
    def otherthan3(musclelist, amsperweek):
        amtperweek = int(amsperweek)
        plan = []
        listcopy = []
        listcopy2 = copy.deepcopy(musclelist)
        for x in range(amtperweek):
            if len(listcopy) == 0:
                listcopy = copy.deepcopy(listcopy2)
            listlist = random.choice(listcopy)
            excersize = random.choice(listlist)
            plan.append(excersize)
            listcopy.remove(listlist)
            indexcopy = listcopy2.index(listlist)
            indexcopy2 = listcopy2[indexcopy].index(excersize)
            listcopy2[indexcopy].pop(indexcopy2)
        return plan
    def daysetup(day,plans,sets):
        realplanplan = day+'\n~~~~~~~~~~~~~~\n'
        for x in plans:
            for ex in x:
                realplanplan += ex+'\n' +sets + '-'+'\n\n'
            realplanplan += '-----------------------------\n'
        realplanplan += '\n'
        return realplanplan
    chestplan = otherthan3(chestex,setsweek[0])
    backplan = otherthan3(backex,setsweek[1])
    bicepplan = otherthan3(bicepex,setsweek[2])
    tricepplan = otherthan3(tricepex,setsweek[3])
    shoulderplan = otherthan3(shoulderex,setsweek[4])
    quadplan = []
    setnum = ''
    if intensify == 1:
        setnum = ' 1 warmup set of 8 reps, 2 sets to failiure, 30 seconds of rest'
    elif intensify == 2:
        setnum = ' 3 sets of 10'
    if setsweek[5] < 3:
        quadplan = otherthan3(quadex,setsweek[5])
    else:
        quadplan = equal3(quadex)
    hamplan = []
    if setsweek[5] < 3:
        hamplan = otherthan3(hamex,setsweek[6])
    else:
        quadplan = equal3(hamex)
    day1 = ''
    day2 = ''
    day3 = ''
    if spit == 1:
        day1 = daysetup('Day 1: ', [chestplan, backplan], setnum)
        day2 = daysetup('Day 2: ', [bicepplan, tricepplan, shoulderplan], setnum)
        day3 = daysetup('Day 3: ', [quadplan, hamplan], setnum)
    elif spit == 2:
        day1 = daysetup('Day 1: ', [chestplan, tricepplan, shoulderplan], setnum)
        day2 = daysetup('Day 2: ', [bicepplan, backplan], setnum)
        day3 = daysetup('Day 3: ', [quadplan, hamplan], setnum)
    planfinals = f'{day1}{day2}{day3}'
    return planfinals

muscles = ['chest', 'back', 'bicep', 'tricep', 'shoulders', 'quads', 'hams']


muscleranking = muscleimportance(muscles) # List of user rankings
weightslist = importance_weight(muscleranking) #List of sets per week adjusted to weight
intensity = loopuntilright('Would you rather train with 1. High intensity lower reps, or 2.Higher reps lower intensity', 3, 0)
split = loopuntilright('Do you Prefer a 1. Arnold Split or 2. Push Pull Legs', 3, 0)

paan = make_plan(weightslist, intensity,split)
print(paan + 'Feel free to mix around excersizes. Repeat this program twice a week if you plan to train 6 times a week' )


    
    
        

