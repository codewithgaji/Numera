import time

# def type_text(text, delay = 0.06):
#     for char in (text):
#         print(char, end = "", flush = True)
#         time.sleep(delay)
#     print()

# CHANGING THE TERMINAL BASED APP TO DJANGO BASED APP
from django.http import JsonResponse # To give a Json response

from django.http import JsonResponse

def word_to_digits(word):
    # Mapping for base numbers
    base_num = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # Mapping for teen numbers
    teens = {
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    }

    # Mapping for tens numbers
    tens = {
        'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
    }

    # Multipliers for larger numbers
    hundreds = {'hundred': 100}
    thousands = {'thousand': 1000}
    millions = {'million': 1000000}
    billions = {'billion': 1000000000}
    trillions = {'trillion': 1000000000000}

    # Split the input word into parts
    word_parts = word.split()
    total = 0
    current_value = 0

    for part in word_parts:
        # Handle base numbers (0-9)
        if part in base_num:
            current_value += base_num[part]
        
        # Handle teen numbers (11-19)
        elif part in teens:
            current_value += teens[part]
        
        # Handle tens (10, 20, 30, ...)
        elif part in tens:
            current_value += tens[part]
        
        # Handle hundreds (e.g., 200, 300, ...)
        elif part in hundreds:
            current_value *= hundreds[part]
        
        # Handle thousands (e.g., 1000, 2000, ...)
        elif part in thousands:
            total += current_value * thousands[part]
            current_value = 0
        
        # Handle millions (e.g., 1 million, 2 million, ...)
        elif part in millions:
            total += current_value * millions[part]
            current_value = 0
        
        # Handle billions (e.g., 1 billion, 2 billion, ...)
        elif part in billions:
            total += current_value * billions[part]
            current_value = 0
        
        # Handle trillions (e.g., 1 trillion, 2 trillion, ...)
        elif part in trillions:
            total += current_value * trillions[part]
            current_value = 0
        
        # If the part is not recognized, return an error
        else:
            return JsonResponse({'error': f"unknown word {part}"}, status=400)
    
    # After processing all parts, add any remaining value in current_value
    total += current_value

    # Return the total with commas for better readability
    return f"{total:,}"
