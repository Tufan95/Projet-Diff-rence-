# Définition des recettes et de leurs ingrédients
recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "pates_carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "sandwich_jambon_beurre": ["pain", "beurre", "jambon", "salade"]
}

# Fonction fonctionnelle utilisant filter pour trouver les recettes réalisables
def trouver_recettes_fonctionnelles(ingredients_utilisateur):
    recettes_possibles = filter(lambda recette: set(recettes[recette]).issubset(set(ingredients_utilisateur)), recettes)
    return list(recettes_possibles)

# Exemple d'appel
ingredients_utilisateur = ["farine", "eau", "sel", "levure", "tomate", "fromage"]
recettes_suggerees = trouver_recettes_fonctionnelles(ingredients_utilisateur)
print("Recettes possibles:", recettes_suggerees)
