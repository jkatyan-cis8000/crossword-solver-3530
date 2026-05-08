"""
Crossword Puzzle Game - Main Entry Point

This module sets up a sample crossword puzzle and starts the interactive game.
"""

from puzzle import Puzzle
from game import Game
from cli import CLI


def create_sample_puzzle() -> Puzzle:
    """
    Create a sample 5x5 crossword puzzle with clues and solution.
    
    Grid layout (positions):
    P Y T H O
    Y 0 0 0 0
    T 0 0 0 0
    H 0 0 0 0
    O 0 0 0 0
    
    Words:
    - 1 across: PYTHON (row 0, cols 0-5)
    - 1 down: PYTHO (cols 0, rows 0-5)
    """
    
    # Define the solution grid (5 rows, 5 columns)
    solution_grid = [
        ['P', 'Y', 'T', 'H', 'O'],
        ['Y', 'A', 'R', 'P', 'S'],
        ['T', 'R', 'E', 'A', 'D'],
        ['H', 'A', 'L', 'L', 'S'],
        ['O', 'S', 'D', 'S', 'Y']
    ]
    
    # Define clues with their positions in the grid
    clues = {
        "across": {
            1: {
                "clue": "Popular programming language named after a snake",
                "positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
            },
            2: {
                "clue": "Metal detector output",
                "positions": [(1, 1), (1, 2), (1, 3), (1, 4)]
            },
            3: {
                "clue": "Path through a forest",
                "positions": [(2, 1), (2, 2), (2, 3), (2, 4)]
            },
            4: {
                "clue": "Multi-purpose building",
                "positions": [(3, 1), (3, 2), (3, 3), (3, 4)]
            },
            5: {
                "clue": "Synonym for 'by' in old English",
                "positions": [(4, 1), (4, 2), (4, 3), (4, 4)]
            }
        },
        "down": {
            1: {
                "clue": "First letter of Greek alphabet",
                "positions": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
            },
            2: {
                "clue": "Snake + Python's namesake",
                "positions": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
            },
            3: {
                "clue": "Past tense of 'tear' (to rip)",
                "positions": [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]
            },
            4: {
                "clue": "End of a rope",
                "positions": [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]
            },
            5: {
                "clue": "Synonym for 'say' (archaic)",
                "positions": [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
            }
        }
    }
    
    return Puzzle(clues, solution_grid)


def main():
    """Entry point for the crossword puzzle game."""
    print("Crossword Puzzle Game")
    print("=" * 50)
    
    # Create the puzzle with sample data
    puzzle = create_sample_puzzle()
    
    # Create game with the puzzle
    game = Game(puzzle)
    
    # Create and run the CLI
    cli = CLI(game)
    cli.run()


if __name__ == "__main__":
    main()
