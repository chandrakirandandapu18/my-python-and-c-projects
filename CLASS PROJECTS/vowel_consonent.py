# while True:
#     letter=input("Enter a Alphabet : ")
#     if ord(letter) <65 or ord(letter)>90 and ord(letter) < 97 or ord(letter)>122:
#         print("You have to give a alphabet..")
#     else:
#         break
# if len(letter)!=1:
#     print("You have to give a single letter ...")
# else:
#     if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O'or letter == 'U' or letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#         print("Given letter is a Vowel..")
#     else:
#         print("Given letter is a consonent....")

n=int(input("Enter a number : "))
result=lambda n:"even" if n%2==0 else "odd"
print(result(n))




