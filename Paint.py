class paint:
    
    __board = []
    continueOpt = True

    def command_request(self):
        option = input('> ').split()

        if option[0] == 'I' and option[1].isnumeric() and option[2].isnumeric():
            self.new_image(option[1], option[2])

        elif option[0] == 'L' and option[1].isnumeric() and option[2].isnumeric():
            self.colours_pixel(option[1], option[2], option[3])
        
        elif option[0] == 'S':
            print(self.__board)

        elif option[0] == 'X':
            print('bye')
            self.continueOpt = False

        else:
            print('Command not found')

    def new_image(self, Mx, Ny):
        for i in range(int(Ny)):
            row = []
            for j in range(int(Mx)):
                row.append('O')
            self.__board.append(row)

    def colours_pixel(self, Mx, Ny, value):
        if self.__board[int(Mx) - 1][int(Ny) - 1]:
            self.__board[int(Mx) - 1][int(Ny) - 1] = value   
        else:
            print('Pixel doesnt exist')
