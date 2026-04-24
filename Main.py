import csv
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ════════════════════════════════════════════════════════
#  1. READ CSV — works with ANY size file (Bonus 2)
# ════════════════════════════════════════════════════════
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

# ════════════════════════════════════════════════════════
#  2-4. CALCULATIONS
#  CA Brut = Prix × Quantite
#  CA Net  = CA Brut × (1 - Remise/100)
#  TVA     = CA Net × 20%
# ════════════════════════════════════════════════════════
def calculer(ventes):
    for v in ventes:
        v['CA_Brut'] = round(v['Prix'] * v['Quantite'], 2)
        v['CA_Net']  = round(v['CA_Brut'] * (1 - v['Remise'] / 100), 2)
        v['TVA']     = round(v['CA_Net'] * 0.20, 2)
        v['TTC']     = round(v['CA_Net'] + v['TVA'], 2)
    return ventes

# ════════════════════════════════════════════════════════
#  5. TOTAL CA
# ════════════════════════════════════════════════════════
def ca_total(ventes):
    return round(sum(v['CA_Net'] for v in ventes), 2)

def tva_totale(ventes):
    return round(sum(v['TVA'] for v in ventes), 2)

def ttc_total(ventes):
    return round(sum(v['TTC'] for v in ventes), 2)

# ════════════════════════════════════════════════════════
#  6. BEST PRODUCT
# ════════════════════════════════════════════════════════
def meilleur_produit(ventes):
    best = max(ventes, key=lambda v: v['CA_Net'])
    return best

# ════════════════════════════════════════════════════════
#  7. EXPORT resultats_final.csv
# ════════════════════════════════════════════════════════
def exporter(ventes, fichier):
    colonnes = ['ID','Prix','Quantite','Remise',
                'CA_Brut','CA_Net','TVA','TTC']
    with open(fichier, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(ventes)
    print(f"✅ Résultats exportés dans '{fichier}'")

# ════════════════════════════════════════════════════════
#  BONUS 1 — MATPLOTLIB CHARTS
# ════════════════════════════════════════════════════════
def afficher_graphiques(ventes):
    ids     = [str(v['ID'])  for v in ventes]
    ca_brut = [v['CA_Brut']  for v in ventes]
    ca_net  = [v['CA_Net']   for v in ventes]
    tva     = [v['TVA']      for v in ventes]

    fig, axes = plt.subplots(1, 3, figsize=(18, 7))
    fig.suptitle('Analyse des Ventes — PFA Automatisation',
             fontsize=16, fontweight='bold', y=0.98)

    # Chart 1 — CA Brut vs CA Net
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

    # Chart 2 — TVA par produit
    axes[1].bar(ids, tva, color='mediumseagreen')
    axes[1].set_title('Montant TVA par Produit')
    axes[1].set_xlabel('ID Produit')
    axes[1].set_ylabel('TVA (€)')
    axes[1].grid(axis='y', linestyle='--', alpha=0.5)

    # Chart 3 — Pie chart CA Net distribution
    colors = plt.cm.Set3.colors[:len(ids)]
    axes[2].pie(ca_net, labels=ids, autopct='%1.1f%%',
                colors=colors, startangle=140)
    axes[2].set_title('Répartition du CA Net par Produit')

    plt.subplots_adjust(top=0.88)
    plt.savefig('graphique_ca.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("✅ Graphiques sauvegardés dans 'graphique_ca.png'")

# ════════════════════════════════════════════════════════
#  BONUS 2 — DYNAMIC FILE READING
# ════════════════════════════════════════════════════════
def choisir_fichier():
    print("\n📂 Fichier utilisé : 'ventes.csv'")
    return 'ventes.csv'

# ════════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════════
def main():
    print("=" * 55)
    print("   PFA — Automatisation des Ventes")
    print("   Maher Zouari|Nadine Naoui |Amal Guebli")
    print("=" * 55)

    # Bonus 2 — dynamic file reading
    fichier = choisir_fichier()

    # 1. Read
    ventes = lire_ventes(fichier)
    if not ventes:
        return

    # 2-4. Calculate
    ventes = calculer(ventes)

    # 5. Display results
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

    # 6. Best product
    best = meilleur_produit(ventes)
    print(f"\n🏆 Meilleur produit : ID {best['ID']} "
          f"avec un CA Net de {best['CA_Net']:.2f} €")

    # 7. Export
    print("\n─── Export ──────────────────────────────────────────")
    exporter(ventes, 'resultats_final.csv')

    # Bonus 1 — charts
    print("\n─── Graphiques ──────────────────────────────────────")
    afficher_graphiques(ventes)

    print("\n" + "=" * 55)
    print("   ✅ Analyse terminée avec succès !")
    print("=" * 55)

if __name__ == "__main__":
    main()