# Welcome to UU-Game

The UU-game project is a collaborative git development of the quarto game using Agile SCRUM methodologies for the 1DL251 Software Engineering and Project Management course held at Uppsala University in Spring 2019. The game supports local and online single and tournament matches between users and AI players of easy, medium, and hard difficulty. It is developed as three separate integrated components, each implemented in Python:
- game engine for modifying game state and automating AI game-play using the minimax algorithm
- game platform for coordinating and displaying game-play between users and AI players
- communication platform for local and online, single and tournament game management

Easy AI difficulty should never win against hard AI difficulty, while medium AI should mostly win against easy AI, and hard AI mostly win against medium AI but never against itself. Traditionally, there are sixteen game pieces split between two equal number of colours, but instead of shapes, these are represented using lower and uppercase chars because game-play is displayed and user input is processed using a CLI.

## Development Team

 * [Viktor Enzell](https://github.com/viktor-enzell)
 * [Gustav From](https://github.com/GustavFrom)
 * [Maxime Gaide](https://github.com/Sravoryk-fork)
 * [Pelle Ingvast](https://github.com/Pallekan) 
 * [Laurin Kerle](https://github.com/LaurinKerle)
 * [Adam Ross](https://github.com/R055A)

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
