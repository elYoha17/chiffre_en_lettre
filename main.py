from constants import words, magnitude_words

max_value = int("9" * 63)

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

            if input_number > max_value:
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
                    part = magnitude_words[i]
                elif number == 0 and length > 1:
                    part = ""
                elif i > 0:
                    part += "-" + magnitude_words[i]

                if part != "":
                    result += ("-" + part) if result != "" else part

            input_value = input_value.replace(",", ".")
            input_value = f"{int(input_value):,}".replace(",", " ")
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
    
    if num in words:
        return words[num]

    hundred, ten, unit = [int(digit) for digit in group_by_magnitude(num)[0]]
    result = ""

    if hundred == 1:
        result += words[100]
    elif hundred > 1:
        result += words[hundred] + "-" + words[100]
        
    if ten != 0 and ten * 10 + unit in words:
        result += ("" if result == "" else "-") + words[ten * 10 + unit]
        return result
    
    if ten > 0:
        result += ("" if result == "" else "-") + words[ten * 10]
        
    if unit == 1 and not (ten == 8 or ten == 0):
        result += "-et"

    if unit > 0:
        result += ("" if result == "" else "-") + words[unit]

    return result
    
if __name__ == "__main__":
    main()