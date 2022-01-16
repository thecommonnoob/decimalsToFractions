number = input('Input a decimal number with the repeating digits in between brackets: ')


def parse_input(input):
    # gets the numbers inside of the brackets
    repeating_number = input.split('(', 1)[1].split(')')[0]

    # removes the brackets from the original number
    original_number = input.replace('(', '')
    original_number = original_number.replace(')', '')
    return (repeating_number, original_number)


def do_math(repeating_number, original_number):
    # does like thing idk forgot what i did
    # well uhm does a thing im trying to explain what it does to myself
    # i cant do it
    # future me can totally read the code and know exactly what it does
    # wow who would have thought i cant read or understand it
    # it works tho so if it aint broke dont fix it that totally wont cause any problems
    multiplied_number = original_number
    decimal_thing = repeating_number
    multiplied_by = 1
    for _ in range(len(repeating_number)):
        multiplied_number = float(multiplied_number) * 10
        decimal_thing = float(decimal_thing) / 10
        multiplied_by *= 10

    # not at all useless

    multiplied_number += decimal_thing

    # uh do the minus thing

    multiplied_number -= decimal_thing
    multiplied_by -= 1

    # fractions woo
    # no longer fractions its somewhere else now

    top_thingy = int(multiplied_number)
    bottom_thingy = int(multiplied_by)

    return (simplify_fraction(top_thingy, bottom_thingy))


def simplify_fraction(top_thingy, bottom_thingy):
    is_divisible_by = 1

    # does stuff idk i forgot if i even programmed this part
    for i in range(min(abs(top_thingy), abs(bottom_thingy)), 1, -1):
        if top_thingy % i == 0 and bottom_thingy % i == 0:
            is_divisible_by = i
            break

    top_thingy /= is_divisible_by
    bottom_thingy /= is_divisible_by
    return (top_thingy, bottom_thingy)


# somehow it works
# idk how it just does
# for now
print(do_math(parse_input(number)[0], parse_input(number)[1]))
