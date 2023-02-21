print()
print('H A N G M A N')

count_win = []
count_lost = []

while True:
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    if menu == 'play':

        import random

        list_of_words = ['python', 'java', 'swift', 'javascript']
        randomword = random.choice(list_of_words)
        tries = 0
        displaylist = []
        s = []

        for letter in randomword:
            displaylist.append('-')
        print(''.join(displaylist))

        while '-' in displaylist and tries < 8:

            x = input('Input a letter: ')
            k = list(randomword)
            if len(x) == 1:
                if x.islower() and x.isascii():
                    if x in k:

                        if x in s:
                            print("You've already guessed this letter.")
                            print()
                            print(''.join(displaylist))
                            tries += 1


                        else:
                            while x in k:
                                s.append(x)

                                displaylist[''.join(k).find(x)] = x
                                k[''.join(k).find(x)] = ' '
                                print()
                                print(''.join(displaylist))
                    else:
                        tries += 1
                        print("That letter doesn't appear in the word.")
                        print()
                        print(''.join(displaylist))

                        if tries >= 8:
                            break

                else:
                    print('Please, enter a lowercase letter from the English alphabet.')
                    print()
                    print(''.join(displaylist))
            else:
                print('Please, input a single letter.')
                print()
                print(''.join(displaylist))

        if '-' not in displaylist:
            count_win.append('1')
            print('You guessed the word ' + str(randomword) + '!')
            survived = 'You survived!'
            print(survived)

        else:
            count_lost.append('1')
            lost = 'You lost!'
            print(lost)

    elif menu == 'results':
        print('You won: ' + str(len(count_win)) + ' times.')
        print('You lost: ' + str(len(count_lost)) + ' times.')

    elif menu == 'exit':
        break
    else:
        menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
