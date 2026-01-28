"""
Concept: Dictionaries (Merging)
In Python 3.9+, you can merge dictionaries using the `|` operator. `dict1 | dict2` creates a new dict with values from `dict2` overwriting `dict1` on collision.

Task: Merge `user_config` into `default_config` using `|`.
"""

def main():
    # Merging dictionaries (Python 3.9+)
    default_config = {"theme": "light", "notifications": True}
    user_config = {"theme": "dark"}
    
    # FIX ME: Merge user_config into default_config (user_config wins)
    # config = default_config | user_config
    config = {}
    
    if config.get("theme") != "dark":
        raise Exception("Theme should be dark!")
        
    if config.get("notifications") is not True:
        raise Exception("Notifications should still be True!")

if __name__ == "__main__":
    main()
