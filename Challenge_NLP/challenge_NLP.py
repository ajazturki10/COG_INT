import re
import pandas as pd




def parse_file(text):
    curr_pattern = "(?:[\₹\$\€]{1}[,\d]+.?\d*)"

    vow = "aeiou"
    res = []
    for substring in text.split():
        flag = (substring.lower()[0] in vow) and (len(substring)==4)

        if flag:
            res.append(substring)

    date_pattern = '\d{2}[/-]\d{1,2}[/-]\d{2,4}'

    order_pattern = r'\w+(?:rst|ond|ird|nth)'

    order_str = re.findall(order_pattern, text)

    print("Cardinality: ", len(set(order_str)))
    print(re.findall(curr_pattern, text))
    print(str(res))
    print(re.findall(date_pattern, text))
    print(re.findall(order_pattern, text))

if __name__ == '__main__':
    test_1 = "C:/Users/ijazt/Desktop/test_1.txt"
    test_2 = "C:/Users/ijazt/Desktop/test_2.txt"
    test_3 = "C:/Users/ijazt/Desktop/test_3.txt"
    test_4 = "C:/Users/ijazt/Desktop/test_4.txt"
    test_5 = "C:/Users/ijazt/Desktop/test_5.txt"

    with open(test_5, encoding='utf-8') as f:
        file = f.readline()
    
    parse_file(file)
