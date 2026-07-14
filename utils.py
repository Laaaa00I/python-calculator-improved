from config.config import YES_ANSWERS, NO_ANSWERS
import math


def get_float(prompt):
    """Returns float value

    Возвращает числовое значение с плавающей точкой"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a float!")

def continue_cycle():
    """'Continue?' cycle

    Цикл 'продолжить?'"""
    while True:
        again = input("Would you like to continue?"
                      "\n1. Yes"
                      "\n2. No"
                      "\n").lower()
        if again in YES_ANSWERS:
            break
        elif again in NO_ANSWERS:
            print("Goodbye!")
            exit()
        else:
            print("Invalid input!")

def simplify(val):
    """Simplifies value (example: 1.0 -> 1)

    Упрощает значение (пример: 1.0 -> 1)"""
    return int(val) if isinstance(val, float) and val.is_integer() else val


def radians_to_degrees(val):
    """Converts radians to degrees

    Конвертирует радианы в градусы"""
    return val * 180 / math.pi

def degrees_to_radians(val):
    """Converts degrees to radians

    Конвертирует градусы в радианы"""
    return val * math.pi / 180