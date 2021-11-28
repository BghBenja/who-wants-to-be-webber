import random
import os
import time
import playsound
from gtts import gTTS
FILE = 'module_progbasics.md'

def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def list_maker():
    list_of_questions = []
    with open(FILE, 'r') as raw_txt:
        for line in raw_txt:
            if '####' in line:
                list_of_questions.append(line[5:])
    return list_of_questions


def get_answers_list():
    answers = []
    with open(FILE) as raw_txt:
        answer = ''
        for line in raw_txt:
            if "#" not in line and line != '\n':
                answer += line
            if "#" in line:
                if len(answer) > 0:
                    answers.append(answer)
                    answer = ''
        answers.append(answer)
    return answers


def delete_old_used_question(used_questions, questions):
    if len(used_questions) > len(questions) // 2:
        del used_questions[0]


def random_choice(questions, used_questions):
    random_question = random.choice(questions)
    while random_question in used_questions:
        random_question = random.choice(questions)
    return random_question


def the_final_countdowning(question, player_name):
    counter = 20
    while counter != 0:
        clean()
        print_question(question, player_name)
        if len(str(counter)) == 1:# a ' ' added to the sentence
            print(f'\033[96mThe answer can be revalid in\033[0m \033[3{counter % 7}m {counter}\033[0m \033[96msecond\033[0m')
        else:
            print(f'\033[96mThe answer can be revalid in\033[0m \033[3{counter % 7}m{counter}\033[0m \033[96msecond\033[0m')
        counter -= 1
        time.sleep(1)


def print_question(question, player_name):
    print(f"\n\033[96m{player_name}'s question is:\033[0m\n\n\033[95m{question}\033[0m")


def get_players():
    players = []
    player_input = 'i'
    while player_input != '':
        clean()
        for color_code, player in enumerate(players):
            print(f'\033[3{color_code % 6 + 1}m{player.capitalize()}',end = ', ')
        player_input = input('\033[96m\nAdd player or press enter:\033[0m\n\n')
        if player_input != '':
            players.append(player_input)
    return players


def print_answer(user_choice, question, player_name, answer_list, question_list):
    if user_choice.lower() == 'y':
        clean()
        print_question(question, player_name)
        print(f'\033[96mYour answer is:\033[0m\n\n\033[95m{answer_list[question_list.index(question)]}\033[0m')
        speak(f'Your answer is {answer_list[question_list.index(question)]}')
    else:
        clean()
        print_question(question, player_name)
        print('\033[96mOkay, you know.\033[0m')
        time.sleep(1)


def speak(text):
    tts= gTTS(text= text, lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def main():
    question_list = list_maker()
    answer_list = get_answers_list()
    players_list = get_players()
    which_player = 0
    used_questions = []
    try:
        while True:
            delete_old_used_question(used_questions, question_list)
            player_name = players_list[which_player % len(players_list)].capitalize()
            question = random_choice(question_list, used_questions)
            the_final_countdowning(question, player_name)
            clean()
            print_question(question, player_name)
            user_choice = input('\033[96mDo you need the answer y/n:\033[0m\n\n')
            print_answer(user_choice, question, player_name, answer_list, question_list)
            if user_choice == 'y':
                print('\033[5mPress enter\033[0m')
                input()
            which_player += 1
            used_questions.append(question)
    except KeyboardInterrupt:
        clean()
        print('\n\033[94m**** YOU TONNY!!!!\033[0m\n')


if __name__ == '__main__':
    main()