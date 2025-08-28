def filter_and_sort_even(numbers):
    return sorted([n for n in numbers if n % 2 == 0])


print(filter_and_sort_even([3, 1, 4, 5, 9, 2, 6]))


def count_character_frequency(text):

    text = text.lower()

    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


# Example calls (testing the function)
print(count_character_frequency("Hello World"))
print(count_character_frequency("Sidhya Robotics"))
print(count_character_frequency("Python Developer"))