# CSC242-Project-1
CSC242 Python Project

This project works with datasets from the IMDB website. This provided
experience reading in the data and using various structures and collections in Python to
store, organize and efficiently query for different kinds of information relating to the movies
and their ratings.


Data:

tt0033467 movie Citizen Kane Citizen Kane 0 1941 \N 119 Drama,Mystery

tt0052357 movie Vertigo Vertigo 0 1958 \N 128 Mystery,Romance,Thriller

tt0081505 movie The Shining The Shining 0 1980 \N 146 Drama,Horror


The fields of importance for title data:

• tconst: will always have a valid value

• titleType: will always have a valid value

• primaryTitle: will always have a valid value

• isAdult: will always have a valid value

• startYear: if no value then assume 0

• runtimeMinutes: if no value than assume 0

• genres: will always have a valid value


Queries:
There are a total of six unique kind of queries this program supports.

1. LOOKUP {tconst}: Look up a movie and rating by its unique identifier.

2. CONTAINS {titleType} {words}: Find all movies of a certain type whose titles
contain the sequence of words.

3. YEAR AND GENRE {titleType} {year} {genre}: Find all movies of a certain
type from a particular year that match a genre.

4. RUNTIME {titleType} {min-minutes} {max-minutes}: Find all movies of a
certain type that are within a range of runtimes.

5. MOST VOTES {titleType} {num}: Find the given number of movies of a certain
type with the most votes.

6. TOP {titleType} {num} {start-year} {end-year}: Find the number of movies
of a certain type by a range of years (inclusive) that are the highest rated and have at
least 1000 votes.

