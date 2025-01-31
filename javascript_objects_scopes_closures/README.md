# JavaScript Objects, Scopes, and Closures

This repository contains a series of tasks related to JavaScript objects, scopes, and closures. Each task demonstrates the use of various JavaScript concepts and follows specific requirements outlined below.

## Requirements

- Allowed editors: vi, vim, emacs
- All files are interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- Each file ends with a new line
- The first line of all files is `#!/usr/bin/node`
- Code is semistandard compliant (version 16.x.x)
- All files are executable
- The length of each file is tested using `wc`
- No use of `var` is allowed

## Tasks

### Task 0: Rectangle #0

**File:** `0-rectangle.js`

Write an empty class `Rectangle` that defines a rectangle using class notation.

### Task 1: Rectangle #1

**File:** `1-rectangle.js`

Write a class `Rectangle` that defines a rectangle:
- The constructor takes 2 arguments `w` and `h`
- Initializes the instance attribute `width` with the value of `w`
- Initializes the instance attribute `height` with the value of `h`

### Task 2: Rectangle #2

**File:** `2-rectangle.js`

Enhance the `Rectangle` class:
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object

### Task 3: Rectangle #3

**File:** `3-rectangle.js`

Enhance the `Rectangle` class:
- Add a method `print()` that prints the rectangle using the character `X`

### Task 4: Rectangle #4

**File:** `4-rectangle.js`

Enhance the `Rectangle` class:
- Add methods `rotate()` and `double()`
  - `rotate()`: exchanges the width and the height of the rectangle
  - `double()`: multiples the width and the height of the rectangle by 2

### Task 5: Square #0

**File:** `5-square.js`

Write a class `Square` that defines a square and inherits from `Rectangle`:
- The constructor takes 1 argument `size`
- The constructor of `Rectangle` is called with `size` for both `width` and `height`

### Task 6: Square #1

**File:** `6-square.js`

Enhance the `Square` class:
- Add a method `charPrint(c)` that prints the square using the character `c`
  - If `c` is undefined, use the character `X`

### Task 7: Occurrences

**File:** `7-occurrences.js`

Write a function that returns the number of occurrences in a list:
- Prototype: `exports.nbOccurences = function (list, searchElement)`

### Task 8: Esrever

**File:** `8-esrever.js`

Write a function that returns the reversed version of a list:
- Prototype: `exports.esrever = function (list)`
- Do not use the built-in method `reverse`

### Task 9: Log me

**File:** `9-logme.js`

Write a function that prints the number of arguments already printed and the new argument value:
- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

### Task 10: Number conversion

**File:** `10-converter.js`

Write a function that converts a number from base 10 to another base passed as argument:
- Prototype: `exports.converter = function (base)`
- Do not declare any new variable (var, let, etc.)

## Usage

To run any of the scripts, make sure the file is executable:
```bash
chmod +x <filename>

