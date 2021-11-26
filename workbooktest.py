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


def the_final_countdowning(question):
    counter = 30
    while counter != 0:
        clean()
        print_question(question)
        print(f'\033[91mThe answer will be revaild in\033[0m \033[9{counter % 7}m{counter}\033[0m \033[91msecond\033[0m')
        counter -= 1
        time.sleep(1)

def print_question(question):
    print(f'\n\033[94mYour question is:\033[0m\n\n\033[95m{question}\033[0m')

def main():
    question_list = list_maker()
    answer_list = get_answers_list()
    try:
        while True:
            question = random_choice(question_list)
            the_final_countdowning(question)
            clean()
            print_question(question)
            print(f'\033[94mYour answer is:\033[0m\n\n\033[95m{answer_list[question_list.index(question)]}\033[0m')
            input('\033[91mPress enter\033[0m')
    except KeyboardInterrupt:
        clean()
        print('\n\033[96mFUCK YOU TONNY!!!!\033[0m\n')


if __name__ == '__main__':
    main()