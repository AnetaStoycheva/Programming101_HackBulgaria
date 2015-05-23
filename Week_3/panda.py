import re
import pickle


class Panda:
    def __init__(self, name, email, gender):

        self.__name = name
        self.__email = email
        self.__gender = gender

        if not isinstance(name, str):
            raise TypeError(str(name) + " is not a valid name.")

        if gender != "male" and gender != "female":
            raise ValueError("The Panda has no valid gender.")

        if not isinstance(email, str):
            raise TypeError(str(email) + " is not a string.")

        if not self.__validate_email():
            raise ValueError(email + " is not a valid email.")

    def __validate_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.__email):
            return False
        return True

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"

    def __str__(self):
        return "Panda account for {} with email {} and gender {}."\
            .format(self.get_name(), self.get_email(), self.get_gender())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_email() == other.get_email()\
            and self.get_gender() == other.get_gender()

    def __hash__(self):
        return hash(self.__str__())


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:
    def __init__(self):
        self.network = {}

    def has_panda(self, panda):
        return panda in self.network

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThere()

        self.network[panda] = []

    def are_friends(self, panda1, panda2):
        return panda1 in self.network[panda2] and\
            panda2 in self.network[panda1]

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends()

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def friends_of(self, panda1):
        if self.has_panda(panda1):
            return self.network[panda1]
        return False

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False

        visited = set()
        queue = []
        levels_to_panda1 = {}

        queue.append(panda1)
        visited.add(panda1)
        levels_to_panda1[panda1] = 0
        found = False

        while len(queue) > 0:
            current_panda = queue.pop(0)
            if current_panda == panda2:
                found = True
                break

            for neighbour in self.network[current_panda]:
                if neighbour not in visited:
                    levels_to_panda1[neighbour] = levels_to_panda1[current_panda] + 1
                    visited.add(neighbour)
                    queue.append(neighbour)

        if found is False:
            return -1

        return levels_to_panda1[panda2]

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) not in [False, -1]

    def how_many_gender_in_network(self, level, panda, gender):

        result = 0

        for neighbour in self.network:
            current_connection_level = self.connection_level(panda, neighbour)

            if neighbour != panda and current_connection_level <= level and neighbour.get_gender() == gender:
                result += 1

        return result

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self.network, f)

    def load(self, file_name):
        with open(file_name, 'rb') as f:
            self.network = pickle.load(f)
