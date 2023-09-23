def find_maxx(numbers):
    
    maxx = numbers[0]
    for number in numbers:
        if number > maxx:
            maxx = number
    return maxx


