import random
import os
import time


def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def list_maker():
    list_of_questions = []
    with open('Questions.md', 'r') as raw_txt:
        for line in raw_txt:
            list_of_questions.append(line)
    return list_of_questions


def get_answers_list():
    answers = []
    with open('module_progbasics.md') as raw_txt:
        answer = ''
        for line in raw_txt:
            if "#" not in line and line != '\n':
                answer += line
            if "#" in line:
                if len(answer) > 0:
                    answers.append(answer)
                    answer = ''
    return answers


def random_choice(questions):
    return random.choice(questions)


def the_final_countdowning(question, player_name):
    counter = 3
    while counter != 0:
        clean()
        print_question(question, player_name)
        if len(str(counter)) == 1:# a ' ' added to the sentence
            print(f'\033[96mThe answer will be revalid in\033[0m \033[3{counter % 7}m {counter}\033[0m \033[96msecond\033[0m')
        else:
            print(f'\033[96mThe answer will be revalid in\033[0m \033[3{counter % 7}m{counter}\033[0m \033[96msecond\033[0m')
        counter -= 1
        time.sleep(1)

def print_question(question, player_name):
    print(f"\n\033[96m{player_name}'s question is:\033[0m\n\n\033[95m{question}\033[0m")


def get_players():
    players = []
    player_input = 'i'
    while player_input != '':
        clean()
        player_input = input('\033[96mPlayer name:\033[0m\n\n')
        if player_input != '':
            players.append(player_input)
    return players


def main():
    question_list = list_maker()
    answer_list = get_answers_list()
    players_list = get_players()
    which_player = 0
    try:
        while True:
            player_name = players_list[which_player % len(players_list)].capitalize()
            question = random_choice(question_list)
            the_final_countdowning(question, player_name)
            clean()
            print_question(question, player_name)
            print(f'\033[96mYour answer is:\033[0m\n\n\033[95m{answer_list[question_list.index(question)]}\033[0m')
            print('\033[5mPress enter\033[0m')
            print('\033[6mPress enter\033[0m')
            input()
    except KeyboardInterrupt:
        clean()
        print('\n\033[94mFUCK YOU TONNY!!!!\033[0m\n')


if __name__ == '__main__':
    main()