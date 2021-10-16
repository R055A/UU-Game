# Welcome to UU-Game

Group software engineering project for collaborative Agile project management and git development of the quarto game for the 1DL251 Software Engineering and Project Management course held at Uppsala University. The game supports local and online single and tournament matches between users and AI players of easy, medium, and hard difficulty. It is implemented in Python with unit testing using the PyCharm IDE and is developed as three separate integrated components:
- game engine for modifying game state and automating AI game-play using the minimax algorithm
- game platform for coordinating and displaying game-play between users and AI players
- communication platform for local and online, single and tournament game management

Easy AI difficulty never wins against hard AI difficulty, while medium AI mostly wins against easy AI, and hard AI mostly wins against medium AI. Traditionally, there are sixteen game pieces split between two equal number of colours, but instead of shapes, these are represented using lower and uppercase chars because game-play is displayed and user input is processed with a CLI.

## Development Team

 * [Enzell, Viktor](https://github.com/viktor-enzell)
 * [From, Gustav](https://github.com/GustavFrom)
 * [Gaide, Maxime](https://github.com/Sravoryk-fork)
 * [Ingvast, Pelle](https://github.com/Pallekan) 
 * [Kerle, Laurin](https://github.com/LaurinKerle)
 * [Ross, Adam](https://github.com/R055A)

## Instructions

### Requirements

* [Python3](https://www.python.org/download/releases/3.0/)

## Test

###### CLI

Navigate to the `UU-Game/` directory and enter:

```
python3 -m unittest
```

## Run

###### CLI

Navigate to the `UU-Game/` directory and enter:

```
Python3 uu_game.py
```
