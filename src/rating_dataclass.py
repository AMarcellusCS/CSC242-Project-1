"""
CSAPX Project One: Movies
ratings_dataclass.py

Dataclass for ratings. Functions for reading in dataclasses to dictionary and printing a rating object.

Author: RIT CS
Author: Adrian Marcellus
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Rating:
    tconst: str
    averageRating: float
    numVotes: int


def read_ratings(filename: str, movies_dict: dict) -> dict:
    """
    reads from file into a dictionary of rating dataclasses
    :param filename: str - name of file or ratings
    :param movies_dict: dict - movies dictionary
    :return: dict - rating object dictionary
    """
    with open(filename, encoding='utf-8') as f:
        dictionary = dict()
        f.readline()
        for line in f:
            fields = line.split("\t")
            in_movies = False
            for diction in list(movies_dict.values()):
                if fields[0] in diction:
                    in_movies = True
                    break
            if in_movies:
                dictionary[fields[0]] = Rating(
                    tconst=str(fields[0]),
                    averageRating=float(fields[1]),
                    numVotes=int(fields[2])
                )
    return dictionary


def print_rating(rating: Rating) -> str:
    """
    returns a string of rating object fields
    :param rating: rating object
    :return: str - ratings objects values
    """
    info = ("Identifier: " + rating.tconst + ", Rating: " + str(rating.averageRating) + ", Votes: " + str(
        rating.numVotes))
    return info
