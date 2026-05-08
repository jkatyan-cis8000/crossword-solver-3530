from typing import Dict, List, Optional, Tuple


class Puzzle:
    """Manages crossword puzzle data: clues, word positions, and solution."""

    def __init__(
        self, clues: Dict, solution_grid: List[List[str]]
    ):
        """Initialize puzzle with clues and solution grid."""
        self._clues = clues
        self._solution_grid = solution_grid

    def get_clue(self, number: int, direction: str) -> Optional[str]:
        """Get clue text by number and direction."""
        direction_clues = self._clues.get(direction, {})
        clue_data = direction_clues.get(number)
        if clue_data:
            return clue_data.get("clue")
        return None

    def get_word_positions(
        self, number: int, direction: str
    ) -> Optional[List[Tuple[int, int]]]:
        """Get cell positions for a word."""
        direction_clues = self._clues.get(direction, {})
        clue_data = direction_clues.get(number)
        if clue_data:
            return clue_data.get("positions")
        return None

    def get_all_word_numbers(self, direction: str) -> List[int]:
        """Get all clue numbers in a direction."""
        direction_clues = self._clues.get(direction, {})
        return list(direction_clues.keys())

    def validate_word(
        self, word: str, number: int, direction: str
    ) -> bool:
        """Validate if a word matches the solution."""
        positions = self.get_word_positions(number, direction)
        if positions is None:
            return False

        if len(word) != len(positions):
            return False

        for (row, col), char in zip(positions, word):
            if self._solution_grid[row][col] != char:
                return False

        return True