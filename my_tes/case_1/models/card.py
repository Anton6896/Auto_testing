class Card:
    def __init__(self, name: str, type: str, arena: int, rarity: str, **kwargs):
        self.name = name
        self.type = type
        self.arena = arena
        self.rarity = rarity

    def __str__(self):
        return f"card ({self.name}) "
