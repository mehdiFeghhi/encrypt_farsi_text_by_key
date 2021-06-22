# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

def main(input,key,item):

    if item == '1':

        array = make_text_to_ord_array(input)
        result = encrypt_by_key(array,make_text_to_ord_array(key))
        output = make_ord_to_text_chat(result)
        open("writeFile.txt","w").write(output)

    else :
        array = make_text_to_ord_array(input)
        result = decrypt_by_key(array,make_text_to_ord_array(key))
        output = make_ord_to_text_chat(result)
        open("writeFile.txt","w").write(output)

def make_text_to_ord_array(input):
    array_ord = []
    for i in input:
        array_ord.append(ord(i))
    return  array_ord

def encrypt_by_key(text_array_ord ,key_array_ord):
    size = len(key_array_ord)
    pointer = 0
    result = []
    for i in text_array_ord:
        get = (i ^ key_array_ord[pointer % size])-1515
        if chr(i) != ' ' and (get >= 65 and get <= 120  and '`'!= chr(get)):
                result.append(get)
        else:
                result.append(i)


        pointer += 1

    return result


def decrypt_by_key(text_array_ord , key_array_ord):
    size = len(key_array_ord)
    pointer = 0
    result = []
    for i in text_array_ord:
       if (i >= 65 and i <= 120 and '`'!= chr(i)):
           result.append((i + 1515) ^ key_array_ord[pointer % size])
       else:
           result.append(i)
       pointer += 1



    return result



def make_ord_to_text_chat(array_ord):

    s = ''
    for i in array_ord:
            s += chr(i)

    print(s)
    return s



if __name__ == '__main__':
    key = input("key :")
    item = input("item  encrypt(1)/decrypt(2): ")
    text = open("readFile.txt","r").read()
    print(text)
    main(text,key,item)
