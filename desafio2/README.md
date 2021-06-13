# Sistemas Inteligentes - Desafio 2

## PacMan - Algoritmos de pesquisa

Desafio desenvolvido no âmbito da unidade curricular de Sistemas Inteligentes com o objetivo de desenvolver 
algoritmos de pesquisa para o jogo PacMan.

## Utilização

Instalar o package tkinter (se necessário):
`sudo apt-get install python3-tk`

Mudar para o diretório:
`cd search`

`python3 pacman.py`

### Parâmetros

Layout: `-l` ou `--layout`
 - testMaze
 - tinyMaze
 - mediumMaze
 - mediumDottedMaze
 - mediumScaryMaze  
 - bigMaze
 - tinyCorners
 - mediumCorners
 - testSearch
 - trickySearch
 - bigSearch

Agente: `-p` ou `--pacman`
 - GoWestAgent
 - SearchAgent
 - StayEastSearchAgent
 - StayWestSearchAgent
 - AStarCornersAgent
 - AStarFoodSearchAgent
 - ClosestDotSearchAgent
 - ApproximateSearchAgent

Argumentos do agente: `-a` ou `--agentArgs`
 - fn=tinyMazeSearch
 - fn=bfs
 - fn=ucs
 - fn=astar,heuristic=manhattanHeuristic
 - fn=bfs,prob=CornersProblem

Ghosts: `-g` ou `--ghosts`

Número de ghosts: `-k` ou `--numghosts`

Timeout: `-t` ou `--timeout`

Exemplos:

 - `python3 pacman.py -p GoWestAgent` ou `python3 pacman.py --pacman GoWestAgent`
 - `python3 pacman.py -l testMaze -p SearchAgent` ou `python3 pacman.py --layout testMaze --pacman SearchAgent`

### Step 1 - Depth-first search

Parâmetros:
 - `-p` - `Search agent`
 - `-a` - `fn=dfs`

Execução no terminal (dentro do diretório search):
 - `python3 pacman.py -l map -p SearchAgent -a fn=dfs`
    
Execução usando make (na raíz):
 - `make map`

Para avaliar a influência da ordem:
 - remover a linha comentada que altera a ordem (linha 111)
 - `make random_map`

Em todas as situações, substituir `map` por um dos mapas.


### Step 2 - Breadth-first search

Parâmetros:
 - `-p` - `SearchAgent`
 - `-a` - `fn=bfs`

Execução no terminal (dentro do diretório search):
 - `python3 pacman.py -l map -p SearchAgent -a fn=ucs`


### Step 3 - Uniform cost search

Parâmetros:
 - `-p` - `SearchAgent`
 - `-a` - `fn=dfs`

Execução no terminal (dentro do diretório search):
 - `python3 pacman.py -l map -p SearchAgent -a fn=ucs`

Substituir `map` por um dos mapas.


### Step 4 - A*

Parâmetros:
 - `-p` - `SearchAgent`
 - `-a` - `fn=astar`, `fn=astar,heuristic=manhattanHeuristic`

Execução no terminal (dentro do diretório search):
 - `python3 pacman.py -l map -p SearchAgent -a fn=ucs`

Substituir `map` por um dos mapas

### Step 5 - Corners Problem

Parâmetros:
 - `-l`
    - `tinyCorners`
    - `mediumCorners`
    - `bigCorners`
- `-p`: `SearchAgent`
- `-a` 
    - `fn=dfs,prob=CornersProblem`
    - `fn=bfs,prob=CornersProblem`
    - `fn=ucs,prob=CornersProblem`
    - `fn=astar,prob=CornersProblem,heuristic=nullHeurisitc`
    - `fn=astar,prob=CornersProblem,heuristic=manhattanHeuristic`

Execução no terminal
 - `python3 pacman.py -l map -p SearchAgent -a args`

### Step 6 - Corners Heuristic

Parâmetros:
 - `-l`:
    - `tinyCorners`
    - `mediumCorners`
    - `bigCorners`

- `-p`:
    - `SearchAgent`
    - `AStarCornersAgent` - forma abreviada de definir o agente como:
        `-p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic`
- `a` (para o caso de definir o agent como `SearchAgent`):
    - `fn=dfs,prob=CornersProblem`
    - `fn=bfs,prob=CornersProblem`
    - `fn=ucs,prob=CornersProblem`
    - `fn=astar,prob=CornersProblem,heuristic=cornersHeuristic`

Execução no terminal
- `python3 pacman.py -l map -p SearchAgent -a args`
- `python3 pacman.py -l map -p AStarSearchAgent`


### Step 7 - Food Heuristic

Parâmetros:
 - `-l`:
    - `testSearch`
    - `tinySearch`
    - `trickySearch`
    - `smallSearch`

- `-p`:
    - `SearchAgent`
    - `AStarFoodSearchAgent`
- `a` (para o caso de definir o agent como `SearchAgent`):
    - `fn=dfs,prob=FoodSearchProblem`
    - `fn=bfs,prob=FoodSearchProblem`
    - `fn=ucs,prob=FoodSearchProblem`
    - `fn=astar,prob=FoodSearchProblem,heuristic=nullHeuristic`
    - `fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic`

Execução no terminal
- `python3 pacman.py -l map -p SearchAgent -a args`
- `python3 pacman.py -l map -p AStarFoodSearchAgent`

### Step 8 - Closest dot search agent

Parâmetros:
 - `-l`:
    - `mediumSearch`
    - `bigSearch`

- `-p`:
    - `ClosestSearchAgent`

Execução no terminal
- `python3 pacman.py -l map -p ClosestDotSearchAgent`
