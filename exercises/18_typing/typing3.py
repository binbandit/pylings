"""
Concept: Typing (Optional & Union)
`Optional[int]` means `int` or `None`. `Union[int, str]` means the value can be either an int or a string.

Task: Type hint `user_id` as Optional[int] and `code` as Union[int, str].
"""

from typing import Optional, Union

# FIX ME: 'user_id' can be an int OR None. 'code' can be int OR str.
# def find_user(user_id: Optional[int], code: Union[int, str]):
#     pass

def find_user(user_id, code):
    pass

def main():
    anns = find_user.__annotations__
    
    if "user_id" not in anns:
        raise Exception("Annotate user_id")
        
    if "code" not in anns:
        raise Exception("Annotate code")
        
    print("Union types used!")

if __name__ == "__main__":
    main()
