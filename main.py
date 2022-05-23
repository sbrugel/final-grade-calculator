from PIL import Image, ImageDraw, ImageOps

def main():
    inputstr = 'X'
    grades = []
    weights = []
    valid_input = False

    while not valid_input:
        while not inputstr[0] == '':
            print('Enter a known grade (decimal >= 0) and its weight (decimal from 0 to 1), separated by a space. To stop inputting grades, enter nothing. > ')
            inputstr = input().split(' ')
            try:
                grades.append(float(inputstr[0]))
                weights.append(float(inputstr[1]))
            except:
                if not inputstr[0] == '':
                    print('Invalid input received. Please re-enter your input.')
                    continue
            else:
                if float(inputstr[0]) < 0 or float(inputstr[1]) < 0 or float(inputstr[1]) > 1:
                    print('Invalid input received. Please re-enter your input.')
                    continue

        if len(grades) == 0:
            print('No input received. Please re-enter your input.')
            continue

        unknown_weight = 0
        while unknown_weight == 0:
            print('Now enter your unknown grade\'s weight (decimal from 0 to 1). > ')
            try:
                unknown_weight = float(input())
            except:
                print('Invalid input received. Please re-enter your input.')
                continue

        target = -1
        while target < 0:
            print('Now enter your target grade percentage (integer >= 0). > ')
            try:
                target = float(input())
            except:
                print('Invalid input received. Please re-enter your input.')
                continue
            else:
                if target < 0:
                    print('Target input out of range. Please re-enter your input.')
                    continue

        # function we will use here will look like (grade1)(weight1) + (grade2)(weight2) + ... + (gradeN)(weightN) - (target) = -x(unknown_weight)
        weighted_grades = []
        for i in range(len(grades)):
            weighted_grades.append(grades[i] * weights[i])

        total = round((((sum(weighted_grades) - target) / unknown_weight) * -1), 2)

        print('===RESULTS===')
        if total > 100:
            print('\tIt looks like this grade isn\'t possible :( Technically...')
        elif total < 0:
            print('\tIt looks like this grade isn\'t possible :) Technically...')
        print('\tYou will need about a ' + str(total) + '% to achieve a final grade of ' + str(target) + '%.')
        print('\tThe highest final grade that can be achieved (grade on assignment is 100%) is ' + round((str(sum(weighted_grades) + (100*unknown_weight))), 2) + '%')
        print('\tThe lowest final grade that can be achieved (grade on assignment is 0%) is ' + round((str(sum(weighted_grades))), 2) + '%')

        # ask user if they want image drawn here
        print('Would you like a graph drawn of achieved grades vs. final grade achieved? (y/n) > ')
        y_n = input()
        if y_n == 'y' or y_n == 'Y':
            draw_image(weighted_grades, unknown_weight)

        valid_input = True

def draw_image(weighted_grades, unknown_weight):
    image = Image.new('RGB', (560, 275), (255, 255, 255)) # white background

    # set up canvas
    draw = ImageDraw.Draw(image)

    # draw labels (y-axis)
    draw.text((5, 20),  'Final Grade', (255,0,0))
    draw.text((25, 40), '100%', (0,0,0))
    draw.text((25, 60), '90%', (0,0,0))
    draw.text((25, 80), '80%', (0,0,0))
    draw.text((25, 100), '70%', (0,0,0))
    draw.text((25, 120), '60%', (0,0,0))
    draw.text((25, 140), '50%', (0,0,0))
    draw.text((25, 160), '40%', (0,0,0))
    draw.text((25, 180), '30%', (0,0,0))
    draw.text((25, 200), '20%', (0,0,0))
    draw.text((25, 220), '10%', (0,0,0))
    draw.text((25, 245), '0%', (0,0,0))

    # draw gridlines (for y-values)
    for i in range(45, 265, 20):
        draw.line([(50, i), (525, i)], (171, 171, 171))

    # draw labels (x-axis)
    draw.text((240, 255), 'Grade Achieved', (0,0,255), None, 4, 'center')
    draw.text((520, 245), '100%', (0,0,0))
    draw.text((470, 245), '90%', (0,0,0))
    draw.text((420, 245), '80%', (0,0,0))
    draw.text((370, 245), '70%', (0,0,0))
    draw.text((320, 245), '60%', (0,0,0))
    draw.text((270, 245), '50%', (0,0,0))
    draw.text((220, 245), '40%', (0,0,0))
    draw.text((170, 245), '30%', (0,0,0))
    draw.text((120, 245), '20%', (0,0,0))
    draw.text((70, 245), '10%', (0,0,0))
    draw.text((25, 245), '0%', (0,0,0))

    # draw gridlines (for x-values)
    for i in range(75, 575, 50):
        draw.line([(i, 245), (i, 45)], (171, 171, 171))

    # draw axes
    draw.line([(50, 40), (50, 245)], (0,0,0))
    draw.line([(50, 245), (530, 245)], (0,0,0))

    # calculate line to draw
    known_total = sum(weighted_grades)
    grade_at_0 = known_total
    grade_at_100 = known_total + (100*unknown_weight)

    startpoint = (50, (240 - (grade_at_0*2)) + 5)
    endpoint = (525, (240 - (grade_at_100*2)) + 5)

    # draw main line
    draw.line([startpoint, endpoint], (0,255,0))

    print('What folder would you like to save this file in? > (don\'t include the trailing backslash) ')
    folder = input()
    print('What name would you like to save the file as? (don\'t include the leading backslash/trailing extension) > ')
    name = input()

    image = ImageOps.scale(image, 2) # scale the image for ease of reading
    image = image.save(folder + '\\' + name + '.png')

main()