BACKUP = "backup/tweets/"

ECONOMICAL_TERMS = [
    "inflation", 
    "deflation",
    "stagflation",
    "desinflation",
    "inflationniste", 
    "deflationniste",
    "antiinflationniste", 
    "antideflationniste", 
    "IPC", 
    "IPCH"
]

PRICES = [
    "prix", 
    "tarif", 
    "montant", 
    "coût", 
    "loyer", 
    "vente", 
    "achat", 
    "location", 
    "frais", 
    "abonnement", 
    "facture", 
    "coûter", 
    "facturer", 
    "payer", 
    "tarifer", 
    "vendre", 
    "devis", 
    "paiement", 
    "rabais", 
    "tarifaire", 
    "croissance", 
    "promotion", 
    "remise", 
    "ristourne"
]

EXPENSIVE = [
    "onéreux", 
    "cher", 
    "prohibitif", 
    "couteux", 
    "élevé", 
    "exorbitant", 
    "inabordable",
    "conséquent",
    "inaccessible", 
    "excessif", 
    "anormal", 
    "dispendieux", 
    "arnaque",
    "arnaquer", 
    "ruineux", 
    "faramineux", 
    "hors de portée", 
    "rondelette", 
    "inconcevable", 
    "rédhibitoire"
]

CHEAP = [
    "faible", 
    "modique", 
    "avantageux", 
    "brader", 
    "imbattable", 
    "dérisoire", 
    "alléchant", 
    "réduit", 
    "occase", 
    "occasion", 
    "défiant toute concurrence", 
    "aubaine", 
    "modeste", 
    "clopinettes", 
    "bon prix", 
    "attrayant", 
    "clopinette", 
    "abordable", 
    "raisonnable", 
    "compétitif", 
    "accessible", 
    "acceptable", 
    "normaux", 
    "moyen", 
    "équitable", 
    "intéressant", 
    "convenable", 
    "négligeable"
]

INSTITUTIONS = [
    "BCE", 
    "banque centrale", 
    "banque central", 
    "Banque de France", 
    "INSEE", 
    "FED", 
    "taux directeur", 
    "taux intérêt"
]

ENGLISH = [
    "price", 
    "prices", 
    "cost", 
    "costs", 
    "rent", 
    "rents", 
    "bill",
    "bills"
]

CONFIG = {
    "ECONOMICAL_TERMS": {"keywords": ECONOMICAL_TERMS, "max_tweets": 100, "file_name": "econ_terms"}, 
    "PRICES": {"keywords": PRICES, "max_tweets": 100, "file_name": "prices"}, 
    "EXPENSIVE": {"keywords": EXPENSIVE, "max_tweets": 50, "file_name": "expensive"}, 
    "CHEAP": {"keywords": CHEAP, "max_tweets": 50, "file_name": "cheap"}, 
    "INSTITUTIONS": {"keywords": INSTITUTIONS, "max_tweets": 50, "file_name": "institutions"}, 
    "ENGLISH": {"keywords": ENGLISH, "max_tweets": 10, "file_name": "english"}, 
}