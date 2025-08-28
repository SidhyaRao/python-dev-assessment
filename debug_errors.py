def calculate_average(numbers):
    try:
        if len(numbers) == 0:
            return 0
        total = 0
        for i in range(len(numbers)):
            total += numbers[1]
    except Exception as e:
        print(f"Error calculating average: {e}")
        return None
    # Logical Error: Incorrect average calculation for empty list
    return total / len(numbers)


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(" Error: Index is out of bounds.")
        return None
    except TypeError:
        print(
            " Error: Invalid type. my_list must be a list and index must be an integer."
        )
        return None


datal = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # This will cause an error
print(f"Average of datal: {calculate_average(datal)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

numbers = [10, 20, 30]
print(get_list_element(numbers, 1))
print(get_list_element(numbers, 5))
print(get_list_element("hello", 2))
print(get_list_element(numbers, "a"))