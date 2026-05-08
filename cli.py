import re
from typing import Optional, Tuple

from game import Game


class CLI:
    """Command-line interface for interactive crossword gameplay."""

    def __init__(self, game: Game):
        """Initialize CLI with a game instance."""
        self._game = game

    def run(self) -> None:
        """Start the interactive CLI loop."""
        print("=" * 50)
        print("Welcome to Crossword Puzzle!")
        print("=" * 50)
        print()
        self._print_instructions()
        print()

        while True:
            self.display_status()

            if self._game.is_complete():
                print("\n" + "=" * 50)
                print("CONGRATULATIONS! You've solved the puzzle!")
                print("=" * 50)
                break

            user_input = self._get_user_input()
            if user_input is None:
                continue

            command, args = user_input

            if command == "quit":
                print("Thanks for playing!")
                break
            elif command == "hint":
                if args:
                    self._provide_hint(args[0], args[1])
                else:
                    print("Usage: hint <clue_number> <direction>")
            elif command == "enter":
                if len(args) >= 3:
                    try:
                        clue_num = int(args[0])
                        direction = args[1].lower()
                        word = args[2].upper()
                        result = self._game.enter_word(clue_num, direction, word)
                        self._print_result(result)
                    except ValueError:
                        print("Invalid clue number. Please enter a number.")
                else:
                    print("Usage: enter <clue_number> <direction> <word>")
            elif command == "help":
                self._print_instructions()
            else:
                print(f"Unknown command: {command}")
                self._print_instructions()

    def display_status(self) -> None:
        """Show current grid and progress."""
        status = self._game.get_status()
        remaining = self._game.get_remaining_clues()

        print(f"\nProgress: {status['solved_count']}/{status['total_words']} words")
        print()

        # Display the grid with clues
        self._display_grid()

        # Show remaining clues
        if remaining:
            print("\nRemaining clues:")
            for item in remaining:
                direction_label = "Across" if item["direction"] == "across" else "Down"
                print(f"  {item['number']}.{direction_label}: {item['clue']}")

    def _display_grid(self) -> None:
        """Display the crossword grid with clue numbers."""
        grid_state = self._game.get_status()["grid_state"]

        # Find max row/col from positions
        max_row, max_col = 0, 0
        for key in grid_state:
            row, col = map(int, key.split(","))
            max_row = max(max_row, row)
            max_col = max(max_col, col)

        # Get word positions to find clue numbers
        clues = {}
        for direction in ["across", "down"]:
            for clue_num in self._game._puzzle.get_all_word_numbers(direction):
                positions = self._game._puzzle.get_word_positions(clue_num, direction)
                if positions:
                    start = positions[0]
                    pos_key = f"{start[0]},{start[1]}"
                    clues[pos_key] = clue_num

        # Render the grid
        print("Grid:")
        print("  " + " ".join(str(i % 10) for i in range(max_col + 1)))

        for row in range(max_row + 1):
            line = f"{row % 10} "
            for col in range(max_col + 1):
                cell_key = f"{row},{col}"
                if cell_key in grid_state:
                    line += f" {grid_state[cell_key]} "
                else:
                    pos_key = f"{row},{col}"
                    if pos_key in clues:
                        clue_num = clues[pos_key]
                        line += f"{clue_num:2d}"
                    else:
                        line += " . "
            print(line)

    def _get_user_input(self) -> Optional[Tuple[str, list]]:
        """Parse user input for word entry."""
        try:
            user_input = input("\nCommand (or 'quit' to exit): ").strip()
        except EOFError:
            return None

        if not user_input:
            return None

        parts = user_input.split()
        command = parts[0].lower()

        if command in ["enter", "hint"]:
            return command, parts[1:]
        elif command in ["quit", "help"]:
            return command, []
        else:
            return None, []

    def _print_result(self, result: dict) -> None:
        """Print the result of a word entry attempt."""
        print()
        if result["success"]:
            print(f"✓ {result['message']}")
        else:
            print(f"✗ {result['message']}")
            if result.get("conflicts"):
                print("  Conflicts found:")
                for row, col, existing, expected in result["conflicts"][:3]:
                    print(f"    Position ({row},{col}): expected '{expected}', got '{existing}'")

    def _print_instructions(self) -> None:
        """Print command instructions."""
        print("Commands:")
        print("  enter <clue_number> <direction> <word>")
        print("    Example: enter 1 across PYTHON")
        print()
        print("  hint <clue_number> <direction>")
        print("    Example: hint 1 across")
        print()
        print("  quit")
        print("  help")
        print()

    def _provide_hint(self, clue_num_str: str, direction: str) -> None:
        """Provide a hint by automatically filling the word."""
        try:
            clue_num = int(clue_num_str)
            if self._game.fill_word(clue_num, direction.lower()):
                print(f"Hint: Word #{clue_num} {direction} has been filled.")
            else:
                print(f"Word #{clue_num} {direction} is already filled or invalid.")
        except ValueError:
            print("Invalid clue number.")
