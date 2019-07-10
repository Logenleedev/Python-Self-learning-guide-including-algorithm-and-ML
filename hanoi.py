# How many steps should it take to finish a hanoi problem?


def hanoi(Layer):
    if Layer == 0:
        return 0
    else:
        return hanoi(Layer-1) + 1 + hanoi(Layer-1)
print(hanoi(6))