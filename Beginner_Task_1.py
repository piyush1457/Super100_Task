# Beginner_Task1
def anagrams(str1,str2):
    return sorted(str1.lower())==sorted(str2.lower())
print(anagrams("top","pot"))
print(anagrams("hello","world"))
