def validate_integer_list(input_string):
    parts = input_string.split()

    if not all(p.lstrip("-").isdigit() for p in parts):
        return None

    return list({int(x) for x in parts})


def recursive_sum(data):
    return 0 if not data else data[0] + recursive_sum(data[1:])


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)