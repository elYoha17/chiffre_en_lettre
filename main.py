from constants import words, magnitude_words

def main() -> None:
    is_running = True
    
    while is_running:
        input_value = input("Entrez un nombre entier : ")

        if input_value.lower() in ('exit', 'quit', "q"):
            is_running = False
            continue

        try:
            magnitudes = group_by_magnitude(int(input_value))

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
            print(f"{input_value} : {result}")
        except:
            print("Veuillez entrer un nombre entier s'il vous plaît.")

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
    num = ""

    if hundred == 1:
        num += words[100]
    elif hundred > 1:
        num += words[hundred] + "-" + words[100]
        
    if ten != 0 and ten * 10 + unit in words:
        num += ("" if num == "" else "-") + words[ten * 10 + unit]
        return num
    
    if ten > 0:
        num += ("" if num == "" else "-") + words[ten * 10]
        
    if unit == 1 and not (ten == 8 or ten == 0):
        num += "-et"

    if unit > 0:
        num += ("" if num == "" else "-") + words[unit]

    return num
    
if __name__ == "__main__":
    main()