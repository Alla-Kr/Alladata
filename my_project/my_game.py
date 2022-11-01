"""Игра угадай число"""
import numpy as np
def random_predict(number: int = 1) -> int:
    """Угадываем число

    Args:
        number (int, optional): _Загаданное число_. Defaults to 1.

    Returns:
        int: с какой попытки угадали
    """ 
    np.random.seed(1)    
    number = np.random.randint(1, 101) # загадываем число
    count = 0 # количество попыток
    
    print('Компьютер загадал число, Вам надо отгадать его за менее чем 20 попыток')

    for i in range(1, 21):
        choice = int(input("Введите число: "))
        if choice > number:
            print("Загаданное число меньше")
        elif choice < number:
            print("Загаданное число больше")
        else:
            print(f"Вы угадали число с {i} - ой попытки")
            break
        count += 1
    
    if count >= 20:
        print(f"Вы исчерпали все попытки, было загадано число {number}")
    return(number) 

print(f'Загаданное число отгадано: {random_predict()}')
    