"""
CSAPX Project One: Movies
movies_main.py

Main method of the program that handles the commands from file and reads in dataset.

Author: RIT CS
Author: Adrian Marcellus
"""
import sys
import time
import operator

import list_splicing
import movie_dataclass as md
import rating_dataclass as rt


def main() -> None:
    """
    Main method parsing through the file.
    :return: None
    """
    if len(sys.argv) == 1:
        movies = "data/title.basics.tsv"
        ratings = "data/title.ratings.tsv"
    else:
        movies = "data/small.basics.tsv"
        ratings = "data/small.ratings.tsv"

    print("reading " + movies + " into dict...")
    start = time.perf_counter()
    movie_dict = md.read_movies(movies)
    print("elapsed time (s): " + str(time.perf_counter() - start))
    print()

    print("reading " + ratings + " into dict...")
    start = time.perf_counter()
    ratings_dict = rt.read_ratings(ratings, movie_dict)
    print("elapsed time (s): " + str(time.perf_counter() - start))
    print()
    tot_movies = 0
    for dictionary in movie_dict.values():
        tot_movies += len(dictionary)
    print("Total movies: " + str(tot_movies))
    print("Total ratings: " + str(len(ratings_dict)))

    for line in sys.stdin:
        commands = line.split(" ")
        commands[-1] = commands[-1].split('\n')[0]
        print()
        if commands[0].upper() == "LOOKUP":
            print("processing: LOOKUP " + commands[1])
            start = time.perf_counter()
            look_up(commands, movie_dict, ratings_dict)
            print("elapsed time (s): " + str(time.perf_counter() - start))
        elif commands[0].upper() == "CONTAINS":
            print("processing: " + print_list(commands))
            start = time.perf_counter()
            try:
                contains(print_list(commands[2:]), list(movie_dict[commands[1]].values()))
            except KeyError:
                print("\tNo match found!")
            print("elapsed time (s): " + str(time.perf_counter() - start))
        elif commands[0].upper() == "YEAR_AND_GENRE":
            print("processing: " + print_list(commands))
            start = time.perf_counter()
            try:
                year_and_genre(commands, list(movie_dict[commands[1]].values()))
            except KeyError:
                print("\tNo match found!")
            print("elapsed time (s): " + str(time.perf_counter() - start))
        elif commands[0].upper() == "RUNTIME":
            print("processing: " + print_list(commands))
            start = time.perf_counter()
            try:
                run_time(commands, list(movie_dict[commands[1]].values()))
            except KeyError:
                print("\tNo match found!")
            print("elapsed time (s): " + str(time.perf_counter() - start))
        elif commands[0].upper() == "MOST_VOTES":
            print("processing: " + print_list(commands))
            start = time.perf_counter()
            try:
                most_votes(commands, list(movie_dict[commands[1]].values()), ratings_dict)
            except KeyError:
                print("\tNo match found!")
            print("elapsed time (s): " + str(time.perf_counter() - start))
        elif commands[0].upper() == "TOP":
            print("processing: " + print_list(commands))
            start = time.perf_counter()
            try:
                top(commands, list(movie_dict[commands[1]].values()), ratings_dict)
            except KeyError:
                top(commands, [], ratings_dict)
            print("elapsed time (s): " + str(time.perf_counter() - start))
        else:
            print(commands[0] + " is not a command.")
            sys.exit()
    sys.exit()


def top(commands: list, movies_by_type: list, ratings: dict) -> None:
    """
    prints the top movies within a range of year
    :param commands: list - commands from file
    :param movies_by_type: list - a list of just movie objects sorted by titleType
    :param ratings: dict - dictionary of rating objects
    :return: None
    """
    movies_by_type.sort(key=operator.attrgetter("startYear"))
    movies_by_type = list_splicing.list_of_years(commands[3:], movies_by_type)
    movies_by_type.sort(key=operator.attrgetter("startYear"))
    index = 0
    new_movie_list = []
    for i in range(int(commands[3]), int(commands[4]) + 1):
        print("\tYEAR: " + str(i))
        if len(movies_by_type) > 0 and movies_by_type[index].startYear == str(i):
            for x in range(index, len(movies_by_type)):
                if movies_by_type[x].startYear == str(i):
                    if x == len(movies_by_type) - 1:
                        new_movie_list.append(movies_by_type[x])
                        ratings_top(commands, new_movie_list, ratings)
                    else:
                        new_movie_list.append(movies_by_type[x])
                else:
                    index = x
                    ratings_top(commands, new_movie_list, ratings)
                    new_movie_list = []
                    break
        else:
            print("\t\tNo match found!")


