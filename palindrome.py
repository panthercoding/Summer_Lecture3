import sys

def extractCharacters(string):
  s = ""
  for char in string:
    if (char.isalpha() == True):
      s += char 
  return(s)

def isPalindromeIterative(string):
  string = extractCharacters(string)
  for i in range(len(string)):
    #checks characters on opposite ends of the string
    if (string[i] != string[len(string) - 1 - i]):
      return(False)
  return(True)

#recursive method
def isPalindrome(string):
  if (len(string) <= 1):
    return(True)
  else:
    firstChar = string[0]
    middleString = string[1:len(string)-1]
    lastChar = string[len(string) - 1]
    """checks if the first and last characters match
    and the middle string is a palindrome """
    return (firstChar == lastChar) and isPalindrome(middleString)

print(isPalindrome(extractCharacters(sys.argv[1])))
  