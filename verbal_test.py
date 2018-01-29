import csv
import random

def UserInterface():
    ModeSelect = input('Select mode: \n 1) Random \n 2) Ordered \n 3) Review \n Plz enter the corresponding number:')

    # Set the path of the file
    path = r'C:\Users\sfaaz007\Desktop\大惟\vocabulary.csv'
    print('ModeSelect', ModeSelect)
    tmplist = []
    with open(path, 'r', encoding='utf8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            tmplist.append(row)

    if ModeSelect == '1' or ModeSelect == '2':
        print('Select Mode: Random test')

        # Initialize essential variables
        score = 0
        count = 0

        # Start the test
        while tmplist:
            count += 1

            # Determine an index for random or ordered showing one question
            if ModeSelect == '1':
                pick = int(random.random()*len(tmplist))
            else:
                pick = 0
                
            # Collect the answer from users
            reply = input('\n {}'.format(tmplist[pick][2]))

            # Verify the answer
            if reply == tmplist[pick][0]:
                score += 1
                print('Correct!')
            else:
                print('\n The correct answer is \n -- {} --'.format(tmplist[pick][0]))
            del tmplist[pick]

            # Set breaking points
            if count % 10 == 0:
                print('You have learned {} vocabularies.'.format(count))
                print('You got {} points.'.format(score))
                process = input('Do u want to take a rest? (Y/N):')
                if process == 'Y':
                    tmplist = []

        print('You have learned {} vocabularies.'.format(count))        
        print('You got {} points.'.format(score))

    elif ModeSelect == '3':
        for ele in tmplist:
            print(ele)
    else:
        print('U have to enter integer number from 1 to 3.')

if __name__=='__main__':
    x = UserInterface()

