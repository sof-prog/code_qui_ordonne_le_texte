import re
import os

# Texte désordonné avec des erreurs
texte_desordonne = (
    "La programmation est une compétence essentielle dans le monde d'aujourd'hui elle nous "
    "permet de résoudre des problèmes complexes et d'automatiser des tâches. Les langages de "
    "programmation comme Python Java et C++ sont largement utilisés dans l'industrie du logiciel. "
    "En apprenant à programmer on développe également sa logique et sa créativité. De plus la "
    "technologie évolue rapidement ce qui rend cette compétence encore plus importante pour les "
    "futurs professionnels. En conclusion apprendre à programmer est un investissement précieux pour "
    "l'avenir."
)

# Identification des erreurs : manque de virgules et d'espaces
erreurs = []

# Vérification du manque de virgules avant les conjonctions (et, ou, mais)
conjonctions = re.findall(r'\b(mais|et|ou)\b', texte_desordonne)
for conjonction in conjonctions:
    # Si la conjonction n'est pas précédée d'une virgule
    if re.search(rf'(?<!\.\s)(\S+)\s+{conjonction}', texte_desordonne):
        erreurs.append(f"Manque de virgule avant '{conjonction}'")

# Vérification des espaces
mauvais_espaces = re.findall(r'\s+[,.!?;]', texte_desordonne)  # Espace avant une ponctuation
if mauvais_espaces:
    erreurs.append("Mauvais espaces avant la ponctuation.")

# Ajout des virgules et correction des espaces
texte_corrige = (
    "La programmation est une compétence essentielle dans le monde d'aujourd'hui, elle nous "
    "permet de résoudre des problèmes complexes et d'automatiser des tâches. Les langages de "
    "programmation comme Python, Java et C++ sont largement utilisés dans l'industrie du logiciel. "
    "En apprenant à programmer, on développe également sa logique et sa créativité. De plus, la "
    "technologie évolue rapidement, ce qui rend cette compétence encore plus importante pour les "
    "futurs professionnels. En conclusion, apprendre à programmer est un investissement précieux pour "
    "l'avenir."
)

# Création du fichier et sauvegarde des résultats
nom_fichier = 'texte_corrige_et_erreurs.txt'
with open(nom_fichier, 'w') as fichier:
    fichier.write("Erreurs détectées :\n")
    for erreur in erreurs:
        fichier.write(f"- {erreur}\n")
    fichier.write("\nTexte corrigé :\n")
    fichier.write(texte_corrige)

# Message de confirmation
print(f"Le fichier '{nom_fichier}' a été créé avec succès dans le répertoire actuel.")
