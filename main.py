from constants import WORDS, MAGNITUDE_WORDS

MAX_VALUE = int("9" * 66)


def main() -> None:
    is_running = True

    while is_running:
        input_value = input("Entrez un nombre entier : ")

        if input_value.lower() in ('exit', 'quit', "q"):
            is_running = False
            continue

        try:
            try:
                input_number = int(input_value)
            except:
                print(f"'{input_value}' n'est pas un nombre entier.")
                print()
                continue

            is_negative = input_number < 0
            if is_negative:
                input_number *= -1

            if input_number > MAX_VALUE:
                print("Ce nombre dépasse les limites autorisés.")
                print()
                continue

            magnitudes = group_by_magnitude(input_number)

            result = ""
            length = len(magnitudes)
            for i in reversed(range(length)):
                number = int(magnitudes[i])
                part = convert_to_words(number)

                if number == i == 1:
                    part = MAGNITUDE_WORDS[i]
                elif number == 0 and length > 1:
                    part = ""
                elif i > 0:
                    part += "-" + MAGNITUDE_WORDS[i]

                if part != "":
                    result += ("-" + part) if result != "" else part

            result = result.replace("cents-", "cent-")

            input_value = f"{input_number:,}".replace(",", " ")
            print(f"{input_value} : {'moins ' if is_negative else ''}{result}")
        except Exception as e:
            print(e)

        print()


def group_by_magnitude(num: int) -> list[str]:
    num_str = str(num)
    remainder = len(num_str) % 3
    if remainder != 0:
        num_str = "0" * (3 - remainder) + num_str

    return [num_str[i:i+3] for i in range(0, len(num_str), 3)][::-1]


def convert_to_words(num: int) -> str:
    if not (0 <= num < 1000):
        raise Exception("Erreur : Le nombre doit être compris entre 0 et 999.")

    if num in WORDS:
        return WORDS[num]

    hundred, ten, unit = [int(digit) for digit in group_by_magnitude(num)[0]]
    result = ""

    if hundred == 1:
        result += WORDS[100]
    elif hundred > 1:
        result += WORDS[hundred] + "-" + WORDS[100] + "s"

    if ten != 0 and ten * 10 + unit in WORDS:
        result += ("" if result == "" else "-") + WORDS[ten * 10 + unit]
        return result
    
    if ten == 8:
        result += ("" if result == "" else "-") + WORDS[4] + "-" + WORDS[20] + ("s" if unit == 0 else "")
    elif ten > 0:
        result += ("" if result == "" else "-") + WORDS[ten * 10]

    if unit == 1 and not (ten == 8 or ten == 0):
        result += "-et"

    if unit > 0:
        result += ("" if result == "" else "-") + WORDS[unit]

    return result


if __name__ == "__main__":
    main()
