import random
import os


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


def random_choice(questions):
    return random.choice(questions)


def main():
    question_list = list_maker()
    try:
        while True:
            question = random_choice(question_list)
            clean()
            print(f'\nYour question is:\n\n{question}')
            input('Press enter')
    except KeyboardInterrupt:
        clean()
        print('\nFUCK YOU TONNY!!!!\n')


if __name__ == '__main__':
    main()