def float_to_octal(n, precision=10):
    integer_part = int(n)
    fractional_part = n - integer_part

    # Partie entière
    int_octal = oct(integer_part)[2:]

    # Partie fractionnaire
    frac_octal = ""
    for _ in range(precision):
        fractional_part *= 8
        digit = int(fractional_part)
        frac_octal += str(digit)
        fractional_part -= digit
        
        if fractional_part == 0:
            break

    return int_octal + "." + frac_octal if frac_octal else int_octal


print(float_to_octal(5*0.75))  # 52.5