def ratings_top(commands: list, list_of_year: list, ratings: dict) -> None:
    """
    prints top rating within a given year
    :param commands: list - commands from file
    :param list_of_year: list - list of movie objects of a given year
    :param ratings: dict - rating object dictionary
    :return: None
    """
    top_num = int(commands[2])
    new_list = []
    for movie in list_of_year:
        if movie.tconst in ratings:
            rating = ratings[movie.tconst]
            if rating.numVotes >= 1000:
                new_list.append([movie, rating.numVotes, rating.averageRating, movie.primaryTitle])
    if top_num > len(list_of_year):
        top_num = len(list_of_year)
    if len(new_list) == 0:
        print("\t\tNo match found!")
        return
    new_list.sort(key=operator.itemgetter(3))
    new_list.sort(key=operator.itemgetter(1), reverse=True)
    new_list.sort(key=operator.itemgetter(2), reverse=True)
    iterator = 1
    for a_list in new_list:
        if iterator - 1 == top_num:
            break
        print("\t\t" + str(iterator) + ". RATING: " + str(a_list[2]) + ", VOTES: " + str(
            a_list[1]) + ", MOVIE: " + md.print_movie(a_list[0]))
        iterator += 1


def most_votes(commands: list, list_of_type: list, ratings: dict) -> None:
    """
    finds movies with the highest votes
    :param commands:
    :param list_of_type: list - list of movie objects by type
    :param ratings: dict - dictionary of rating objects
    :return: None
    """
    top_num = int(commands[2])
    new_list = []
    for movie in list_of_type:
        if movie.tconst in ratings:
            rating = ratings[movie.tconst]
            new_list.append([movie, rating.numVotes, movie.primaryTitle])
    if top_num > len(list_of_type):
        top_num = len(list_of_type)
    if len(new_list) == 0:
        print("\tNo match found!")
        return
    new_list.sort(key=operator.itemgetter(2))
    new_list.sort(key=operator.itemgetter(1), reverse=True)
    iterator = 1
    for a_list in new_list:
        if iterator - 1 == top_num:
            break
        print("\t" + str(iterator) + ". VOTES: " + str(
            a_list[1]) + ", MOVIE: " + md.print_movie(a_list[0]))
        iterator += 1


def run_time(commands: list, movies_by_type: list) -> None:
    """
    finds movies within a runtime
    :param commands: list - commands from file
    :param movies_by_type: list - list of movies by type
    :return: None
    """
    movies_by_type.sort(key=operator.attrgetter("runtimeMinutes"))
    movies_by_type = list_splicing.list_of_runtime(commands[2:], movies_by_type)
    if len(movies_by_type) == 0:
        print("\tNo match found!")
    else:
        movies_by_type.sort(key=operator.attrgetter("primaryTitle"))
        movies_by_type.sort(key=operator.attrgetter("runtimeMinutes"), reverse=True)
        for movie in movies_by_type:
            print("\t" + md.print_movie(movie))


def year_and_genre(commands: list, movies_by_type: list) -> None:
    """
    finds movies of a year and genre
    :param commands: list - list of commands from file
    :param movies_by_type: list - list of movies by type
    :return: None
    """
    movies_by_type.sort(key=operator.attrgetter("startYear"))
    movies_by_type = list_splicing.list_of_years([commands[2], commands[2]], movies_by_type)
    new_list_movies = []
    for movie in movies_by_type:
        if commands[3] in movie.genres:
            new_list_movies.append(movie)
    if len(new_list_movies) == 0:
        print("\tNo match found!")
    else:
        new_list_movies.sort(key=operator.attrgetter("primaryTitle"))
        for movie in new_list_movies:
            print("\t" + md.print_movie(movie))


def contains(command: str, movie_list: list) -> None:
    """
    finds movies that contain a genre
    :param command: str - command of what genre
    :param movie_list: list - list of movies by type
    :return: None
    """
    new_list_movies = []
    for movie in movie_list:
        if command in movie.primaryTitle:
            new_list_movies.append(movie)
    if len(new_list_movies) == 0:
        print("\tNo match found!")
    else:
        new_list_movies.sort(key=operator.attrgetter("order"))
        for movie in new_list_movies:
            print("\t" + md.print_movie(movie))


def look_up(commands: list, movies: dict, ratings: dict) -> None:
    """
    finds the movie and rating of a specified movie
    :param commands: list - commands from file
    :param movies: dict - dictionary of movies
    :param ratings: dict - dictionary of ratings
    :return: None
    """

    found = False
    for dictionary in movies.values():
        if commands[1] in dictionary:
            movie = dictionary[commands[1]]
            print("\tMOVIE: ", end="")
            print(md.print_movie(movie))
            found = True
            break
    if not found:
        print("\tMovie not found!")
    try:
        rating = ratings[commands[1]]
        print("\tRATING: ", end="")
        print(rt.print_rating(rating))
    except KeyError:
        print("\tRating not found!")


def print_list(plist: list) -> str:
    """
    prints a list as one string with spaces between fields
    :param plist:  list - list to parse
    :return: str - string from parsed list
    """
    string = ""
    for i in range(len(plist)):
        if i == len(plist) - 1:
            string += plist[i]
        else:
            string += plist[i] + " "
    return string


if __name__ == '__main__':
    main()
