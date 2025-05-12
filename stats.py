def count_words(text):
        words = text.split()
        return len(words)

def count_characters(text):
    no_of_characters = {}
    characters = text.lower()
    for char in characters:
        if char in "abcdefghijklmnopqrstuvwxyz":
            if char in no_of_characters:
                no_of_characters[char] += 1
            else:
                no_of_characters[char] = 1
    return no_of_characters

def sort_list(no_of_characters):
    char_list = []

    for char, count in no_of_characters.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    def sort_on(no_of_characters):
        return no_of_characters["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list 
