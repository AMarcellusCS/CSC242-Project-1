"""
CSAPX Project One: Movies
movie_dataclass.py

Dataclass for movies. Functions for reading in dataclasses to dictionary and printing a movie object.

Author: RIT CS
Author: Adrian Marcellus
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    tconst: str
    titleType: str
    primaryTitle: str
    originalTitle: str
    isAdult: str
    startYear: str
    endYear: str
    runtimeMinutes: int
    genres: str
    order: int


def read_movies(filename: str) -> dict:
    """
    reads the movies from the file into a dictionary
    :param filename: str - name of the file
    :return: dict - dictionary of movie objects
    """
    dictionary = dict()
    with open(filename, encoding='utf-8') as f:
        f.readline()
        count = 1
        for line in f:
            fields = line.split("\t")
            if fields[4] != "1":
                field7 = fields[7]
                field5 = fields[5]
                if field7 == "\\N":
                    field7 = 0
                if field5 == "\\N":
                    field5 = "0"
                if fields[1] not in dictionary:
                    dictionary[fields[1]] = {fields[0]: Movie(
                        tconst=str(fields[0]),
                        titleType=str(fields[1]),
                        primaryTitle=str(fields[2]),
                        originalTitle=str(fields[3]),
                        isAdult=str(fields[4]),
                        startYear=str(field5),
                        endYear=str(fields[6]),
                        runtimeMinutes=int(field7),
                        genres=str(fields[8]),
                        order=int(count))
                    }
                else:
                    dictionary[fields[1]][fields[0]] = Movie(
                        tconst=str(fields[0]),
                        titleType=str(fields[1]),
                        primaryTitle=str(fields[2]),
                        originalTitle=str(fields[3]),
                        isAdult=str(fields[4]),
                        startYear=str(field5),
                        endYear=str(fields[6]),
                        runtimeMinutes=int(field7),
                        genres=str(fields[8]),
                        order=int(count)
                    )
                count += 1
    return dictionary


def print_movie(movie: Movie) -> str:
    """
    returns string of movie dataclass values
    :param movie: movie object to get fields from
    :return: string of movie object
    """
    genre_string = ""
    if len(movie.genres) <= 3:
        genre_string = "None"
    else:
        movie_genres = movie.genres.strip()
        movie_genres = movie_genres.split(",")
        for i in range(len(movie_genres)):
            if i == (len(movie_genres) - 1):
                genre_string += movie_genres[i]
            else:
                genre_string += movie_genres[i] + ", "
    info = ("Identifier: " + movie.tconst + ", Title: " + movie.primaryTitle + ", Type: " + movie.titleType
            + ", Year: " + str(movie.startYear) + ", Runtime: " + str(movie.runtimeMinutes) + ", Genres: " + genre_string)
    return info
