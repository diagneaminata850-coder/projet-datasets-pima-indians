import pandas as pd  
import matplotlib.pyplot as plt  


url_donnees = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
noms_colonnes = [
    'Grossesses', 'Glucose', 'Tension', 'Epaisseur_Peau', 
    'Insuline', 'IMC', 'Pedigree_Diabete', 'Age', 'Resultat'
]

df = pd.read_csv(url_donnees, names=noms_colonnes)

print("--- APERÇU DES 5 PREMIERS PATIENTS ---")
print(df.head())
print("\n")


# On veut savoir si le glucose est plus élevé chez les malades
# On groupe par la colonne 'Resultat' (0 = Sain, 1 = Diabétique)
# Puis on calcule la moyenne (.mean) de la colonne 'Glucose'
analyse_glucose = df.groupby('Resultat')['Glucose'].mean()

print("MOYENNE DU TAUX DE GLUCOSE")
print(f"Groupe Sain (0) : {analyse_glucose[0]:.2f}")
print(f"Groupe Diabétique (1) : {analyse_glucose[1]:.2f}")
print("Interprétation : Le taux de sucre est nettement plus élevé chez les malades.")
print("\n")


# On cherche le nombre de patients de plus de 50 ans
plus_de_50_ans = df[df['Age'] > 50] 
nb_patients = plus_de_50_ans.shape[0] 

print(f"Nombre de patients de plus de 50 ans dans l'étude : {nb_patients}")
print("\n")

#VISUALISATION
# On trace un nuage de points : Âge  Glucose
plt.figure(figsize=(10, 6)) 
plt.scatter(df['Age'], df['Glucose'], c=df['Resultat'], cmap='coolwarm', alpha=0.7)


plt.title("Analyse du Diabète : Lien entre Âge et Glucose")
plt.xlabel("Âge du patient")
plt.ylabel("Taux de Glucose")
plt.grid(True, linestyle='--', alpha=0.5 ) 

print("Génération du graphique en cours...")
plt.show() 