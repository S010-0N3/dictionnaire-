students = ["Thomas","Matt","Sarah","Nina"]
scores = [10,15,17,13]

index = [0,1,2,3]
name ="Thomas"
score = 0

#j'ai creer une boucle for qui recherche dans le dictionnaire la note du Nom que j'ai mis.
for i in index:
  if students[i] == name:
    score=scores[i]
print(score)

scores = {} #dictionnaire vide
#ajoute un element au dictionnaire en vrai...
#entre crochet la cle "keys" et le resultat "values"
scores["Nina"]= 13
scores["Fally"]= 20
scores["Eric"]= 3
scores["Sol"]= 6

print(scores)

#dictionnaire pre-remplie
animals ={"lion": 30,"coq": 2,"serpent": 45}
print(animals)

#je peux en modifier les valeur :
animals["lion"] = 45
print(animals)
animals["lion"] = animals["lion"]- 34
print(animals)

#affiche les cles d'un dictionnaire :
fiche = {"nom":"Wayne", "prenom":"Bruce"}
for cle in fiche.keys():
  print(cle)

#affiche la valeur dun dictionnaire
fiche = {"nom":"Wayne", "prenom":"Bruce"}
for valeur in fiche.values():
  print(valeur)


#exercies 

scores["Marie"]= 15
scores["Nina"]= scores["Nina"] +2
scores["Sol"] = 10

#je verifie la presence dans mon dictionnaire
matt_found = "Matt" in scores
sol_found = "Sol" in scores

print(matt_found)
print(sol_found)
print(scores)