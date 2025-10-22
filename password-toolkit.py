#!/usr/bin/env python3
"""
Password Toolkit (version interactive)
Auteur : Kenneth OUSSOU LIO
But : Vérifier ou générer des mots de passe depuis un menu simple.
"""

import string
import secrets

def check_password(pw: str) -> tuple:
    """Évalue un mot de passe et retourne (score, conseils_list)."""
    score = 0
    conseils = []

    # Critère 1 : longueur
    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        conseils.append("Allonger le mot de passe à au moins 8-12 caractères.")

    # Critère 2 : minuscules
    if any(c.islower() for c in pw):
        score += 1
    else:
        conseils.append("Ajouter des lettres minuscules.")

    # Critère 3 : majuscules
    if any(c.isupper() for c in pw):
        score += 1
    else:
        conseils.append("Ajouter des lettres majuscules.")

    # Critère 4 : chiffres
    if any(c.isdigit() for c in pw):
        score += 1
    else:
        conseils.append("Ajouter au moins un chiffre.")

    # Critère 5 : symboles
    symbols = set(string.punctuation)
    if any(c in symbols for c in pw):
        score += 1
    else:
        conseils.append("Ajouter des caractères spéciaux (ex: !@#$%).")

    # Critère 6 : diversité
    if len(set(pw)) > len(pw) * 0.6:
        score += 1
    else:
        conseils.append("Éviter les caractères répétés (aaaa, 1111).")

    # Score max = 8
    return score, conseils

def generate_password(length: int = 12, use_symbols: bool = True) -> str:
    """Génère un mot de passe sûr."""
    if length < 4:
        raise ValueError("La longueur minimale recommandée est 4 caractères.")
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def pretty_print_result(pw: str):
    """Affiche un rapport clair."""
    score, conseils = check_password(pw)
    if score >= 7:
        niveau = " Très fort"
    elif score >= 5:
        niveau = " Fort"
    elif score >= 3:
        niveau = " Moyen"
    else:
        niveau = " Faible"

    print("\n=== Résultat ===")
    print(f"Mot de passe : {pw}")
    print(f"Score : {score}/8 — Niveau : {niveau}")
    if conseils:
        print("\n Conseils :")
        for c in conseils:
            print(f"- {c}")
    else:
        print("\n Aucun conseil : mot de passe bien équilibré.")

def menu():
    """Menu principal du programme."""
    while True:
        print("\n===== PASSWORD TOOLKIT =====")
        print("1. Vérifier un mot de passe")
        print("2. Générer un mot de passe")
        print("3. Quitter")

        choix = input("Choisissez une option (1-3) : ").strip()

        if choix == "1":
            pw = input("\nEntrez le mot de passe à vérifier : ")
            pretty_print_result(pw)

        elif choix == "2":
            try:
                length = int(input("\nLongueur du mot de passe (ex: 12) : "))
            except ValueError:
                print(" Veuillez entrer un nombre valide.")
                continue

            sym = input("Inclure des symboles ? (o/n) : ").lower()
            use_symbols = (sym != "n")

            pw = generate_password(length, use_symbols)
            print("\nMot de passe généré :")
            print(f" {pw}")
            pretty_print_result(pw)

        elif choix == "3":
            print("\n Merci d'avoir utilisé Password Toolkit !")
            break

        else:
            print(" Choix invalide, essayez encore.")

if __name__ == "__main__":
    menu()
