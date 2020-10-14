class paint:
    
    board = []

    def command_request(self):
        option = input('> ').split()

        if option[0] == 'I' and option[1].isnumeric() and option[2].isnumeric():
            print('ok')

        if option[0] == 'X':
            print('bye')
            return False

        return True

