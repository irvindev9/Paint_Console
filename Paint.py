class paint:
    
    __board = []
    continueOpt = True

    def command_request(self):
        option = input('> ').split()

        if option[0] == 'I' and option[1].isnumeric() and option[2].isnumeric():
            self.new_image(option[1], option[2])

        elif option[0] == 'L' and option[1].isnumeric() and option[2].isnumeric():
            self.colours_pixel(option[1], option[2], option[3])
        
        elif option[0] == 'V' and option[1].isnumeric() and option[2].isnumeric() and option[3].isnumeric():
            self.colours_vertical(option[1], option[2], option[3], option[4])
        
        elif option[0] == 'S':
            print('\n=>\n')
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

    def colours_vertical(self, Mx, Ny1, Ny2, value):
        Ny1 = int(Ny1)
        Ny2 = int(Ny2)

        if Ny1 <= Ny2:
            while Ny1 <= Ny2:
                if self.__board[Ny1 - 1][int(Mx) - 1]:
                    self.__board[Ny1 - 1][int(Mx) - 1] = value
                Ny1 = Ny1 + 1
        else:
            while Ny2 <= Ny1:
                if self.__board[Ny2 - 1][int(Mx) - 1]:
                    self.__board[Ny2 - 1][int(Mx) - 1] = value
                Ny2 = Ny2 + 1
