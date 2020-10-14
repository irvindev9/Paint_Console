class paint:
    
    __board = []
    continueOpt = True

    def command_request(self):
        option = input('> ').split()

        if option[0] == 'I' and option[1].isnumeric() and option[2].isnumeric() and len(option) == 3:
            self.new_board(option[1], option[2])

        elif option[0] == 'L' and option[1].isnumeric() and option[2].isnumeric() and len(option) == 4:
            self.colours_pixel(option[1], option[2], option[3])
        
        elif option[0] == 'V' and option[1].isnumeric() and option[2].isnumeric() and option[3].isnumeric() and len(option) == 5:
            self.colours_vertical(option[1], option[2], option[3], option[4])

        elif option[0] == 'H' and option[1].isnumeric() and option[2].isnumeric() and option[3].isnumeric() and len(option) == 5:
            self.colours_horizontal(option[1], option[2], option[3], option[4])

        elif option[0] == 'F' and option[1].isnumeric() and option[2].isnumeric() and len(option) == 4:
            self.r_region(option[1], option[2], option[3])
        
        elif option[0] == 'S' and len(option) == 1:
            print('\n=>\n')
            print(self.__board)
            
        elif option[0] == 'D' and len(option) == 1:
            self.dimensionsPrint()

        elif option[0] == 'X' and len(option) == 1:
            print('bye')
            self.continueOpt = False

        else:
            print('Command not found')

    def new_board(self, Mx, Ny):
        self.__board = []

        for i in range(int(Ny)):
            row = []
            for j in range(int(Mx)):
                row.append('O')
            self.__board.append(row)

    def colours_pixel(self, Mx, Ny, value):
        if self.validate_pixel((int(Ny) - 1), (int(Mx) - 1)):
            self.__board[int(Ny) - 1][int(Mx) - 1] = value
        else:
            print('Pixel doesnt exist')

    def colours_vertical(self, Mx, Ny1, Ny2, value):
        Ny1 = int(Ny1)
        Ny2 = int(Ny2)

        if Ny1 <= Ny2:
            while Ny1 <= Ny2:
                if self.validate_pixel((int(Ny1) - 1), (int(Mx) - 1)):
                    self.__board[Ny1 - 1][int(Mx) - 1] = value

                Ny1 = Ny1 + 1
        else:
            while Ny2 <= Ny1:
                if self.validate_pixel((int(Ny2) - 1), (int(Mx) - 1)):
                    self.__board[Ny2 - 1][int(Mx) - 1] = value

                Ny2 = Ny2 + 1

    def colours_horizontal(self, Mx1, Mx2, Ny, value):
        Mx1 = int(Mx1)
        Mx2 = int(Mx2)

        if Mx1 <= Mx2:
            while Mx1 <= Mx2:
                if self.validate_pixel((int(Ny) - 1), (Mx1 - 1)):
                    self.__board[int(Ny) - 1][Mx1 - 1] = value

                Mx1 = Mx1 + 1
        else:
            while Mx2 <= Mx1:
                if self.validate_pixel((int(Ny) - 1), (Mx2 - 1)):
                    self.__board[int(Ny) - 1][Mx2 - 1] = value
                    
                Mx2 = Mx2 + 1

    def r_region(self, Mx, Ny, value):
        xVector, yVector = self.dimensions()

        if self.validate_pixel((Ny - 1), (Mx - 1)):
            return 1

        for i in range(xVector):
            # print(self.__board[i - 1])
            for j in range(yVector):
                if self.validate_pixel((j - 1), (i - 1)):
                    if self.__board[j - 1][i - 1] == 1:
                        return 1


    
    def validate_pixel(self, Mx, Ny):
        xVector, yVector = self.dimensions()

        if (int(Mx)) <= xVector and (int(Ny)) <= yVector:
            return True
        else:
            return False

    def dimensions(self):
        yVector = len(self.__board)
        if yVector > 0:
            xVector = len(self.__board[0])
        else:
            xVector = 0

        return xVector, yVector

    def dimensionsPrint(self):
        print(self.dimensions())
        