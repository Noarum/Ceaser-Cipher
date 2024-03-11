def ceaser_shift():

    # limitation.
    first_char_code1 = ord("A")
    last_char_code1 = ord("z")
    char_range1 = first_char_code1 - last_char_code1 + 1

    # ceaser cipher function.
    # store result.
    result = ""
    while True: 
            user_massage = input("Message to be Encrypted : ")
            while True:
                try:
                    user_shift_key = int(input("Enter Shift Key : "))
                    break
                except ValueError:
                    print("please insert a valid shift key numerical value")
                    continue
            while True:
                # check every character.
                for char in user_massage:
                    # convert character to ASCII code.
                    if char.isalpha():
                        char_code = ord(char)
                        new_char_code = char_code + user_shift_key
                        if new_char_code > last_char_code1:
                            new_char_code -= char_range1
                        if new_char_code < first_char_code1:
                            new_char_code += char_range1
                        if char_code == 90:
                            new_char_code = 65
                        if char_code == 122:
                            new_char_code = 97
                        new_char = chr(new_char_code)
                        result += new_char

                    else:
                        result += char
                break
            print(result)
            result = ''
