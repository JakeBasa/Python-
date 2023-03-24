def is_palindrome(string):
    string = string.lower()
    palindrome = string[::-1].lower()
    result = "Palindrome" if string == palindrome else "Not Palindrome"
    return result
