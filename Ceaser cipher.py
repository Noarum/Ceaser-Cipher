def ceaser_shift():
    result = ""
    while True: 
        user_message = input("Message to be Encrypted : ")
        while True:
            try:
                user_shift_key = int(input("Enter Shift Key : "))
                break
            except ValueError:
                print("please insert a valid shift key numerical value")
        
        for char in user_message:
            if char.isupper():
                result += chr((ord(char) - ord('A') + user_shift_key) % 26 + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') + user_shift_key) % 26 + ord('a'))
            else:
                result += char
        
        print(result)
        result = ''

ceaser_shift()
