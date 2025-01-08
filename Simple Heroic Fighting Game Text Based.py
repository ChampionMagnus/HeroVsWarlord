import random

class Character:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def attack(self, opponent):
        damage = random.randint(1, self.attack_damage)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")

def main():
    player = Character("Hero", 100, 20)
    enemy = Character("Warlord", 100, 15)

    print("Welcome to the Simple Heroic Fighting Game!")
    print(f"{player.name} vs {enemy.name}")

    while player.health > 0 and enemy.health > 0:
        print("\nPlayer's turn:")
        input("Press Enter to attack evil source master")
        player.attack(enemy)
        print(f"{player.name}'s health: {player.health}")
        print(f"{enemy.name}'s health: {enemy.health}")

        if enemy.health <= 0:
            print("Congratulations! You defeated the Evil Warlord.")
            break

        print("\nEnemy's turn:")
        input("Press Enter for the enemy to try a flimsy attack on our Hero")
        enemy.attack(player)
        print(f"{player.name}'s health: {player.health}")
        print(f"{enemy.name}'s health: {enemy.health}")

        if player.health <= 0:
            print("Game over! The enemy defeated you.")
            break

if __name__ == "__main__":
    main()