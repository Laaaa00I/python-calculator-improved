from Operations import StandardOperations, TrigonometricOperations
from utils import radians_to_degrees, degrees_to_radians

standard_operations_list = {
    **dict.fromkeys(["1", "sum", "сумма", "сложение", "плюс", "+"], StandardOperations.sum),
    **dict.fromkeys(["2", "sub", "subtract", "отнять", "вычесть", "-"], StandardOperations.sub),
    **dict.fromkeys(["3", "mult", "multiply", "умножить", "произведение", "*"], StandardOperations.mul),
    **dict.fromkeys(["4", "div", "division", "разделить", "деление", "/"], StandardOperations.div),
    **dict.fromkeys(["5", "pow", "exponent", "степень", "возвести", "^"], StandardOperations.pow),
    **dict.fromkeys(["6", "root", "корень", "извлечь", "радикал", "√"], StandardOperations.root)
}
trigonometric_operations_list = {
    **dict.fromkeys(["1", "sin", "sine", "синус"], TrigonometricOperations.sin),
    **dict.fromkeys(["2", "cos", "cosine", "косинус"], TrigonometricOperations.cos),
    **dict.fromkeys(["3", "tan", "tangent", "tg", "тангенс"], TrigonometricOperations.tan),
    **dict.fromkeys(["4", "cot", "cotangent", "ctg", "котангенс"], TrigonometricOperations.cot),
    **dict.fromkeys(["5", "sec", "секас", "секущая"], TrigonometricOperations.sec),
    **dict.fromkeys(["6", "cosec", "косеканс"], TrigonometricOperations.cosec)
}
#^^^ Standard and trigonometric operations dictionaries
#Ru: Словари стандартных и тригонометрических операций

converter_operations_list = {
    **dict.fromkeys(["1", "radians to degrees", "радианты в градусы", "рвг", "rtd"], radians_to_degrees),
    **dict.fromkeys(["2", "degrees to radians", "градусы в радианты", "гвр", "dtr"], degrees_to_radians)
}
#^^^ Converter dictionary
#Ru: Словарь конвертера