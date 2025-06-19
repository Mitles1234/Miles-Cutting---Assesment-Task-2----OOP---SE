# Dungeon Crawler Text Adventurer Program

This Python program allows you to see statistics, and equipment. 

## Features
- See users data such as health, stamina, and mana in the form of a bar.
- View a full map with where the player is at a given point on the map.
- Take inputs from the user and alerts the user if they incorrectly inputed information.
- Interact with an enaging store, and meet characters
- Battle Enemies through using a variety of weapons, and armour pieces
- Traverse a dense, and immersive world

## Requirements
To run this program, you need to install the following dependencies:

- `os` to effectively layout and update the terminal. 
- `math` to handle and maniplulate data. 
- `json` to interact with save data.
- `time` to allow for more unique elements of interacting with the GUI that invlove waiting.
- `random` to have elements of the game that can change and adapt between different runs, making for a unique experience every playthrough.
- `wcwidth` to allow the program to better understand and handle the Ascii characters, allowing for a more "GUI like" design

### Install dependencies
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt

### How to Play:

#### How to Interact:
The entire program uses simple number system, and descriptive titles to interact with the program.

NOTE: Many aspects of the UI are adaptive - meaning when you enter an input, rather than printing new text below, it might update previous text.

#### How to Start
When the program is loaded, their is 4 options for save files. This means you can have up to 4 runs, at any stage in the level. At the same time.

To select which save, pick from 1-4. Option 5 allows you to overwrite an existing save, and option 6 lets you leave the program.

Once this has happend, simply follow the prompts on screen, where you will enter your name, and begin your journey.