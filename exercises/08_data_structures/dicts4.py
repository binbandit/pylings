"""
Concept: Dictionaries (Safe Access)
Using brackets `dict[key]` raises an error if the key is missing. `.get(key, default)` allows safe access.

Task: Use `.get()` to safely retrieve Bob's role (or default to "guest") and handle a missing user.
"""

def main():
    # Nested dictionary
    users = {
        "alice": {"role": "admin"},
        "bob": {"role": "user"}
    }
    
    # FIX ME: Get Bob's role safely. If bob doesn't exist, return "guest"
    # role = users.get("bob", {}).get("role", "guest")
    role = "unknown"
    
    if role != "user":
        raise Exception("Bob's role should be user!")
        
    # Check non-existent user
    role_charlie = "admin" # FIX ME
    
    if role_charlie != "guest":
         raise Exception("Charlie should be guest!")

if __name__ == "__main__":
    main()
