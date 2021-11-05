# <b>SUN BREAKER</b>
## <b> Démarrage rapide </b>
### <b> Description </b>
Sun breaker est un module permettant de chiffrer des chaînes de caractères vers du décimal sans qu’avec la sortie, l’entrée puise être retrouvée.
### <b> Installation </b>
Téléchargez le repository, et déplacez sunbreaker.py dans le dossier de votre programme.

### <b> Utilisation </b>
exemple 1:
```py
from sunbreaker import sunbreaker
print(sunbreaker("coucou"))
```
exemple 2:
```py
from sunbreaker import sunbreaker
entree = "coucou"
sortie = sunbreaker(entree))
print(sortie)
```
exemple 3:
```py
from sunbreaker import sunbreaker
entree = input("mot de passe: ")
sortie = sunbreaker(entree))
if sortie == 13116700427615401352081257131071408589073225: #break de "coucou"
    print("c'est bien vous!")
else:
    print("ce n'est pas vous!")
```
### <b>Génération rapide</b>
pour générer rapidement des breaks, vous pouvez utiliser testeur.py qui vous permet de tapé du texte et de le crypter


## <b> Algorithme </b>
Un petit schéma veau mieux qu’un long discours <i>:kappa:</i>
<img src="doc/algorithme.png">

## <b> Brut force et data base </b>

Rien de mieux pour tester un algorithme que de le mettre a rude épreuve car même si il est impossible (a causse des bits perdus) de retrouver l’entrée avec la sortie, on peut toujours testé toute les entrées avec le break. Pour sa le brut force est la 🤣.

Le programme brut-force/brut-force.py pemet ainsi de tester toutes les possibilité (avec des jeu de caractère différent).

Mais si plutôt que de devoirs généré toute les combinaison et de les crypté, on les enregistrerais dans un basse de données. brut-force/Mkdata.py le fait pour vous, et brut-force/finder.py permet de retrouvé les break dans les basse de données.

## <b> Doublon </b>

Le problème de crypté avec perte c’est que certaine des chaînes de caractère peuvent avoir le même break. En effet, 177339536549 et le break de:
```
 2f
 0<f
 0 f
 2p0
 100
 200
 0&0
 0<p0
 0 p0
 0 00
```

et oui...

Pour trouver ses cas particulier 2 programme ont été codé, brut-force/double/double.py (qui utilisé les data basse classique) et brut-force/double/double.cpp (avec des data base «simple» que vous trouverais dans brut-force/double/simple-data)

Voila les sorties que l’on peut avoir:

```
nombre d'apparition
|    break
|    |
V    V
2 - 608585
2 - 9509
2 - 608553
2 - 19472648
2 - 38947657
2 - 608585
2 - 9509
2 - 19939993866
3 - 20007102730
2 - 532773
2 - 674089
2 - 168101
2 - 40837179057420
2 - 40974620108044
4 - 40421124427
2 - 39884253515
2 - 146447292661572876
```

<b>Bonne chance et amusé vous bien!</b>

Mon serveur discord: https://discord.gg/PFbymQ3d97

<i>-pf4 </i>