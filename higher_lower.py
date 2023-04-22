from art import logo, vs
from game_data import data
import random
import os


def get_people(data_set):
    random.shuffle(data_set)
    # people = [random.choice(data_set) for _ in range(2)]
    people = [random.choice(data_set)]
    if people[0] in data_set:
        data_set.remove(people[0])
    for person in people:
        print(f"{person['name']}, a {person['description']}, from {person['country']}")
        print(f"Current follower count: {person['follower_count']}\n")
    return people


def compare_people(choice_1, choice_2, user_score):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a' and choice_1[0]['follower_count'] > choice_2[0]['follower_count']:
        print(
            f"You're Right! {choice_1[0]['name']} has more followers than {choice_2[0]['name']}! {choice_1[0]['follower_count']} vs. {choice_2[0]['follower_count']}\n")
        return True
    elif user_choice == 'b' and choice_2[0]['follower_count'] > choice_1[0]['follower_count']:
        print(
            f"You're Right! {choice_2[0]['name']} has more followers than {choice_1[0]['name']}! {choice_1[0]['follower_count']} vs. {choice_2[0]['follower_count']}\n")
        return True
    else:
        print(
            f"You Lose! {choice_1[0]['name']} has {choice_1[0]['follower_count']} followers and {choice_2[0]['name']} has {choice_2[0]['follower_count']} followers\n")
        print(f"Your final score is: {user_score}")
        return False


print("Welcome to the Higher Lower Game!")
print("I will give you two options and you have to guess which one has more followers on Instagram.\n")

score = 0
while True:
    print(logo)
    print("Compare A: ")
    person_1 = get_people(data)
    print(vs)
    print("Against B: ")
    person_2 = get_people(data)
    print(f"Your current score is: {score}")
    if not compare_people(person_1, person_2, score):
        break
    score += 1
    os.system('clear')