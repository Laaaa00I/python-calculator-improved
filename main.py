from Operations import TrigonometricOperations, StandardOperations
from config.config import STANDARD_OPERATIONS, TRIGONOMETRIC_OPERATIONS, STANDARD_MODE, TRIGONOMETRIC_MODE
from config.lists import standard_operations_list, trigonometric_operations_list
from utils import get_float, simplify, continue_cycle


while True:

    is_trigonometric = False
    print("Select calculation mode:"
          "\n1. Standard"
          "\n2. Trigonometric")

    while True:
        mode = input(">> ").lower()
        if mode in STANDARD_MODE:
            x = get_float("Enter first number: ")
            y = get_float("Enter second number: ")
            obj = StandardOperations(x, y)
            break
        if mode in TRIGONOMETRIC_MODE:
            is_trigonometric = True
            x = get_float("Enter number: ")
            obj = TrigonometricOperations(x)
            break
        print("Invalid input!")
    #^^^ Mode selection
    #Ru: Выбор режима

    if mode in STANDARD_MODE:
        print(STANDARD_OPERATIONS)
    else:
        print(TRIGONOMETRIC_OPERATIONS)
    #^^^ Menu print
    #Ru: Вывод меню

    while True:

        while True:
            op = input("Choose operation: ").lower()
            if op in standard_operations_list or op in trigonometric_operations_list: break
            print("Invalid operation!")
        #^^^ Operation selection
        #Ru: Выбор операции

        try:
            if is_trigonometric:
                res = trigonometric_operations_list[op](obj)
            else:
                res = standard_operations_list[op](obj)
            res = simplify(res)
            print("=" * 30)
            print(f"Result: {res}")
            if is_trigonometric:
                print("Note: trigonometric mode uses and calculates radians!")
            print("=" * 30)
            break
        except ZeroDivisionError as e: print(f"Error: {e}")
        except ValueError as e: print(f"Error: {e}")
        #^^^ Try & Except — tries to output result, otherwise shows error
        #Ru: Try & Except — пытается вывести результат, иначе показывает ошибку
    #^^^ Contains operation selection & result/error display
    #Ru: Содержит выбор операции и отображение результата/ошибки

    continue_cycle()
    #^^^ 'Continue?' cycle
    #Ru: Цикл 'продолжить?'
#^^^ Main calculation cycle
#Ru: Основной цикл калькуляций
