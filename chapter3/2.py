import random
secret_number = random.randint(1, 20)
print('Мною задумано число в интервале от 1 до 29. Попробуйте его угадать')

for guesses_taken in range(1, 7):
    print('Ваш вариант')
    guess = int(input())

    if guess < secret_number:
        print('Предложенное число меньше задуманного') 
    elif guess > secret_number:
         print('Предложенное число больше задуманного')   
    else:
        break

if guess == secret_number:
    print('МОЛОДЕЦ!' + str(guesses_taken))    
else:
    print('нет! было задумано число' + str(secret_number))