class Piece:
    def __init__(self, color, place):
        self.color = color
        self.place = place
        self.moves = []
        self.takes = []
        self.target = ""

    def __repr__(self):
        return f"---------------\n" \
               f"color: {self.color}\n"\
               f"place: {self.place}\n" \
               f"target: {self.target}\n" \
               f"moves: {self.moves}\n" \
               f"takes: {self.takes}\n" \
               f"----------------"

class Pawn(Piece)
    def __init__(self, colr, place):
        super().__init__(color, place)
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = self.new_target()
    def get_moves(self):
        raise Exception ()
    def get_takes(self):
        return []
    def new_target(self):
        return "A1"

class Queen(Piece)
    def __init__(self, colr, place):
        super().__init__(color, place)
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = self.new_target()
    def get_moves(self):
        raise Exception ()
    def get_takes(self):
        return []
    def new_target(self):
        return "A1"

piece = Piece('white', 'E2')
print(piece)
