# Crossword Puzzle Application Architecture

## Overview
A command-line crossword puzzle game where users fill in grid entries by clue number and direction, with real-time validation and completion confirmation.

## Modules

### 1. grid.py
**Responsibility:** Manages the crossword grid state and rendering

**Exports:**
- `Grid(size: tuple[int, int])` - Creates a grid of specified size
- `Grid.place_word(word: str, start: tuple[int, int], direction: str) -> bool` - Places a word in the grid
- `Grid.get_cell(row: int, col: int) -> Optional[str]` - Gets the character at a position
- `Grid.set_cell(row: int, col: int, char: str)` - Sets a character at a position
- `Grid.render() -> str` - Renders the grid as a string for display

### 2. puzzle.py
**Responsibility:** Manages the crossword puzzle data (clues, solutions, word positions)

**Exports:**
- `Puzzle(clues: dict, solution_grid: List[List[str]])` - Creates a puzzle with clues and solution
- `Puzzle.get_clue(number: int, direction: str) -> Optional[str]` - Gets a clue by number and direction
- `Puzzle.get_word_positions(number: int, direction: str) -> Optional[list]` - Gets cell positions for a word
- `Puzzle.get_all_word_numbers(direction: str) -> list` - Gets all clue numbers in a direction
- `Puzzle.validate_word(word: str, number: int, direction: str) -> bool` - Validates if a word matches the solution

### 3. game.py
**Responsibility:** Core game logic - tracks progress, accepts user input, validates entries

**Exports:**
- `Game(puzzle: Puzzle)` - Creates a game with a puzzle
- `Game.enter_word(clue_number: int, direction: str, word: str) -> dict` - Attempts to enter a word
- `Game.get_status() -> dict` - Gets current game status (grid state, solved words, progress)
- `Game.is_complete() -> bool` - Checks if the puzzle is fully solved
- `Game.get_remaining_clues() -> list` - Lists clues not yet filled

### 4. cli.py
**Responsibility:** Command-line interface for user interaction

**Exports:**
- `CLI(game: Game)` - Creates CLI with game instance
- `CLI.run()` - Starts the interactive CLI loop
- `CLI.display_status()` - Shows current grid and progress
- `CLI.get_user_input() -> Optional[tuple]` - Parses user input for word entry

### 5. main.py
**Responsibility:** Application entry point - initializes puzzle and starts game

**Exports:**
- `main()` - Entry point that sets up and runs the game

## Data Flow
1. `main.py` creates a `Puzzle` with pre-defined clues and solution
2. A `Game` instance tracks the player's progress
3. `CLI` provides interaction loop, accepting clue number and direction
4. `Game.enter_word()` validates against `Puzzle` solution
5. `Grid` renders the current state showing filled letters

## Interfaces

### Puzzle Data Structure
```python
{
    "across": {
        1: {"clue": "...", "positions": [(0,0), (0,1), ...]},
        ...
    },
    "down": {
        1: {"clue": "...", "positions": [(0,0), (1,0), ...]},
        ...
    }
}
```

### Validation Response
```python
{
    "success": bool,
    "message": str,
    "conflicts": list,  # list of conflicting positions if any
    "already_filled": bool
}
```
