def remove_fourth_character(word: str) -> str:
    new_str = ""
    for char in range(len(word)):
        if char == 3:
            continue
        else:
            new_str += word[char]
    
    return new_str


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
