# Analyse des facteurs de risque du Diabète (Dataset Pima Indians)

##  Présentation du projet
Ce projet personnel vise à analyser les indicateurs de santé (Glucose, IMC, Âge) pour identifier les corrélations avec le diagnostic du diabète. 
C'est une première approche de la **Data Science appliquée au secteur médical**.

##  Technologies utilisées
  **Python 3.x**
  **Pandas** : Manipulation et nettoyage des données.
  **Matplotlib** : Visualisation statistique.

##  Résultats clés
* Mise en évidence d'un taux de glucose moyen de **141 mg/dL** chez les patients diabétiques contre **110 mg/dL** chez les patients sains.
* Identification visuelle d'un cluster de risque élevé chez les patients de plus de 45 ans avec un IMC > 30.

##  Comment lancer le projet?
1. Installer les dépendances : `pip install pandas matplotlib`
2. Lancer le script : `python data_sante.py`

3. <img width="983" height="629" alt="image" src="https://github.com/user-attachments/assets/a9366a2c-b8e7-42a0-a8ad-338154ed190a" />

L'analyse de ce dataset met en lumière deux indicateurs critiques dans le dépistage du diabète : le taux de glucose à jeun et l'Indice de Masse Corporelle (IMC).
Les données confirment une corrélation forte entre un glucose > 140 mg/dL et la présence de la pathologie, représentant le seuil d'alerte et validant l'importance du suivi glycémique préventif.
L'observation de clusters montre que le risque est démultiplié chez les patients de plus de 45 ans présentant une surcharge pondérale, ce qui souligne l'intérêt du score de risque combiné plutôt que de l'analyse d'un facteur isolé.
Ce type d'analyse descriptive est la première étape vers la médecine prédictive, permettant d'anticiper les complications et d'adapter les parcours de soins de manière personnalisée.
