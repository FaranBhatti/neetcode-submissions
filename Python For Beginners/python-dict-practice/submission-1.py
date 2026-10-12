from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    countLettersDict = {}

    for letter in word:
        if letter in countLettersDict:
            countLettersDict[letter] += 1
        else:
            countLettersDict[letter] = 1

    return countLettersDict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
