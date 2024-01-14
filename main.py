
def add(number_a: int | float, number_b: int | float) -> int | float:
    return number_a + number_b


if __name__ == '__main__':
    numbers: list[int] = [1, 2]
    print('numberA:', numbers[0])
    print('numberB:', numbers[1])
    print(f'{numbers[0]} + {numbers[1]} = {add(numbers[0], numbers[1])}')
