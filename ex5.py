def perform_cal(first_operand, second_operand, operator):
    if operator == 'add':
        return first_operand + second_operand
    elif operator == 'subtract':
        return first_operand - second_operand
    elif operator == 'multiply':
        return first_operand * second_operand
    elif operator == 'divide':
        if second_operand == 0:
            return "Error!"
        else:
            return first_operand / second_operand
    else:
        return "Error!"

print(perform_cal(2, 2, 'add'))