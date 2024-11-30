import string

def clean_input(s):
    return ''.join(c.lower() for c in s if c.isalnum())

def is_palindrome(s):
    cleaned = clean_input(s)
    return cleaned == cleaned[::-1]

def main():
    user_input = input("Enter a string or sentence: ")
    if is_palindrome(user_input):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")

if __name__ == "__main__":
    main()
