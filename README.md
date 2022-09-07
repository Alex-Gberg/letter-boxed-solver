# Letter Boxed Solver
> This program solves the New York Times Letter Boxed game

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)


## General Information
- Given the Letter Boxed letters this program finds a solution in as few words as possible
- The current implementation uses a greedy algorithm

## Technologies used
- Python 3.8.10

## Features
- Input the letters in the terminal
- Receive the solution as a sequence of words which you can input into the Letter Boxed game

## Setup
- Use `python3 letterBoxedSolver.py` to run the program

## Usage
- Input the letters as prompted, you will be asked to input one side of the box at a time
- Input the letters for one side altogether (example: "abc")
- The program will then print the solution sequence 

## Project Status
The project is still ongoing

## Room for Improvement
- The solver could be made more automatic by retrieving letters automatically and autotyping the solution
- A new algorithm is needed as the greedy algorithm does not always find the optimal solution
- The dictionary needs to be refined as sometimes the solution includes words that the New York Times does not consider valid


## Acknowledgements
- The list of English words `filtered_words.txt` comes from [here](https://github.com/dwyl/english-words) and was filtered using [pyenchant](https://pypi.org/project/pyenchant/)
