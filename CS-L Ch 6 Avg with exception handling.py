def read_numbers(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = float(line.strip())
                numbers.append(number)
        return numbers
    except FileNotFoundError:
        print("Error: File not found")
        return None
    except ValueError:
        print("Error: Invalid value in file")
        return None

def calculate_average(numbers):
    if numbers:
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average
    else:
        return None

def print_average(average):
    if average is not None:
        print("Average:", average)
    else:
        print("Error: Could not calculate average")

def main():

    filename = input("Enter filename: ")
    numbers = read_numbers(filename)
    average = calculate_average(numbers)
    print_average(average)

if __name__ == '__main__':
    main()
