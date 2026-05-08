# Design Doc: Grid Module

## Overview
The `grid.py` module provides the `Grid` class for managing a 2D crossword puzzle grid.

## Implementation Details

### Grid Class
- **Purpose**: Manages crossword grid state and rendering
- **Storage**: Internal 2D list of `Optional[str]` (None for empty cells)

### Methods

#### `__init__(size: Tuple[int, int])`
- Creates a grid with specified dimensions (rows, cols)
- All cells initialized to None (empty)

#### `get_cell(row: int, col: int) -> Optional[str]`
- Returns character at position, or None if empty

#### `set_cell(row: int, col: int, char: str) -> None`
- Sets a character at a position

#### `place_word(word: str, start: Tuple[int, int], direction: str) -> bool`
- Places a word in the grid starting at position
- Direction: "across" or "down"
- Only fills cells that are currently empty
- Returns False if word goes out of bounds

#### `render() -> str`
- Renders grid as string
- Empty cells displayed as "."
- Characters separated by spaces for readability

## Constraints
- Grid coordinates are 0-indexed
- Empty cells represented as None internally, "." when rendered
- Words can only be placed within grid bounds