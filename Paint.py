class paint:
    
    board = []
    continueOpt = True

    def command_request(self):
        option = input('> ').split()

        if option[0] == 'I' and option[1].isnumeric() and option[2].isnumeric():
            print('ok')

        elif option[0] == 'X':
            print('bye')
            self.continueOpt = False

        else:
            print('Command not found')
