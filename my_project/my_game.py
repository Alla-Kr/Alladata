"""Игра угадай число"""
import numpy as np
def random_predict(number: int = 1) -> int:
    """Угадываем число
    Args:
        number (int, optional): _Загаданное число_. Defaults to 1.
    Returns:
        int: с какой попытки угадали
    """ 
    np.random.seed(1) # фиксируем загаданное число    
    number = np.random.randint(1, 101) # загадываем число
    count = 0  # задаем счетчик
    min_num = 1
    max_num = 100

    while True:
        count += 1
        print('Число:', number, '---', 'Попытка:', count)

        predict_num = int(( min_num + max_num) / 2)  # загадываем число как среднее между минимальным и максимальным и отбрасываем дробную часть

        if predict_num > number:
            max_num = predict_num
        elif predict_num < number:
            min_num = predict_num
        else:
            print(f'Алгоритм рассчитал число {number} за {count} попыток')
            break
    return count
random_predict()