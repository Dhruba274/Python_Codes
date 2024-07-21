def int_to_words(num):
    ones = ['','one','two','three','four','five','six','seven','eight','nine','ten',
             'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    if num < 20:
        return ones[num]
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else '-' + ones[num % 10])
    elif num < 1000:
        return ones[num // 100] + ' hundred' + ('' if num % 100 == 0 else ' and ' + int_to_words(num % 100))
    elif num < 1000000:
        return int_to_words(num // 1000) + ' thousand' + ('' if num % 1000 == 0 else ' ' + int_to_words(num % 1000))
    return None

digit = int(input("Enter a digit: "))
print(int_to_words(digit))
