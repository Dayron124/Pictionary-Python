"""
Stores the state of the drawing board
"""

from _typeshed import Self

class Board(object):
    ROWS = COLS =720
    
    def __init__(self, rows, cols):
        self.data = self._create_empty_board()
        
    def update(x, y, color):
        Self.data[y][x] = color
        
    def clear(self):
        self.data = self._create_empty_board()
        
    def _create_empty_board(self):
        return [[(255,255,255) for _ in range(self.COLS)] for _ in range(self.ROWS)]
    
    def fill(self, x, y):
        pass
    
    def get_board(self):
        return self.data