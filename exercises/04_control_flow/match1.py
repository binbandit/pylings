"""
match1.py - Match Statements (Python 3.10+)

The `match` statement compares a value against patterns:

    match value:
        case pattern1:
            # runs if value matches pattern1
        case pattern2:
            # runs if value matches pattern2
        case _:
            # wildcard - matches anything (like 'default' in other languages)

This is similar to switch/case in other languages but more powerful.

Your task: Add a case for HTTP status code 418 ("I'm a teapot").
The case should print "I'm a teapot" when status is 418.
"""


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        # TODO: Add a case for 418 that returns "I'm a teapot"
        case _:
            return "Unknown"


def main():
    # Test the existing cases
    print(f"200: {http_status(200)}")
    print(f"404: {http_status(404)}")

    # Test the case you need to add
    result = http_status(418)
    print(f"418: {result}")

    if result != "I'm a teapot":
        raise Exception(f'Status 418 should return "I\'m a teapot", got "{result}"')

    print("Match statement works!")


if __name__ == "__main__":
    main()
