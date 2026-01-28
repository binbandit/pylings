"""
Quiz: RPG Character System

Goal: Combine Classes, Inheritance, and Method Overriding.

Scenario:
1. Create a base class `Character` with `name` and `hp` (health points).
   - Method `take_damage(amount)` reduces HP.
   - Method `is_alive()` returns True if HP > 0.
   
2. Create a subclass `Wizard` that inherits from `Character`.
   - It has extra attribute `mana`.
   - Method `cast_spell(target)`:
     - Costs 10 mana.
     - Deals 25 damage to the target (calls target.take_damage).
     - If not enough mana, print "Not enough mana!" and do nothing.
"""

# FIX ME: Define Character class
class Character:
    # def __init__(self, name, hp): ...
    # def take_damage(self, amount): ...
    # def is_alive(self): ...
    pass

# FIX ME: Define Wizard class
class Wizard: # (Character)
    # def __init__(self, name, hp, mana): ...
    # def cast_spell(self, target): ...
    pass

def main():
    # Make a dummy check to prevent immediate failure if empty
    if not hasattr(Character, 'take_damage'):
        raise Exception("Define Character class first")

    hero = Wizard("Merlin", hp=100, mana=20)
    monster = Character("Goblin", hp=40)
    
    # Turn 1
    hero.cast_spell(monster) # Monster HP -> 15, Mana -> 10
    
    if monster.hp != 15:
        raise Exception(f"Monster should have 15 HP, has {monster.hp}")
    if hero.mana != 10:
        raise Exception(f"Hero should have 10 Mana, has {hero.mana}")
        
    # Turn 2
    hero.cast_spell(monster) # Monster HP -> -10 (Dead), Mana -> 0
    
    if monster.is_alive():
        raise Exception("Monster should be dead")
        
    # Turn 3 (No mana)
    hero.cast_spell(monster) # Should print "Not enough mana"
    
    if hero.mana < 0:
        raise Exception("Mana cannot go negative")
        
    print("Quiz 2 Passed!")

if __name__ == "__main__":
    main()
