# Convertisseur de nombres en lettres (Français)

Ce projet est un script Python permettant de convertir n'importe quel nombre entier (jusqu'à 66 chiffres) en sa représentation en lettres en français.

---

## Fonctionnalités

* Conversion de nombres entiers en lettres (ex : `123` → `cent-vingt-trois`).
* Gestion des nombres négatifs (`-45` → `moins quarante-cinq`).
* Support des grands nombres avec les grandeurs (`millions`, `milliards`, etc.).
* Sortie lisible avec séparation des milliers.

---

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/elYoha17/chiffre_en_lettre.git
   ```

2. Se placer dans le dossier du projet :

   ```bash
   cd chiffre_en_lettre
   ```

3. Lancer le script :

   ```bash
   python main.py
   ```

---

## Utilisation

Le script vous demandera d'entrer un nombre entier.

Pour quitter la boucle interactive, tapez `exit`, `quit` ou `q`.

Exemples :

```
Entrez un nombre entier : 123
123 : cent-vingt-trois

Entrez un nombre entier : -456
-456 : moins quatre-cent-cinquante-six
```

---

## Structure du projet

* **main.py** : Script principal pour lancer le convertisseur en mode interactif.
* **constants.py** : Contient les dictionnaires `WORDS` et `MAGNITUDE_WORDS` ainsi que la logique de conversion.
* **README.md** : Documentation du projet.

---

## Limites

* Le script ne supporte que les nombres entiers.
* La limite maximale est `999...9` (66 chiffres).
* Les nombres à virgule ne sont pas pris en charge.

---

## Contribution

Les contributions sont les bienvenues !
Pour contribuer :

1. Forker le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b user-feature`)
3. Committer vos modifications (`git commit -am 'Ajout d'une fonctionnalité'`)
4. Pousser la branche (`git push origin user-feature`)
5. Créer un Pull Request

---

## Licence

Ce projet est sous licence MIT.
