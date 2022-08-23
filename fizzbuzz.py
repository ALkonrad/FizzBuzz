full_result = ''
for i in range(1, 101):
    result = "Fizz" * bool(i % 3 == 0)
    result += "Buzz" * bool(i % 5 == 0)
    if not result:
        result = str(i)
    full_result += result
print(full_result)
