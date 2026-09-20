def find_common_elements(list1, list2):
    """Return a list of values present in both input lists."""
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common


def find_user_by_name(users, name):
    """Return the matching user dictionary, or None when no user matches."""
    for user in users:
        if user["name"] == name:
            return user
    return None


def get_list_of_even_numbers(numbers):
    """Return the even integers in their original order."""
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens