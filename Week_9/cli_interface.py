import hashlib


# hash_object = hashlib.sha1(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)


class CliInterface:
    def __init__(self, sql_manager):
        self.__sql_manager = sql_manager

    def start(self):
        print('Welcome to our bank service. You are not logged in.')
        print('Please register or login')

        while True:
            command = input('$$$>')
            try:
                self.__command_dispatcher(command)
            except Exit:
                break

    def __command_dispatcher(self, command):
        if command == 'register':
            self.__register()
        elif command == 'login':
            self.__login()
        elif command == 'help':
            self.__help()
        elif command == 'exit':
            self.__exit()
        else:
            print('Not a valid command')

    def __register(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')  # safe password!!!

        result = self.__sql_manager.register(username, password)

        if result:
            print('Registration Successful')
        if not result:
            print('Registration failed')

    def __login(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')  # safe password!!!

        logged_user = self.__sql_manager.login(username, password)

        if logged_user:
            self.start_logged_in(logged_user)
        else:
            print('Login failed')

    def __help(self):
        print('login - for logging in!')
        print('register - for creating new account!')
        print('exit - for closing program!')
        print('help - for helping! ;)')

    def __exit(self):
        raise Exit()

    def start_logged_in(self, logged_user):
        print('Welcome you are logged in as: ' + logged_user.get_username())

        while True:
            command = input('Logged>>')
            try:
                self.__command_dispatcher_logged_in(command, logged_user)
            except Logout:
                break

    def __command_dispatcher_logged_in(self, command, logged_user):
        if command == 'info':
            self.__info(logged_user)
        elif command == 'changepass':
            self.__changepass(logged_user)
        elif command == 'change-message':
            self.__change_message(logged_user)
        elif command == 'show-message':
            self.__show_message(logged_user)
        elif command == 'help':
            self.__help_logged_in(logged_user)
        elif command == 'logout':
            self.__logout(logged_user)
        else:
            print('Not a valid command')

    def __info(self, logged_user):
        print("You are: " + logged_user.get_username())
        print("Your id is: " + str(logged_user.get_client_id()))
        print("Your balance is: " + str(logged_user.get_balance()) + '$')

    def __changepass(self, logged_user):
        new_pass = input('Enter your new password: ')
        result = self.__sql_manager.change_pass(new_pass, logged_user)

        if result:
            print('You succesfully changed your password!')
        else:
            print('Changing password failed!')

    def __change_message(self, logged_user):
        new_message = input('Enter your new message: ')
        self.__sql_manager.change_message(new_message, logged_user)

    def __show_message(self, logged_user):
        print(logged_user.get_message())

    def __help_logged_in(self, logged_user):
        print('info - for showing account info')
        print('changepass - for changing passowrd')
        print('change-message - for changing users message')
        print('show-message - for showing users message')
        print('logout - for closing program!')
        print('help - for helping! ;)')

    def __logout(self, logged_user):
        raise Logout()


class Exit(Exception):
    pass


class Logout(Exception):
    pass
