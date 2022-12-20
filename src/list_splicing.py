"""
CSAPX Project One: Movies
list_splicing.py

Functions for splicing sorted lists by value.

Author: RIT CS
Author: Adrian Marcellus
"""


def list_of_runtime(commands: list, movies_by_type: list) -> list:
    """
    splices a list of type into a list of type and specified runtime
    :param commands: list of commands from file
    :param movies_by_type: list of movies by type
    :return: list of type and runtime
    """
    new_movie_list = []
    if len(movies_by_type) <= 0:
        return new_movie_list
    index = int(len(movies_by_type) / 2)
    found = False
    length = len(movies_by_type)
    half = int(index/2)
    while not found:
        if half <= 1:
            found = True
        elif int(commands[0]) > int(movies_by_type[index].runtimeMinutes) or int(movies_by_type[index].runtimeMinutes) > int(
                commands[1]):
            if int(movies_by_type[index].runtimeMinutes) > int(commands[1]):
                index = int(index - half)
                half = int(half/2)
            else:
                index = int(index + half)
                half = int(half / 2)
        else:
            found = True
    up = True
    down = True
    iterator = 0
    while up or down:
        if down and index - iterator >= 0 and int(movies_by_type[index - iterator].runtimeMinutes) >= int(
                commands[0]) and int(
                movies_by_type[index - iterator].runtimeMinutes) <= int(commands[1]):
            if iterator != 0:
                new_movie_list.append(movies_by_type[index - iterator])
        else:
            down = False
        if up and index + iterator < length and int(movies_by_type[index + iterator].runtimeMinutes) <= int(
                commands[1]) and int(
                movies_by_type[index + iterator].runtimeMinutes) >= int(commands[0]):
            new_movie_list.append(movies_by_type[index + iterator])
        else:
            up = False
        iterator += 1
    return new_movie_list


def list_of_years(commands: list, movies_by_type) -> list:
    """
    splices a list of type into a list of type and specified years
    :param commands: list of commands from file
    :param movies_by_type: list of movies by type
    :return: list of type and years
    """
    new_movie_list = []
    if len(movies_by_type) <= 0:
        return new_movie_list
    index = int(len(movies_by_type) / 2)
    found = False
    length = len(movies_by_type)
    half = int(index / 2)
    while not found:
        if half <= 1:
            found = True
        elif int(commands[0]) > int(movies_by_type[index].startYear) or int(movies_by_type[index].startYear) > int(commands[1]):
            if int(movies_by_type[index].startYear) > int(commands[1]):
                index = int(index - half)
                half = int(half / 2)
            else:
                index = int(index + half)
                half = int(half / 2)
        else:
            found = True
    up = True
    down = True
    iterator = 0
    while up or down:
        if down and index - iterator >= 0 and int(movies_by_type[index - iterator].startYear) >= int(commands[0]) and int(
                movies_by_type[index - iterator].startYear) <= int(commands[1]):
            if iterator != 0:
                new_movie_list.append(movies_by_type[index - iterator])
        else:
            down = False
        if up and index + iterator < length and int(movies_by_type[index + iterator].startYear) <= int(commands[1]) and int(
                movies_by_type[index + iterator].startYear) >= int(commands[0]):
            new_movie_list.append(movies_by_type[index + iterator])
        else:
            up = False
        iterator += 1
    return new_movie_list
