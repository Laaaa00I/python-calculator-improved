from config.config import CONVERTER_OPERATIONS
from config.lists import converter_operations_list
from utils import get_float, continue_cycle


while True:

    angle_to_convert = get_float("Enter an angle: ")
    print("Choose conversation way:")
    print(CONVERTER_OPERATIONS)

    while True:
        op = input(">> ").lower()
        if op in converter_operations_list: break
        else: print("Invalid operation!")
    #^^^ Operations selection
    #Ru: Выбор операции

    converted_angle = converter_operations_list[op](angle_to_convert)

    print(f"{angle_to_convert} rad = {converted_angle}°")

    if angle_to_convert < 0:
        print("Note: negative angle!")
    elif angle_to_convert == 0:
        print("Note: zero angle!")

    continue_cycle()
    #^^^ 'Continue?' cycle
    #Ru: Цикл 'продолжить?'
#^^^ Main convertion cycle
#Ru: Основной цикл конвертаций