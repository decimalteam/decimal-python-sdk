import locale


def number_format(num, places=0):
    return locale.format_string("%.*f", (places, num), True)


def get_amount_uni(amount, reverse = False):
    exp = 18
    if reverse:
        exp = -18
    numb = amount * pow(10, exp)
    prepared_num = number_format(numb, 0)
    return prepared_num