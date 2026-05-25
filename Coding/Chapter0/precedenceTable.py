from textwrap import dedent

def get_operator_precedence_table():
    """
    Returns a list of tuples: (precedence_level, operators, description, associativity)
    Based on Python's official precedence rules.
    """
    return [
        (1, "()", "Parentheses (grouping)", "Left-to-right"),
        (2, "x[index], x[index:index], x(...), x.attr", "Subscription, slicing, function call, attribute reference", "Left-to-right"),
        (3, "await x", "Await expression", "Left-to-right"),
        (4, "**", "Exponentiation", "Right-to-left"),
        (5, "+x, -x, ~x", "Unary plus, unary minus, bitwise NOT", "Right-to-left"),
        (6, "*, @, /, //, %", "Multiplication, matrix multiplication, division, floor division, modulus", "Left-to-right"),
        (7, "+, -", "Addition, subtraction", "Left-to-right"),
        (8, "<<, >>", "Bitwise shift operators", "Left-to-right"),
        (9, "&", "Bitwise AND", "Left-to-right"),
        (10, "^", "Bitwise XOR", "Left-to-right"),
        (11, "|", "Bitwise OR", "Left-to-right"),
        (12, "in, not in, is, is not, <, <=, >, >=, !=, ==", "Comparisons, membership, identity tests", "Left-to-right"),
        (13, "not x", "Logical NOT", "Right-to-left"),
        (14, "and", "Logical AND", "Left-to-right"),
        (15, "or", "Logical OR", "Left-to-right"),
        (16, "if ... else ...", "Conditional expression", "Right-to-left"),
        (17, "lambda", "Lambda expression", "Left-to-right"),
        (18, ":=", "Assignment expression (Walrus operator)", "Right-to-left"),
    ]

def print_precedence_table():
    table = get_operator_precedence_table()
    print(f"{'Precedence':<10} {'Operators':<50} {'Description':<60} {'Associativity'}")
    print("-" * 140)
    for prec, ops, desc, assoc in table:
        print(f"{prec:<10} {ops:<50} {desc:<60} {assoc}")

if __name__ == "__main__":
    print("\nPython Operator Precedence Table (Highest → Lowest)\n")
    print_precedence_table()
    print("\nNote: Parentheses can always be used to override precedence.")