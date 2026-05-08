# Design Doc: Puzzle Module

## Overview
The `puzzle.py` module provides the `Puzzle` class for managing crossword puzzle data including clues, word positions, and solution validation.

## Implementation Details

### Puzzle Class
- **Purpose**: Manages puzzle data structure with clues and solution grid
- **Storage**: Clues in nested dict format; solution grid as 2D list

### Clue Data Structure
```python
{
    "across": {
        1: {"clue": "Description", "positions": [(0,0), (0,1), ...]},
        ...
    },
    "down": {
        1: {"clue": "Description", "positions": [(0,0), (1,0), ...]},
        ...
    }
}
```

### Methods

#### `__init__(clues: Dict, solution_grid: List[List[str]])`
- Initializes puzzle with clues dictionary and solution grid
- Solution grid is a 2D list of characters

#### `get_clue(number: int, direction: str) -> Optional[str]`
- Returns clue text for given number and direction
- Returns None if clue not found

#### `get_word_positions(number: int, direction: str) -> Optional[List[Tuple[int, int]]]`
- Returns list of (row, col) positions for word
- Returns None if word not found

#### `get_all_word_numbers(direction: str) -> List[int]`
- Returns list of all clue numbers in specified direction
- Direction: "across" or "down"

#### `validate_word(word: str, number: int, direction: str) -> bool`
- Checks if entered word matches solution
- Compares against solution grid at each position
- Returns True if word matches solution exactly

## Constraints
- Clue numbers must be integers
- Directions: "across" or "down"
- Validation checks both length and character-by-character match