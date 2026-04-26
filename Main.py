import csv
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def generer_ventes_csv(fichier='ventes.csv'):
    donnees = [
        ['ID', 'Prix', 'Quantite', 'Remise'],
        [101, 15.0, 3, 10],
        [102, 25.0, 2, 5],
        [103, 10.0, 5, 0],
        [104, 50.0, 1, 20],
        [105, 30.0, 4, 15],
        [106, 45.0, 3, 10],
        [107, 20.0, 6, 0],
        [108, 60.0, 2, 25],
        [109, 35.0, 4, 5],
        [110, 80.0, 1, 30],
    ]
    
    with open(fichier, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(donnees)
    
    print(f"✅ Fichier '{fichier}' généré automatiquement avec {len(donnees)-1} produits.") 
def lire_ventes(fichier):
    if not os.path.exists(fichier):
        print(f"❌ Erreur : Le fichier '{fichier}' est introuvable.")
        return []
    ventes = []
    with open(fichier, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ventes.append({
                'ID'      : int(row['ID']),
                'Prix'    : float(row['Prix']),
                'Quantite': int(row['Quantite']),
                'Remise'  : float(row['Remise'])
            })
    print(f"✅ {len(ventes)} produits chargés depuis '{fichier}'")
    return ventes

def calculer(ventes):
    for v in ventes:
        v['CA_Brut'] = round(v['Prix'] * v['Quantite'], 2)
        v['CA_Net']  = round(v['CA_Brut'] * (1 - v['Remise'] / 100), 2)
        v['TVA']     = round(v['CA_Net'] * 0.20, 2)
        v['TTC']     = round(v['CA_Net'] + v['TVA'], 2)
    return ventes

def ca_total(ventes):
    return round(sum(v['CA_Net'] for v in ventes), 2)

def tva_totale(ventes):
    return round(sum(v['TVA'] for v in ventes), 2)

def ttc_total(ventes):
    return round(sum(v['TTC'] for v in ventes), 2)

def meilleur_produit(ventes):
    best = max(ventes, key=lambda v: v['CA_Net'])
    return best

def exporter(ventes, fichier):
    colonnes = ['ID','Prix','Quantite','Remise',
                'CA_Brut','CA_Net','TVA','TTC']
    with open(fichier, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(ventes)
    print(f"✅ Résultats exportés dans '{fichier}'")

def afficher_graphiques(ventes):
    ids     = [str(v['ID'])  for v in ventes]
    ca_brut = [v['CA_Brut']  for v in ventes]
    ca_net  = [v['CA_Net']   for v in ventes]
    tva     = [v['TVA']      for v in ventes]

    fig, axes = plt.subplots(1, 3, figsize=(18, 7))
    fig.suptitle('Analyse des Ventes — PFA Automatisation',
             fontsize=16, fontweight='bold', y=0.98)

    x = range(len(ids))
    width = 0.35
    axes[0].bar([i - width/2 for i in x], ca_brut,
                width, label='CA Brut', color='steelblue')
    axes[0].bar([i + width/2 for i in x], ca_net,
                width, label='CA Net',  color='darkorange')
    axes[0].set_title('CA Brut vs CA Net par Produit')
    axes[0].set_xlabel('ID Produit')
    axes[0].set_ylabel('Montant (€)')
    axes[0].set_xticks(list(x))
    axes[0].set_xticklabels(ids)
    axes[0].legend()
    axes[0].grid(axis='y', linestyle='--', alpha=0.5)

    axes[1].bar(ids, tva, color='mediumseagreen')
    axes[1].set_title('Montant TVA par Produit')
    axes[1].set_xlabel('ID Produit')
    axes[1].set_ylabel('TVA (€)')
    axes[1].grid(axis='y', linestyle='--', alpha=0.5)

    colors = plt.cm.Set3.colors[:len(ids)]
    axes[2].pie(ca_net, labels=ids, autopct='%1.1f%%',
                colors=colors, startangle=140)
    axes[2].set_title('Répartition du CA Net par Produit')

    plt.subplots_adjust(top=0.88)
    plt.savefig('graphique_ca.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("✅ Graphiques sauvegardés dans 'graphique_ca.png'")

def choisir_fichier():
    print("\n📂 Fichier utilisé : 'ventes.csv'")
    return 'ventes.csv'

def main():
    print("=" * 55)
    print("   PFA — Automatisation des Ventes")
    print("   Maher Zouari|Nadine Naoui |Amal Guebli")
    print("=" * 55)

    generer_ventes_csv()

    fichier = choisir_fichier()

    ventes = lire_ventes(fichier)
    if not ventes:
        return

    ventes = calculer(ventes)

    print("\n─── Résultats par Produit ───────────────────────────")
    print(f"{'ID':<6} {'Prix':>8} {'Qté':>5} {'Remise':>8} "
          f"{'CA Brut':>10} {'CA Net':>10} {'TVA':>8} {'TTC':>10}")
    print("─" * 55)
    for v in ventes:
        print(f"{v['ID']:<6} {v['Prix']:>8.2f} {v['Quantite']:>5} "
              f"{v['Remise']:>7.0f}% {v['CA_Brut']:>10.2f} "
              f"{v['CA_Net']:>10.2f} {v['TVA']:>8.2f} {v['TTC']:>10.2f}")

    print("─" * 55)
    print(f"\n💰 CA Total (HT)  : {ca_total(ventes):.2f} €")
    print(f"🧾 TVA Totale     : {tva_totale(ventes):.2f} €")
    print(f"💳 Total TTC      : {ttc_total(ventes):.2f} €")

    best = meilleur_produit(ventes)
    print(f"\n🏆 Meilleur produit : ID {best['ID']} "
          f"avec un CA Net de {best['CA_Net']:.2f} €")

    print("\n─── Export ──────────────────────────────────────────")
    exporter(ventes, 'resultats_final.csv')

    print("\n─── Graphiques ──────────────────────────────────────")
    afficher_graphiques(ventes)

    print("\n" + "=" * 55)
    print("   ✅ Analyse terminée avec succès !")
    print("=" * 55)

if __name__ == "__main__":
    main()