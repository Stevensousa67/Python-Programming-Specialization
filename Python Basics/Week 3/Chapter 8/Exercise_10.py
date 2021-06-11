# Get the user to enter some text and print out True if it’s a palindrome, False otherwise. (Hint: Start by reversing
# the input string, and then use the == operator to compare two values to see if they are the same)

text = input("Enter a text to check if it is a palindrome: ")
reversed = text[::-1]

if reversed == text:
    print(True)
else:
    print(False)
