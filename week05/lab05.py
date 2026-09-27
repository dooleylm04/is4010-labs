
def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid.

    Args:
        users: A list of dictionaries, each representing a user. A user
            may have an "age" key whose value should be an int or float.

    Returns:
        The average of all valid numeric ages as a float. Users with a
        missing age or a non-numeric age (e.g. a string or None) are
        ignored. Returns 0.0 if there are no valid ages.
    """
    valid_ages = []
    for user in users:
        age = user.get("age")
        if isinstance(age, (int, float)) and not isinstance(age, bool):
            valid_ages.append(age)

    if not valid_ages:
        return 0.0
    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return email addresses belonging to active users.

    Args:
        users: A list of dictionaries, each representing a user. A user
            may have an "is_active" key and an "email" key.

    Returns:
        A list of email strings for users whose "is_active" value is
        truthy and who have an "email" key. Returns an empty list if
        no such users exist.
    """
    emails = []
    for user in users:
        if user.get("is_active") and "email" in user:
            emails.append(user["email"])
    return emails