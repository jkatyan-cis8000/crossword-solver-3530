from typing import List, Optional, Tuple


class Grid:
    """Manages a 2D crossword grid."""

    def __init__(self, size: Tuple[int, int]):
        """Initialize grid with given size (rows, cols)."""
        self.rows, self.cols = size
        self._grid: List[List[Optional[str]]] = [
            [None for _ in range(self.cols)] for _ in range(self.rows)
        ]

    def get_cell(self, row: int, col: int) -> Optional[str]:
        """Get the character at a position."""
        return self._grid[row][col]

    def set_cell(self, row: int, col: int, char: str) -> None:
        """Set a character at a position."""
        self._grid[row][col] = char

    def place_word(
        self, word: str, start: Tuple[int, int], direction: str
    ) -> bool:
        """Place a word in the grid. Returns True if successful."""
        row, col = start
        if direction == "across":
            if col + len(word) > self.cols:
                return False
            for i, char in enumerate(word):
                if self._grid[row][col + i] is None:
                    self._grid[row][col + i] = char
        elif direction == "down":
            if row + len(word) > self.rows:
                return False
            for i, char in enumerate(word):
                if self._grid[row + i][col] is None:
                    self._grid[row + i][col] = char
        else:
            return False
        return True

    def render(self) -> str:
        """Render the grid as a string for display."""
        lines = []
        for row in self._grid:
            line_parts = []
            for cell in row:
                if cell is None:
                    line_parts.append(".")
                else:
                    line_parts.append(cell)
            lines.append(" ".join(line_parts))
        return "\n".join(lines)