import string

def is_palindrome(phrase):
  prcsd_text = phrase.strip().lower()
  prcsd_text = [char for char in prcsd_text if str.isalnum(char)]
  prcsd_text = ''.join(prcsd_text)
  return prcsd_text == prcsd_text[::-1]

print(is_palindrome('hello world'))  # false
print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true