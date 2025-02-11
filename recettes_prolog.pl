
% D�finition des recettes et de leurs ingr�dients
recette(pizza, [farine, eau, sel, levure, tomate, fromage]).
recette(salade, [laitue, tomate, concombre, vinaigre, huile]).
recette(pates_carbonara, [pates, creme, lardons, fromage, sel, poivre]).
recette(omelette, [oeufs, sel, poivre, fromage, herbes]).
recette(sandwich_jambon_beurre, [pain, beurre, jambon, salade]).

% R�gle pour v�rifier si tous les ingrédients d'une recette sont
% disponibles
recette_possible(Recette, IngredientsDisponibles) :-
    recette(Recette, IngredientsNecessaires),
    subset(IngredientsNecessaires, IngredientsDisponibles).

% Sous-ensemble : v�rifie si tous les �l�ments d'une liste sont dans
% une autre
subset([], _).
subset([X|XS], L) :- member(X, L), subset(XS, L).
