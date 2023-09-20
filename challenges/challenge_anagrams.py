def is_anagram(first_string, second_string):
    string1 = first_string.lower()
    string2 = second_string.lower()

    if first_string:
        string1 = merge_sort_word(string1)

    if second_string:
        string2 = merge_sort_word(string2)

    is_anagram = string1 == string2

    if first_string == '' and second_string == '':
        is_anagram = False

    return (string1, string2, is_anagram)


def merge_sort_word(word):
    if len(word) <= 1:
        return word

    middle = len(word) // 2
    left = word[:middle]
    right = word[middle:]

    left = merge_sort_word(left)
    right = merge_sort_word(right)

    return merge_words(left, right)


def merge_words(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return "".join(result)


is_anagram("cadb", "badc")
