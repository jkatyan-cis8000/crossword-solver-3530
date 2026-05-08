from typing import Dict, List, Optional, Set


class Game:
    """Manages game state: tracks progress, validates word entries, reports completion."""

    def __init__(self, puzzle):
        """Initialize game with a puzzle instance."""
        self._puzzle = puzzle
        self._filled_words: Set[str] = set()
        self._grid_state: Dict[str, str] = {}

    def enter_word(self, clue_number: int, direction: str, word: str) -> dict:
        """
        Attempt to enter a word into the puzzle.
        Returns a dict with success status and message.
        """
        word_key = f"{clue_number}{direction}"

        if word_key in self._filled_words:
            return {
                "success": False,
                "message": f"Word #{clue_number} {direction} is already filled.",
                "already_filled": True
            }

        # Validate word against puzzle solution
        if not self._puzzle.validate_word(word, clue_number, direction):
            # Check if any letters conflict with existing filled letters
            positions = self._puzzle.get_word_positions(clue_number, direction)
            conflicts = []
            if positions:
                for (row, col) in positions:
                    cell_key = f"{row},{col}"
                    if cell_key in self._grid_state:
                        existing = self._grid_state[cell_key]
                        # Find position where they differ
                        pos_idx = positions.index((row, col))
                        if pos_idx < len(word) and word[pos_idx] != existing:
                            conflicts.append((row, col, existing, word[pos_idx]))

            if conflicts:
                return {
                    "success": False,
                    "message": f"Word #{clue_number} {direction} does not match solution. "
                              f"Conflicts found at positions.",
                    "conflicts": conflicts
                }
            return {
                "success": False,
                "message": f"Word #{clue_number} {direction} does not match solution.",
                "conflicts": []
            }

        # Valid entry - record it
        self._filled_words.add(word_key)

        # Update grid state with the filled word
        positions = self._puzzle.get_word_positions(clue_number, direction)
        for i, (row, col) in enumerate(positions):
            self._grid_state[f"{row},{col}"] = word[i]

        return {
            "success": True,
            "message": f"Word #{clue_number} {direction} ('{word}') accepted!",
            "conflicts": []
        }

    def get_status(self) -> dict:
        """Get current game status (grid state, solved words, progress)."""
        all_words = []
        for direction in ["across", "down"]:
            for clue_num in self._puzzle.get_all_word_numbers(direction):
                all_words.append(f"{clue_num}{direction}")

        return {
            "grid_state": self._grid_state,
            "filled_words": list(self._filled_words),
            "total_words": len(all_words),
            "solved_count": len(self._filled_words),
            "progress": len(self._filled_words) / len(all_words) if all_words else 0
        }

    def is_complete(self) -> bool:
        """Check if the puzzle is fully solved."""
        for direction in ["across", "down"]:
            for clue_num in self._puzzle.get_all_word_numbers(direction):
                word_key = f"{clue_num}{direction}"
                if word_key not in self._filled_words:
                    return False
        return True

    def get_remaining_clues(self) -> list:
        """List clues not yet filled."""
        remaining = []
        for direction in ["across", "down"]:
            for clue_num in self._puzzle.get_all_word_numbers(direction):
                word_key = f"{clue_num}{direction}"
                if word_key not in self._filled_words:
                    remaining.append({
                        "number": clue_num,
                        "direction": direction,
                        "clue": self._puzzle.get_clue(clue_num, direction)
                    })
        return remaining

    def fill_word(self, clue_number: int, direction: str) -> bool:
        """Automatically fill a word with the correct solution (for hints)."""
        word_key = f"{clue_number}{direction}"
        if word_key in self._filled_words:
            return False

        positions = self._puzzle.get_word_positions(clue_number, direction)
        if not positions:
            return False

        # Build the solution word from the solution grid
        solution_word = ""
        for row, col in positions:
            solution_word += self._puzzle._solution_grid[row][col]

        self._filled_words.add(word_key)

        for i, (row, col) in enumerate(positions):
            self._grid_state[f"{row},{col}"] = solution_word[i]

        return True
