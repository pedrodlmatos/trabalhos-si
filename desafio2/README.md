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
