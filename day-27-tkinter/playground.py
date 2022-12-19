def add(*args: int) -> int:
    # print(type(args)) # class 'tuple'
    # print(args[0]) # 3
    # print(args[1]) # 5
    sum: int = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 2, 1, 7, 4, 3)) # 31
