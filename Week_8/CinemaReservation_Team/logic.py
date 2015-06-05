import sqlite3
import sys
import time

CINEMA_DB = "cinema.db"

conn = sqlite3.connect(CINEMA_DB)
cursor = conn.cursor()


def helpp():
    print("""You can use the following magic commands for our magic cinema:
show_movies
show_movie_projections <movie_id> [<date>]
make_reservation
cancel_reservation <name>
help
exit
abracadabra""")


def abracadabra():
    print("YOUR COMPUTER IS GOING TO EXPLODE IN 3 SECONDS! RUN FOR YOUR LIFE!")
    time.sleep(3)
    print("BOOOOOOOM")
    sys.exit()


def show_movies():
    print("Current movies ordered by rating:")
    result = cursor.execute("""
        SELECT id, name
        FROM Movies
        ORDER BY rating DESC
    """)

    movie_ids = set()

    for row in result.fetchall():
        print("movie_id: {}".format(row[0]), "movie_name: {}".format(row[1]))
        movie_ids.add(row[0])

    return movie_ids


# we have to handle the case where the name is not in reservation table
def cancel_reservation(name):
    cursor.execute("""
        DELETE FROM Reservations
        WHERE username = \"{}\"
    """.format(name))
    conn.commit()


# current function doesn't print the remaining free seats
def show_movie_projections(movie_id, date=None):
    if date is None:
        result = cursor.execute("""
            SELECT proj_id, date, time, type
            FROM Projections
            WHERE movie_id = {}
            ORDER BY date ASC
        """.format(movie_id))
    else:
        result = cursor.execute("""
            SELECT proj_id, time, type
            FROM Projections
            WHERE movie_id = {} AND date = \'{}\'
            ORDER BY date ASC
        """.format(movie_id, date))

    for row in result.fetchall():

        print("projection_id: {}, date: {}, time: {}, type: {}".format(row[0],
            row[1], row[2], row[3]))


def choose_projection(projection_id):
    pass


class GiveUp(Exception):
    pass


def input_or_give_up(argument):
    var = input(argument)
    if var == "give_up":
        raise GiveUp
    else:
        return var


def enter_username():
    while True:
        username = input_or_give_up("Please, enter your name!>")
        if len(username) < 2:
            continue
        else:
            return username


def choose_movie():
    movies_by_ids = show_movies()

    while True:
        chosen_movie_id = input_or_give_up("Choose movie by its 'movie_id'>")
        try:
            chosen_movie_id = int(chosen_movie_id)
            if chosen_movie_id not in movies_by_ids:
                continue
            else:
                return chosen_movie_id

        except:
            continue


# da se opravi!
def make_reservation():

    try:
        hacker = enter_username()
        number_of_tickets = input_or_give_up("Please, enter the number of tickets U want!>")
        chosen_movie_id = choose_movie()
        show_movie_projections(chosen_movie_id, date=None)
        chosen_projection = input_or_give_up("Choose projection by its 'projection_id'>")
        # choose_projection(chosen_projection)  # tova 6te go pazim v bazata
        # aviable_seats()
        # choose_seat()  # tova 6te go pazim v bazata
        # # print("This is your reservation:\n {}\n Date and Time: {}, type\n {}".format(movie_id, date, time, type, seats))
        # conn.commit()
    except GiveUp:
        print("U gave up the reservation process.")
        return


def close_connection():
    conn.close()

# Happy coding :)
# ^ ^
# ---

# Thank youuu :)
