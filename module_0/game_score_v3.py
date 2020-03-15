import numpy as np

def game_core_v3(number):
    count = 0
    start = 1 #Начало диапазона
    end = 100 #Конец дапазона
    number = np.random.randint(start,end) 
    predict = 0 
    while True:
        count += 1
        predict = (start+end)//2 # Уменьшаем диапазон поиска вдвое
        if number == predict: 
            break
        elif number > predict:
            start = predict
        elif number < predict:
            end = predict
    return(count) # выход из цикла, если угадали
    print (f"Вы угадали число {number} за {count} попыток.")
score_game(game_core_v3)