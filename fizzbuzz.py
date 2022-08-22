for i in range(1, 100):
    result = "Fizz" * bool(i % 3 == 0)
    result += "Buzz" * bool(i % 5 == 0)
    if not result:
        result = i
    print(result)
