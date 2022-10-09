# Купили холодильник,короб которого, со сторонами: X× Y × H. 
# Установить, пройдёт ли он в проем двери с размерами A × B. 
# Составить алгоритм: if else

X = float(input('Enter refrigerator width, meters (Example: 0.595):') or 0.595)
Y = float(input('Enter refrigerator depth, meters (Example: 0.682):') or 0.682)
H = float(input('Enter refrigerator height, meters (Example: 1.86):') or 1.86)
A = float(input('Enter doorway width, meters (Example: 0.7)') or 0.7)
B = float(input('Enter doorway height, meters (Example: 2.3)') or 2.3)

SUCCESS_ANSWER = "You have every chance to move the refrigerator through the door."
FAIL_ANSWER = "Sorry, your refrigerator is too big and don't through the door."

def box_door_inside(X, Y, H, A, B):
    if X < A and Y < B:
        return SUCCESS_ANSWER
    if X < B and Y < A:
        return SUCCESS_ANSWER
    if X < A and H < B:
        return SUCCESS_ANSWER
    if X < B and H < A:
        return SUCCESS_ANSWER
    if Y < A and H < B:
        return SUCCESS_ANSWER
    if Y < B and H < A:
        return SUCCESS_ANSWER
    else:
        return FAIL_ANSWER

print(box_door_inside(X, Y, H, A, B))