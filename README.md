---
title: "twitter-inflation-perception"
bibliography: references.bib
link-citations: true
---

# twitter-inflation-perception

## Objective

Last year was marked by rampant inflation, which keeps having a negative impact on the global economy as of today. Monitoring the evolution of inflation through precise measurement is thus a crucial matter for central banks and other institutions. 

Simply put, inflation rate is measured by comparing the current prices of a set of goods and services to previous prices. Inflation is generally calculated by statistical and economic institutions such as Insee and Banque de France. The latter also studies inflation perception through survey and social media analysis. Specifically, Banque de France has tried to gather insights on how people perceive and discuss inflation on social media, and to use this information to better understand their economic sentiments and expectations as in [[1]](#1). 

Inspired by this article, our project aims to measure inflation perception by analyzing Twitter data using Natural Language Processing (NLP) techniques. By leveraging the vast amount of text data available on Twitter, the project hopes to provide indicators that may be valuable to understand inflation dynamics. 

## Data collection

## Data preprocessing 

## Building an indicator of inflation perception


## References

<a id="1">[1]</a> 
Julien Denes & Ariane Lestrade & Lou Richardet, 2022.
"<B><A HREF="https://ideas.repec.org/h/bis/bisifc/57-13.html">Using twitter data to measure inflation perception</A></B>,"
<A HREF="https://ideas.repec.org/s/bis/bisifc.html">IFC Bulletins chapters</A>, in:  Bank for International Settlements (ed.), <A HREF="/b/bis/bisifb/57.html">Machine learning in central banking</A>, volume 57,
Bank for International Settlements.

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