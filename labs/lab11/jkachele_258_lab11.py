def count_vowels(s):
    vowelCount = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    try:
        s[0]  # Throws an exception if s isnt a string or empty
        for char in s:
            if not char.isalpha() and char != ' ':
                raise ValueError(
                    "Input string must contain only alphabetic characters")
            if char.lower() in vowels:
                vowelCount += 1
    except TypeError:
        raise Exception("Input should be a string")
    except IndexError:
        raise Exception("Input string cannot be empty")
    else:
        return f"The sentance contains { vowelCount } vowels"


# print(count_vowels("The quick brown fox jumps over the lazy dog"))
# print(count_vowels(123))
# print(count_vowels("221B baker street"))
# print(count_vowels(""))
