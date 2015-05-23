import requests
from sys import argv
from sys import exit
from os import environ
from collections import deque

client_id = environ['CLIENT_ID']
client_secret = environ['CLIENT_SECRET']


class CliInterface:
    def __init__(self, graph):
        self.graph = graph

    def start(self):
        print("Welcome to our github crawler.")

        while True:
            command = input("Enter command > ")
            try:
                self.__command_dispatcher(command)
            except Exit:
                break

    def __command_dispatcher(self, command):
        parts = command.split(" ")
        if parts[0] == "do_you_follow":
            print(self.graph.do_you_follow(parts[1]))

        elif parts[0] == "do_you_follow_indirectly":
            print(self.graph.do_you_follow_indirectly(parts[1]))

        elif parts[0] == "does_he_she_follows":
            print(self.graph.does_he_she_follows(parts[1]))

        elif parts[0] == "does_he_she_follows_indirectly":
            print(self.graph.does_he_she_follows_indirectly(parts[1]))

        elif parts[0] == "who_follows_you_back":
            print(self.graph.who_follows_you_back())

        elif parts[0] == 'exit':
            raise Exit

        else:
            print('Not a valid command')


class Exit(Exception):
    pass


class DirectedGraph:
    def __init__(self):
        self.__edges = {}

    def add_edge(self, node_a, node_b):
        if node_a not in self.__edges:
            self.__edges[node_a] = []
        if node_b not in self.__edges:
            self.__edges[node_b] = []

        self.__edges[node_a].append(node_b)

    def get_neighbours_for(self, node):
        return self.__edges[node]

    def path_between(self, node_a, node_b):
        if node_a not in self.__edges or node_b not in self.__edges:
            return False

        visited = set()
        queue = []

        queue.append(node_a)
        visited.add(node_a)

        found = False

        while len(queue) > 0:
            current_node = queue.pop()
            if current_node == node_b:
                found = True
                break

            for neighbour in self.__edges[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return found


class GitHubCrawler:
    def __init__(self, name, level):
        self.graph = DirectedGraph()
        self.name = name
        self.level = level

    def create_graph(self):
        visited = set()
        queue = deque()
        levels_to_me = {}

        queue.append(self.name)
        visited.add(self.name)
        levels_to_me[self.name] = 0

        while len(queue) > 0:
            current_user = queue.popleft()

            if levels_to_me[current_user] > self.level:
                break

            for neighbour in self.get_neighbours_from_api(current_user):
                self.graph.add_edge(current_user, neighbour)
                if neighbour not in visited:
                    levels_to_me[neighbour] = levels_to_me[current_user] + 1
                    visited.add(neighbour)
                    queue.append(neighbour)

    def get_neighbours_from_api(self, user):
        url = "https://api.github.com/users/{}/following?client_id={}&client_secret={}".format(user, client_id, client_secret)
        following_json = requests.get(url).json()

        result = []

        for item in following_json:
            result.append(item["login"])

        return result

# returns True / False if you follow directly the given user
    def do_you_follow(self, user):
        return user in self.graph.get_neighbours_for(self.name)

    def do_you_follow_indirectly(self, user):
        return self.graph.path_between(self.name, user)

    def does_he_she_follows(self, user):
        return self.name in self.graph.get_neighbours_for(user)

# returns True / False if the given users follows someone who follows you
    def does_he_she_follows_indirectly(self, user):
        return self.graph.path_between(user, self.name)

# returns usernames, that follows you and are followed by you or by people you follow
    def who_follows_you_back(self):
        result = []

        visited = set()
        queue = []

        queue.append(self.name)
        visited.add(self.name)

        while len(queue) > 0:
            current_node = queue.pop(0)

            if self.does_he_she_follows(current_node):
                result.append(current_node)

            for neighbour in self.graph.get_neighbours_for(current_node):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return result


def main():
    if len(argv) != 3:
        print("Usage: type 'python3 follow_github.py <name> <level>'")
        exit("Try again! :)")
    gh_crawler = GitHubCrawler(argv[1], int(argv[2]))
    gh_crawler.create_graph()
    cli = CliInterface(gh_crawler)
    cli.start()


if __name__ == '__main__':
    main()
