LEVEL_DATA = {
    "city": {
        "description": "The central hub, where you can go to the Forest or the Shop.",
        "enemies": [],  
    },
    "forest": {
        "description": "A dark forest full of undead and wolves.",
        "enemies": ["Zombie", "Wolf"] 
    },
    "dark forest": {
        "description": "An even darker forest with bandits and goblins lurking.",
        "enemies": ["Bandit", "Goblin"]
    },
    "badlands": {
        "description": "A barren wasteland with the most dangerous creatures.",
        "enemies": ["Dragon", "Troll"]
    },
    "shop": {
        "description": "A small shop that sells potions, weapons, and armor.",
        "enemies": []
    },
    "roulette": {
        "description": "A small gambling area where you can play roulette.",
        "enemies": []
    }
}

# below dict defines all possible "neighbors" or transitions from each level
LEVEL_CONNECTIONS = {
    "city": ["forest", "shop", "roulette"],   # from city you can go to forest, shop, or roulette
    "forest": ["city", "dark forest"],        # from forest, can go back to city or into dark_forest
    "dark forest": ["forest", "badlands"],               # from dark_forest, back to forest
    "badlands": ["dark forest"],              # from badlands, back to dark_forest
    "shop": ["city"],                        # from shop, back to city
    "roulette": ["city"],                    # from roulette, back to city
}
