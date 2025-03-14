from faker import Faker
import random


fake = Faker('fr_FR')

def generate_character():
    character = {
        "Nom": fake.name(),
        "Race": random.choice(["Humain", "Elfe", "Nain", "Halfelin", "Orc"  ]),
        "Classe": random.choice(["Guerrier", "Mage", "Voleur", "Clerc", "Rôdeur"]),
        "Force": random.randint(3, 18),
        "Dextérité": random.randint(3, 18),
        "Constitution": random.randint(3, 18),
        "Intelligence": random.randint(3, 18),
        "Sagesse": random.randint(3, 18),
        "Charisme": random.randint(3, 18),
        "Historique": fake.sentence(nb_words=10)
    }
    Sorts = {
        "Sort1": fake.sentence(nb_words=3),
        "Sort2": fake.sentence(nb_words=3),
        "Sort3": fake.sentence(nb_words=3),
        "Sort4": fake.sentence(nb_words=3),
        "Sort5": fake.sentence(nb_words=3)
    }
    Sorts_Couts = {
        "Sort1": random.randint(1, 10),
        "Sort2": random.randint(1, 10),
        "Sort3": random.randint(1, 10),
        "Sort4": random.randint(1, 10),
        "Sort5": random.randint(1, 10)
    }
    return character, Sorts, Sorts_Couts

def display_character(character, Sorts, Sorts_Couts):
    for key, value in character.items():
        print(f"{key}: {value}")
    print("\n")
    print("Sorts:")
    for key, value in Sorts.items():
        print(f"{key}: {value}")
    print("\n")
    print("Cout Sorts:")
    for key, value in Sorts_Couts.items():
        print(f"{key}: {value}")
    print("\n")


character, Sorts, Sorts_Couts = generate_character()
display_character(character, Sorts, Sorts_Couts)
