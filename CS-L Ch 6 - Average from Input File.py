with open('numbers.txt', 'r') as file:
    numbers = []
    total = 0
    count = 0
    for line in file:
        number = float(line.strip())
        count += 1
        total += number
        numbers.append(number)
        print('I read in', count, 'number(s). Current number is:', number, 'Total is:', total)


average = total / count
print('Average: ', average)
