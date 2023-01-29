# twitter-inflation-perception

## TODO

1. Classifieur pour identifier les tweets traitant des prix
2. Voir méthode pour identifier la direction des prix (classifieur, identification par mots-clef) 
3. Construction de l'indicateur (nombre de tweets traitant des prix, sentiment)
4. Evaluation de l'indicateur à partir des données d'inflation observée

## Ressources 

- Articles Medium NLP : [ici](https://medium.com/@p.emmanuel.diot/list/nlp-twitter-0fdb53596aeb)
- Librairie `Scweet`: [PyPI](https://pypi.org/project/Scweet/) + [github](https://github.com/Altimis/Scweet)


## Plan

1. Collecte par mots clés
    - `twint`
    - `tweepy`
    - [`TweetScraper`](https://github.com/jonbakerfish/TweetScraper)

2. Text exploration
    - Fréquence des mots 
    - Evolution dans le temps

3. Text preprocessing
    - Voir TP
    - word2vec

4. Filtration
    - Vérifier que les tweets traitent des prix / inflation 
    - Voir *"Using twitter data to measure inflation perception"*, Julien Denes 
    - Modèle de classification binaire : $y=1$ si le tweet traite du sujet des prix, 0 sinon
    - Semi supervised learning / Active learning

4. Mesure de la direction des prix (sur les tweets classés comme 1 à l'étape 3)
    - Classification binaire : $y=1$ si le tweet traite d'augmentation de prix, 0 sinon
    - Classification multi-label (inflation, deflation, stagflation, stability)
    - Semi supervised learning / Active learning
    - Sentiment analysis (RNN, gtp3, etc.) 
        - score de positivité (faible inflation) / négativité (forte inflation)
        - utiliser un [dictionnaire](https://journodev.tech/blog-12-main-dictionaries-for-sentiment-analysis/) de mots positifs et négatifs et compter leur occurrence

5. Construction de l'indicateur 
    - Aggrégation des scores construits à l'étape 4 par jour / semaine / mois

## Bonus

- Analyse de la performance de notre indicateur (comparaison aux courbes d'inflation, corrélations)
- Modèle économétrique d'estimation de l'inflation classique $\rightarrow$ évaluer la contribution de l'indicateur de perception d'inflation

## Instal virtual environment

```
> python -m venv env
> env\Scripts\activate.bat 
> pip install -r requirements.txt
```