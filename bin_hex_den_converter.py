def base_to_den(val, base: int):
    val = str(val).upper()
    positional_value = base**(len(val)-1)
    total = 0
    i = 0
    for digit in val:
        total += positional_value * int(
                chr_to_int(val[i]))
        positional_value //= base
        i += 1
    return int(total)

def chr_to_int(char: str):
    try:
        return int(char)
    except ValueError:
        return ord(char) - 55

def den_to_base(num: int, base: int) -> str:
    """Works up to base 36. Over would produce unexpected results. Instead, \
an error is raised"""
    if base > 26:
        raise ValueError("Function can only handle bases under 26. Base given:"
                + str(base))
    elif num < base:
        if base > 10:
            return int_to_hex_chr(num)
        return str(num)

    convert_digit = lambda x: str(x)
    if base > 10:
        convert_digit = int_to_hex_chr

    last_digit = convert_digit(num % base)
    front_digits = den_to_base(num // base, base)

    return front_digits + last_digit

def int_to_hex_chr(num: int) -> str:
    """Returns character corresponding to an int's hex representation.
Int given must be under 26."""
    #26 letters in alphabet - function theoretically works with all bases < 27
    if num < 10:
        return str(num)
    elif num < 26:
        return chr(num + 55) # unicode value of "A" is 65.
    else:
        raise ValueError("Expected int of value under 26. Int of value "
                         + str(num) + " passed.")


def bin_to_den(binary):
    return base_to_den(binary, 2)

def hex_to_den(hexa):
    return base_to_den(hexa, 16)

def den_to_bin(den: int):
    return den_to_base(den, 2)

def den_to_hex(den: int):
    return den_to_base(den, 16)


def base_to_base(val, initial_base, target_base):
    return den_to_base(base_to_den(val, initial_base), target_base)



