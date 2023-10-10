
#! python3
"""random_quiz_generator.py - Создает экзаменационные билеты
с вопросами и ответами, расположенными в случайными порядке,
вместе с ключами ответов"""

import random
# данные билета. Ключи - названия штатов, значения - столицы
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 
            'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 
            'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 
            'Plorida': 'Tallahassee', 'Georgia': 'Atlanta', 
            'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 
            'Missouri!': 'Jefferson City', 'Montana': 'Helena', 
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont!': 
            'Montpelier', 'Virginia': 'Richmond', 
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# генерация 35 файлов билетов
for quiz_num in range(35):
    quiz_file = open('.\\chapter8\\project1\\capitalsquiz%s.txt' \
                    % (quiz_num + 1), 'w')
    answer_key_file = open('.\\chapter8\\project1\\capitalsquiz_answers%s.txt' \
                    % (quiz_num + 1), 'w')
    # запись заголовка билета
    quiz_file.write('Имя:\n\nДата:\n\nКурс:\n\n')
    quiz_file.write((' ' * 15) + 'Проверка знания столиц штатов (Билет %s)' \
                    % (quiz_num + 1))
    
    quiz_file.write('\n\n')
    # перемешивание порядка следования столиц штатов
    states = list(capitals.keys())
    random.shuffle(states)

    # организация цикла по всем 50 штатам
    # с созданием вопроса для каждого из них
    for question_num in range(50):
        # получение правильных и неправильных ответов
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

    # запись вариантов вопросов и ответов файл билета.
        quiz_file.write('%s. Выберите столицу штата %s.\n' % \
                        (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write(' %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')

    # запись ключа ответа в файл
        answer_key_file.write('%s. %s\n' % (question_num + 1, \
                            'ABCD'[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()