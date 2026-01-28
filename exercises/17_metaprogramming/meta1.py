"""
Concept: Metaclasses
Metaclasses are "classes of classes". They control how classes are created. By overriding `__call__` in a metaclass, you can control instantiation (e.g., implementing the Singleton pattern).

Task: Implement the Singleton pattern in the metaclass `__call__` method.
"""

# FIX ME: unexpected metaclass behavior
# Define a metaclass 'Singleton' that ensures only one instance is created.
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        # FIX ME: Implement singleton logic
        # if cls not in cls._instances:
        #     cls._instances[cls] = super().__call__(*args, **kwargs)
        # return cls._instances[cls]
        return super().__call__(*args, **kwargs)

class Database(metaclass=Singleton):
    def __init__(self):
        self.connected = True

def main():
    db1 = Database()
    db2 = Database()
    
    if db1 is not db2:
        raise Exception("Database should be a singleton (db1 is not db2)!")
        
    print("Metaclass working!")

if __name__ == "__main__":
    main()
