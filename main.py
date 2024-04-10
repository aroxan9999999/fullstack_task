def unique_elements(numbers):  # 1
    return list(set(numbers))


def prime_numbers(minimum, maximum):  # 2
    primes = []
    for possiblePrime in range(minimum, maximum + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes


class Point:  # 3
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def sort_strings_by_length(strings):  # 4
    sorted_strings = sorted(strings, key=len)
    return sorted_strings[::-1]


strings = ["apple", "banana", "cherry", "blueberry", "grapefruit"]
print(sort_strings_by_length(strings))
