"""""    Scope    """""

enemies = 1


def increase_enemies():
    """override enemies value"""
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies inside function: {enemies}")


# Local Scope

def drink_potion():
    """Get stronger"""
    potion_strength = 2
    print(potion_strength)


drink_potion()

# print(potion_strength) will return var not defined becsuse it is local to the function drink_potion()


# Global Scope
player_health = 10


def drink_potion_():
    """Get stronger"""
    potion_strength = 2
    print(player_health)


drink_potion_()
print(player_health)    # works as it is defined outside the function globally


# There is no block scope

game_level = 3
enemies = ["Skeleton", "Zombies", "Aliens"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)    # works because if statement doesn't confine it locally


# To modify a global var in a local function
enemies = 1


def increase_enemies_():
    """override enemies value"""
    print(f"enemies inside function: {enemies}")
    return enemies + 2


enemies = increase_enemies_()
print(f"enemies outside function: {enemies}")
