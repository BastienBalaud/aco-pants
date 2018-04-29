# Fourmiale

[https://github.com/BastienBalaud/aco-pants](https://github.com/BastienBalaud/aco-pants)

Projet scolaire, de recherche de chemin le plus court pour parcourir les pubs de Grande Bretagne en utilisant algorithmes des colonies de fourmis. Cette version se limite au 208 pubs de Londres ce qui nécessite environ 30 secondes de calcul. Le temps de calcul étant exponentiel.

## Structure de données
Elle se limite à la récupération des coordonnées cartésienne nord et est.

## Fonction de fitness 
Utilisation du théorème de Pythagore

```python
distance = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)) / 1000
```

## Graphe

![out](img/out.png 'Graphe')

## Option du programme 
```
usage: ACOwithPants.py [-h] [-v] [-p]

optional arguments:
  -h, --help        show this help message and exit
  -v, --verbose     increase output verbosity
  -p, --parse_only  Only to test parser
```
