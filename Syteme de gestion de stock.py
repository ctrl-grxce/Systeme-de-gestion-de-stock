class Produit:
    def __init__(self, nom, ID, prix_achat, prix_vente, quantite, seuil_minimum):
        self.nom = nom
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.quantite = quantite
        self.seuil_minimum = seuil_minimum
        self.ID = ID
    def affichier_infos(self):
        print(f"Nom: {self.nom}")
        print(f"ID: {self.ID}")
        print(f"Prix d'achat: {self.prix_achat}")
        print(f"Prix de vente: {self.prix_vente}")
        print(f"Quantité: {self.quantite}")
        print(f"Seuil minimum: {self.seuil_minimum}")
    def dire_stock_bas(self):
        if self.quantite < self.seuil_minimum:
            print(f"Le stock de {self.nom} est bas")
        else:
            print(f"Le stock de {self.nom} est suffisant")
    def augmenter_produit(self, quantite):
        self.quantite += quantite
    def diminuer_produit(self, quantite):
        self.quantite -= quantite
class stock:
    def __init__(self, produits, quantite):
        self.produits = produits
        self.quantite = quantite
    produits = {}
    def ajouter_produit(self, produit, quantite):
        self.produits[produit] = quantite
    def retirer_produit(self, produit, quantite):
        self.produits[produit] -= quantite
    def chercher_produit(self, nom, ID):
        for produit in self.produits:
            if produit.nom == nom and produit.ID == ID:
                return produit
        return None
    def affichier_stock(self):
        for produit, quantite in self.produits.items():
            print(f"{produit}: {quantite}")
    def verifier_stock_bas(self):
        for produit, quantite in self.produits.items():
            if quantite < produit.seuil_minimum:
                print(f"Le stock de {produit} est bas")
            else:
                print(f"Le stock de {produit} est suffisant")
    def verifier_stock_suffisant(self):
        for produit, quantite in self.produits.items():
            if quantite >= produit.seuil_minimum:
                print(f"Le stock de {produit} est suffisant")   






    