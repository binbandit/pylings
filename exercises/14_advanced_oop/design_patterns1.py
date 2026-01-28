
# DESIGN PATTERNS: SINGLETON
# ==========================
#
# What: A class that allows only ONE instance to be created.
#
# Why:  Controlling access to shared resources (e.g., Database Connection, Configuration Manager).
#
# How:  Override `__new__` method.
#       cls._instance = None (class variable)
#       if cls._instance is None: create it.
#       return cls._instance.
#
# Task:
# 1. Implement a `DatabaseConnection` class that is a Singleton.
# 2. Every time you call `DatabaseConnection()`, you must get the EXACT SAME object.

class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        # TODO: Implement Singleton logic
        if cls._instance is None:
             cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Note: __init__ runs every time you call Class().
        # In robust singletons, you assume initialization happens once or check a flag.
        self.status = "Connected"

def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    assert db1 is db2, "db1 and db2 should be the same object"
    
    db1.status = "Disconnected"
    assert db2.status == "Disconnected", "Change in db1 should reflect in db2"

if __name__ == "__main__":
    test_singleton()
    print("Singleton pattern passed!")
