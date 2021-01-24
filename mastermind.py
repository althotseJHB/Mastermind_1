import random


def run_game():

    '''
        Gets 4 random digits, make sure there's no repeating code
    '''
    code = [] #empty list
    # hard_set = 6378 #testing reasons
    for x in range(0,4): #iterate through the list
        random_digits = random.randint(1,8) #randomly generate
        while random_digits in code:
            random_digits = random.randint(1,8)
        code += [random_digits]


    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    correct1 = False
    turns = 12
# --------------- GAME LOOP ----------------------------
    while not correct1 and turns > 0:
# ----------------- Step 2: Get a guess ------------------
        usser = ''
        while True:
            usser = input("Input 4 digit code: ")
            if len(usser) > 4 or len(usser) < 4:
                    print("Please enter exactly 4 digits.")
                    continue
            else:
                break
# ----------------step 3: EVALUATE INPUT ---------------
        correct_position = 0
        correct_number = 0
        for i in range(0, len(usser)):
            if int(usser[i]) == code[i]:
                correct_position += 1
            elif int(usser[i]) in code:
                correct_number += 1
# ----------------step 4: Count guesses ------------------
        turns -= 1
        if correct_position == 4:
            print('Number of correct digits in correct place:    ', correct_position)
            print('Number of correct digits not in correct place:', correct_number)
            print('Congratulations! You are a codebreaker!')
            break
        else:
            print('Number of correct digits in correct place:    ', correct_position)
            print('Number of correct digits not in correct place:', correct_number)
            print('Turns left:', turns)
    code_string = ''
    for i in code:
        code_string += str(i)

    print('The code was:', code_string)


if __name__ == "__main__":
    run_game()
