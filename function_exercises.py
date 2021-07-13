
def is_two(n):
    if n == 2 or '2':
        return True
    else:
        return False


def is_vowel(letter):
    if letter in ('a', 'e', 'i', 'o', 'u'):
        return True
    else: 
        return False


def is_consonant(letter):
    if letter not in ('a', 'e', 'i', 'o', 'u'):
        return True
    else: 
        return False       


def proper_noun(noun):
    result = noun.capitalize()
    return result

proper_noun('brooke')

total_bill = 50
desired_tip = .15

def calculate_tip(total_bill, desired_tip):
    return total_bill * desired_tip

original_price = 150
discount = 50

def apply_discount(original_price, discount):
    return original_price - (original_price * (discount/100))

def handle_commas(number):
    return int(number.replace(',',''))

def get_letter_grade(grade):
    if grade <= 69:
        return 'F'
    elif grade <= 74 and grade > 69:
        return 'D'
    elif grade <= 79 and grade > 74:
        return 'C'
    elif grade <= 89 and grade > 79:
        return 'B'
    elif grade <= 100 and grade > 89:
        return 'A'
    else:
        return False

def remove_vowels(word):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in word if letter.lower() not in vowels]
    result = ''.join(result)
    return result



