import random

def get_user_Move():
    user_choice = input("(pierre, papier, ciseaux): ").lower()
    while user_choice not in ["pierre", "papier", "ciseaux"]:
        user_choice = input("Entrée invalidet").lower()
    return user_choice

def get_rdm_move():
    return random.choice(["rock", "papier", "ciseaux"])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ex aequo"
    elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
         (user_choice == "papier" and computer_choice == "pierre") or \
         (user_choice == "ciseaux" and computer_choice == "papier"):
        return "Win !"
    else:
        return "T nul"

def Disp_score(scoreIA, scoreUser):
    print(f"IA: {scoreIA} | Toi: {scoreUser}")

def play_game():
    scoreIA, scoreUser = 0, 0
    Disp_score(scoreIA, scoreUser)

    while scoreIA < 3 and scoreUser < 3:
        user_Move = get_user_Move()
        IA_Move = get_rdm_move()
        print(f"Vous avez choisi: {user_Move}")
        print(f"IA à choisi: {IA_Move}")
        result = winner(user_Move, IA_Move)
        print(result)
        if result == "Win !":
            scoreUser += 1
        elif result == "T nul":
            scoreIA += 1
        Disp_score(scoreIA, scoreUser)
    if scoreIA == 3:
        result = "IA a gagné"
    else:
        result = "Vous avez gagné"

if __name__ == "__main__":
    play_game()