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
    
    Grid layout:
    R O A S Y
    O P E R S
    A E A R Y
    S R R S Y
    Y S Y Y G
    
    Words:
    - 1 across: ROASY (row 0, cols 0-4)
    - 2 across: OPERS (row 1, cols 0-4)
    - 3 across: EARY (row 2, cols 1-4)
    - 4 across: RRSY (row 3, cols 1-4)
    - 5 across: SYYG (row 4, cols 1-4)
    - 1 down: ROASY (col 0, rows 0-4)
    - 2 down: OPERS (col 1, rows 0-4)
    - 3 down: AEARY (col 2, rows 0-4)
    - 4 down: SRRSY (col 3, rows 0-4)
    - 5 down: YSYYG (col 4, rows 0-4)
    """
    
    # Define the solution grid (5 rows, 5 columns)
    solution_grid = [
        ['R', 'O', 'A', 'S', 'Y'],
        ['O', 'P', 'E', 'R', 'S'],
        ['A', 'E', 'A', 'R', 'Y'],
        ['S', 'R', 'R', 'S', 'Y'],
        ['Y', 'S', 'Y', 'Y', 'G']
    ]
    
    # Define clues with their positions in the grid
    # Grid:
    # R O A S Y
    # O P E R S
    # A E A R Y
    # S R R S Y
    # Y S Y Y G
    
    # Across words:
    # Row 0: ROASY
    # Row 1: OPERS
    # Row 2: EARY (cols 1-4)
    # Row 3: RRSY (cols 1-4)
    # Row 4: SYYG (cols 1-4)
    
    # Down words:
    # Col 0: ROASY
    # Col 1: OPERS
    # Col 2: AEARY
    # Col 3: SRRSY
    # Col 4: YSYYG
    
    clues = {
        "across": {
            1: {
                "clue": "Start of 'ROSARY' without B",
                "positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
            },
            2: {
                "clue": "A type of court proceeding",
                "positions": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
            },
            3: {
                "clue": "End of 'BOREAL' (last 4 letters)",
                "positions": [(2, 1), (2, 2), (2, 3), (2, 4)]
            },
            4: {
                "clue": "Plural of military formation",
                "positions": [(3, 1), (3, 2), (3, 3), (3, 4)]
            },
            5: {
                "clue": "Initials of a popular messaging app",
                "positions": [(4, 1), (4, 2), (4, 3), (4, 4)]
            }
        },
        "down": {
            1: {
                "clue": "First word in row 0 (same as across 1)",
                "positions": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
            },
            2: {
                "clue": "First word in row 1 (same as across 2)",
                "positions": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
            },
            3: {
                "clue": "A group of geese in flight",
                "positions": [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]
            },
            4: {
                "clue": "A type of surgical instrument",
                "positions": [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]
            },
            5: {
                "clue": "A stretch of sandy shore",
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
