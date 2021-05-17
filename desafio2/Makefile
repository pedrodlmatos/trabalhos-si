PYTHON = python3

i ?= 0
n ?= 100

tinyMaze:
	cd search/; \
	${PYTHON} pacman.py -l tinyMaze -p SearchAgent -a fn=dfs


smallMaze:
	cd search/; \
	${PYTHON} pacman.py -l smallMaze -p SearchAgent -a fn=dfs


mediumMaze:
	cd search/; \
	${PYTHON} pacman.py -l mediumMaze -p SearchAgent -a fn=dfs


bigMaze:
	cd search/; \
	${PYTHON} pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z 0.8


random_tinyMaze:
	cd search; \
	i=$(i); \
	cost=0; \
	while [ $${i} -le $(n) ] ; do \
	  curr=$$(python3 pacman.py -l tinyMaze -p SearchAgent -a fn=dfs -q | awk 'NR==3 {print $$(NF-3)}'); \
	  cost=`expr $$cost + $$curr`; \
	  i=`expr $$i + 1`; \
  done; \
  echo "Medium cost for tinyMaze"; \
  echo "scale=2 ; $$cost / $(n)" | bc


random_smallMaze:
	cd search; \
	i=$(i); \
	cost=0; \
	while [ $${i} -le $(n) ] ; do \
	  curr=$$(python3 pacman.py -l smallMaze -p SearchAgent -a fn=dfs -q | awk 'NR==3 {print $$(NF-3)}'); \
	  cost=`expr $$cost + $$curr`; \
	  i=`expr $$i + 1`; \
  done; \
  echo "Medium cost for smallMaze"; \
  echo "scale=2 ; $$cost / $(n)" | bc


random_mediumMaze:
	cd search; \
	i=$(i); \
	cost=0; \
	while [ $${i} -le $(n) ] ; do \
	  curr=$$(python3 pacman.py -l mediumMaze -p SearchAgent -a fn=dfs -q | awk 'NR==3 {print $$(NF-3)}'); \
	  cost=`expr $$cost + $$curr`; \
	  i=`expr $$i + 1`; \
  done; \
  echo "Medium cost for mediumMaze"; \
  echo "scale=2 ; $$cost / $(n)" | bc


random_bigMaze:
	cd search; \
	i=$(i); \
	cost=0; \
	while [ $${i} -le $(n) ] ; do \
	  curr=$$(python3 pacman.py -l bigMaze -p SearchAgent -a fn=dfs -q | awk 'NR==3 {print $$(NF-3)}'); \
	  cost=`expr $$cost + $$curr`; \
	  i=`expr $$i + 1`; \
  done; \
  echo "Medium cost for bigMaze"; \
  echo "scale=2 ; $$cost / $(n)" | bc


