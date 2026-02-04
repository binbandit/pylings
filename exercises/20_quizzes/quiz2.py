"""
Quiz: RPG Character System

This quiz combines: Classes, Inheritance, __init__, Methods, and Conditionals.

Scenario:
You're building a simple RPG game with characters that can fight.

Task 1: Complete the Character class
- __init__(self, name, hp): Store name and hp as instance attributes
- take_damage(self, amount): Reduce hp by amount (hp can go negative)
- is_alive(self): Return True if hp > 0, False otherwise

Task 2: Complete the Wizard class (inherits from Character)
- __init__(self, name, hp, mana): Call parent __init__, then store mana
- cast_spell(self, target):
    - If mana >= 10: subtract 10 from mana, deal 25 damage to target
    - If mana < 10: print "Not enough mana!" and do nothing

Example:
    hero = Wizard("Merlin", hp=100, mana=30)
    enemy = Character("Goblin", hp=50)

    hero.cast_spell(enemy)  # enemy.hp becomes 25, hero.mana becomes 20
    hero.cast_spell(enemy)  # enemy.hp becomes 0, hero.mana becomes 10
    enemy.is_alive()        # Returns False
"""


class Character:
    """Base class for all game characters."""

    def __init__(self, name, hp):
        """
        Initialize a character.

        Args:
            name: The character's name (str)
            hp: Health points (int)
        """
        # TODO: Store name and hp as instance attributes
        # Hint: self.name = name
        pass

    def take_damage(self, amount):
        """
        Reduce this character's HP by the given amount.
        HP can go negative (character is dead).
        """
        # TODO: Subtract amount from self.hp
        pass

    def is_alive(self):
        """
        Check if the character is still alive.

        Returns:
            bool: True if hp > 0, False otherwise
        """
        # TODO: Return True if hp > 0, else False
        pass


class Wizard(Character):
    """A magical character that can cast spells."""

    def __init__(self, name, hp, mana):
        """
        Initialize a wizard.

        Args:
            name: The wizard's name (str)
            hp: Health points (int)
            mana: Mana points for casting spells (int)
        """
        # TODO: Call the parent class __init__ to set name and hp
        # Hint: super().__init__(name, hp)

        # TODO: Store mana as an instance attribute
        pass

    def cast_spell(self, target):
        """
        Cast a spell at a target character.

        - Costs 10 mana
        - Deals 25 damage to target
        - If not enough mana, prints "Not enough mana!" and does nothing

        Args:
            target: A Character (or subclass) to damage
        """
        # TODO: Check if self.mana >= 10
        #       If yes: subtract 10 mana, call target.take_damage(25)
        #       If no: print "Not enough mana!"
        pass


def main():
    # Verify Character class is implemented
    print("Testing Character class...")

    if not hasattr(Character, "take_damage") or not hasattr(Character, "is_alive"):
        raise Exception(
            "Character class needs take_damage and is_alive methods.\n"
            "Make sure you've defined all required methods."
        )

    # Test Character
    goblin = Character("Goblin", hp=40)

    if not hasattr(goblin, "hp") or not hasattr(goblin, "name"):
        raise Exception(
            "Character __init__ should store name and hp as instance attributes.\n"
            "Hint: self.name = name; self.hp = hp"
        )

    if goblin.hp != 40:
        raise Exception(f"Goblin hp should be 40, got {goblin.hp}")

    if not goblin.is_alive():
        raise Exception("Goblin with 40 HP should be alive!")

    goblin.take_damage(25)
    if goblin.hp != 15:
        raise Exception(
            f"After 25 damage, goblin hp should be 15, got {goblin.hp}\n"
            "Hint: self.hp -= amount"
        )

    print("  Character class works!")

    # Test Wizard
    print("Testing Wizard class...")

    hero = Wizard("Merlin", hp=100, mana=20)

    if not hasattr(hero, "mana"):
        raise Exception(
            "Wizard should have a 'mana' attribute.\nHint: self.mana = mana"
        )

    if not hasattr(hero, "hp"):
        raise Exception(
            "Wizard should inherit 'hp' from Character.\n"
            "Hint: super().__init__(name, hp)"
        )

    monster = Character("Ogre", hp=40)

    # First spell
    hero.cast_spell(monster)

    if monster.hp != 15:
        raise Exception(
            f"After cast_spell, monster hp should be 15, got {monster.hp}\n"
            "Hint: Call target.take_damage(25)"
        )

    if hero.mana != 10:
        raise Exception(
            f"After cast_spell, hero mana should be 10, got {hero.mana}\n"
            "Hint: self.mana -= 10"
        )

    # Second spell
    hero.cast_spell(monster)

    if monster.hp != -10:
        raise Exception(
            f"After second spell, monster hp should be -10, got {monster.hp}"
        )

    if monster.is_alive():
        raise Exception("Monster with -10 HP should NOT be alive!")

    if hero.mana != 0:
        raise Exception(f"Hero mana should be 0, got {hero.mana}")

    # Third spell (no mana)
    print("  Testing 'Not enough mana' case...")
    hero.cast_spell(monster)  # Should print "Not enough mana!"

    if hero.mana < 0:
        raise Exception(
            "Mana should not go negative!\nHint: Check if mana >= 10 BEFORE subtracting"
        )

    print("  Wizard class works!")

    print("\nQuiz 2 passed!")


if __name__ == "__main__":
    main()
