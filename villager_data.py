"""Functions to parse a file containing villager data."""

# Open the file
input_file = open("villagers.csv")

def villagers_info(filename):
    """
    Return a list of all the villagers information.

    :param filename: input file as an opened file object data type

    Returns villagers information as a list.
    """
    
    # Moves pointer to first element of the file
    filename.seek(0)           

    # Creates an empty list to store aggregate villagers data
    all_villagers = []

    # Iterate through each line in the file and append each line as an individual villager's info
    for line in filename:
        villager = line.rstrip()
        villager = villager.split("|")
        all_villagers.append(villager)
    
    return all_villagers


def all_species(filename):
    """
    Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    
    species = set()

    all_villagers = villagers_info(filename)

    for villager in all_villagers:
        species.add(villager[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """
    Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers_by_species = []

    all_villagers = villagers_info(filename)

    for villager in all_villagers:
        if search_string == "All":
            villagers_by_species.append(villager[0])
        elif villager[1] == search_string:
            villagers_by_species.append(villager[0])

    return sorted(villagers_by_species)


def all_names_by_hobby(filename):
    """
    Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # Create a list to store all hobbies
    villager_hobbies = []

    # Create a list to store villagers by hobby
    villagers_by_hobby = []

    all_villagers = villagers_info(filename)

    # Identify all unique hobbies and store in all_hobbies
    for villager in all_villagers:
        if villager[3] not in villager_hobbies:
            villager_hobbies.append(villager[3])

    # Group villagers by hobby
    for i, hobby in enumerate(villager_hobbies):
        hobby_group = [villager_hobbies[i]]
        for villager in all_villagers:
            if villager[3] == villager_hobbies[i]:
                hobby_group.append(villager[0])
        villagers_by_hobby.append(hobby_group)

    return villagers_by_hobby


def all_data(filename):
    """
    Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    all_villagers = villagers_info(filename)

    for villager in all_villagers:
        person = (villager[0], villager[1], villager[2], villager[3], villager[4])
        all_data.append(person)

    return all_data


def find_motto(filename, villager_name):
    """
    Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    all_villagers = villagers_info(filename)

    for villager in all_villagers:
        if villager_name == villager[0]:
            return villager[4]


def find_likeminded_villagers(filename, villager_name):
    """
    Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    same_personality = set()
    personality = ""

    all_villagers = villagers_info(filename)

    for villager in all_villagers:
        if villager_name in villager:
            personality = villager[2]
        if villager[2] == personality:
            same_personality.add(villager[0])

    return same_personality


# Close the file
input_file.close()