def main():
    inputstr = 'X'
    grades = []
    weights = []
    valid_input = False
    
    while not valid_input:
        while not inputstr[0] == '':
            print('Enter a known grade (decimal from 0) and its weight (decimal from 0 to 1), separated by a space. To stop inputting grades, enter nothing. > ')
            inputstr = input().split(' ')
            try:
                grades.append(float(inputstr[0]))
                weights.append(float(inputstr[1]))
            except:
                if not inputstr[0] == '':
                    print('Invalid input received. Please re-enter your input.')
                    continue
            else:
                if inputstr[0] < 0 or inputstr[1] < 0 or inputstr[1] > 1:
                    print('Invalid input received. Please re-enter your input.')
                    continue

        if len(grades) == 0:
            print('No input received. Please re-enter your input.')
            continue

        unknown_weight = 0
        while unknown_weight == 0:
            print('Now enter your unknown grade\'s weight (decimal from 0 to 1), separated by a space. > ')
            try:
                unknown_weight = float(input())
            except:
                print('Invalid input received. Please re-enter your input.')
                continue

        summation = sum(weights) + unknown_weight

        if not summation == 1:
            print('Weights must total to 1, however, the provided inputs total to ' + str(summation) + '. Please re-enter your input.')

            # reset inputs; requires a full restart
            inputstr = 'X'
            grades = weights = []

            continue

        target = -1
        while target < 0 or target > 100:
            print('Now enter your target grade percentage (integer from 0-100). > ')
            try:
                target = int(input())
            except:
                print('Invalid input received. Please re-enter your input.')
                continue
            else:
                if target < 0 or target > 100:
                    print('Target input out of range. Please re-enter your input.')
                    continue

        # function we will use here will look like (grade1)(weight1) + (grade2)(weight2) + ... + (gradeN)(weightN) - (target) = -x(unknown_weight)
        weighted_grades = []
        for i in range(len(grades)):
            weighted_grades.append(grades[i] * weights[i])

        total = round((((sum(weighted_grades) - target) / unknown_weight) * -1), 2)

        if total > 100:
            print('It looks like this grade isn\'t possible :( Technically...')
        elif total < 0:
            print('It looks like this grade isn\'t possible :) Technically...')
        print('You will need about a ' + str(total) + '% to achieve a final grade of ' + str(target) + '%.')

        valid_input = True

main()