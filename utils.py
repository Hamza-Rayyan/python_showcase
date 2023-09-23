def find_max(numbers):
    
    maxx = numbers[0]
    for number in numbers:
        if number > maxx:
            maxx = number
    return maxx


