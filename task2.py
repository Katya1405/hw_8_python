# Напишите функцию encrypt_caesar(msg, shift)

def encrypt_caesar(msg, shift):
    result = ""
    for i in msg:
        try:  
            current_index = alphabet.index(i)
            if current_index + shift > len(alphabet):
                new_index = current_index + shift - len(alphabet)
            else:
                new_index = current_index + shift
            result += alphabet[new_index]
        except ValueError:
                result += i
    return result

alphabet = [
    "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
msg = input('Введите сообщение для шифровки: ')
print(encrypt_caesar(msg, 3))

