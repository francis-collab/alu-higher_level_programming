# JavaScript - Web jQuery

This repository contains JavaScript scripts that use jQuery to interact with APIs, manipulate the DOM, and enhance web pages dynamically.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
  - [0. No jQuery](#0-no-jquery)
  - [1. With jQuery](#1-with-jquery)
  - [2. Click and turn red](#2-click-and-turn-red)
  - [3. Add `.red` class](#3-add-red-class)
  - [4. Toggle classes](#4-toggle-classes)
  - [5. Append new item](#5-append-new-item)
  - [6. Change the header](#6-change-the-header)
  - [7. Star Wars character](#7-star-wars-character)
  - [8. Star Wars movies](#8-star-wars-movies)
  - [9. Say Hello!](#9-say-hello)

## Description
This project explores how to use jQuery for DOM manipulation and AJAX requests. The scripts dynamically update elements, fetch data from APIs, and modify webpage content in response to user actions.

## Installation
To use the scripts, ensure you have jQuery included in your HTML files. You can use the following CDN:
```html
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
```

## Usage
Each script should be linked in an HTML file as specified in the respective tasks. Open the HTML file in a browser to see the effects.

## Tasks

### 0. No jQuery
**File:** `0-script.js`
- Selects `header` and updates its color to `#FF0000` using vanilla JavaScript.

### 1. With jQuery
**File:** `1-script.js`
- Uses jQuery to change the color of the `header` to `#FF0000`.

### 2. Click and turn red
**File:** `2-script.js`
- Changes the text color of `header` to red when the user clicks on `DIV#red_header`.

### 3. Add `.red` class
**File:** `3-script.js`
- Adds the `.red` class to `header` when `DIV#red_header` is clicked.

### 4. Toggle classes
**File:** `4-script.js`
- Toggles between `.red` and `.green` classes for `header` when `DIV#toggle_header` is clicked.

### 5. Append new item
**File:** `5-script.js`
- Adds a new `<li>` item to `UL.my_list` when `DIV#add_item` is clicked.

### 6. Change the header
**File:** `6-script.js`
- Updates the `header` text to `New Header!!!` when `DIV#update_header` is clicked.

### 7. Star Wars character
**File:** `7-script.js`
- Fetches and displays the name of a Star Wars character from the API: `https://swapi-api.alx-tools.com/api/people/5/?format=json`.

### 8. Star Wars movies
**File:** `8-script.js`
- Fetches and lists all Star Wars movie titles from `https://swapi-api.alx-tools.com/api/films/?format=json`.
- Adds them to the `UL#list_movies` element.

### 9. Say Hello!
**File:** `9-script.js`
- Fetches a greeting in French (`hello`) from `https://fourtonfish.com/hellosalut/?lang=fr` and displays it in `DIV#hello`.

## Author
This project was completed by Francis
