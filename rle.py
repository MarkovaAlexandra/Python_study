# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc



def rle_code(text):
    if text.isalpha():
        etalon = text[0]
        count = 0
        result = ''
        pre_result = ''
        for char in text:
            if char != etalon:
                pre_result = str(count) + etalon
                etalon = char
                result = result + pre_result
                count = 1
            
            else:
                count +=1
        result=result + str(count) + etalon

    if not text.isalpha():
        result = ''
        for char in text:
            if char.isdigit():
                count = int(char)
            else:
                result = result + char*count
        

    return result
# text = '3g2r5f1g2w'
text = open('digit_text.txt','r')
my_string = text.read()
encode = rle_code(my_string)
print(encode)

        

