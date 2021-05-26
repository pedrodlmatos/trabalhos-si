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


#### Step 1 - Depth-first search

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

#### Step 2 - Breadth-first search


#### Step 3 - Uniform cost search

Parâmetros:
 - `-p` - `SearchAgent`
 - `-a` - `fn=dfs`

Execução no terminal (dentro do diretório search):
 - `python3 pacman.py -l map -p SearchAgent -a fn=ucs`
    
Execução usando make (na raíz):
 - `make ucs_map`

Em todas as situações, substituir `map` por um dos mapas.


