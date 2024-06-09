scores = [90, 85, 77, 65, 97, 88, 94]
def is_A_student(score):
    return score >= 75
print(list(filter(is_A_student, scores)))

# palindrome
words = ["level", "test", "radar", "hello", "world"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)