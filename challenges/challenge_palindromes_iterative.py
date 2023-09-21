def is_palindrome_iterative(word):
    if word == '':
        return False

    for i in range(len(word) // 2):
        last_index = word[-i - 1]
        if word[i] != last_index:
            return False

    return True
