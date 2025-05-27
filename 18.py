from pyparsing import Word, alphas, alphanums, Forward, Group, Suppress, oneOf, Optional, infixNotation, opAssoc, ZeroOrMore

# Define basic elements
identifier = Word(alphas, alphanums + "_")

# Variables and constants
variable = identifier
constant = identifier

# Predicates and functions
predicate = identifier

# Terms: variable or constant
term = variable | constant
term_list = Group(term + ZeroOrMore(Suppress(",") + term))

# Predicate application: e.g., P(x), Loves(John, Mary)
predicate_expr = Group(predicate + Suppress("(") + term_list + Suppress(")"))

# Logical connectives
NOT = Suppress("¬") | Suppress("~")
AND = Suppress("∧") | Suppress("&")
OR = Suppress("∨") | Suppress("|")
IMPLIES = Suppress("→") | Suppress("=>")
IFF = Suppress("↔") | Suppress("<=>")

# Quantifiers
FORALL = Suppress("∀") | Suppress("forall")
EXISTS = Suppress("∃") | Suppress("exists")

# Forward declaration for recursion
fopc_expr = Forward()

# Quantified expressions
quantified_expr = Group(
    (FORALL | EXISTS)("quantifier") +
    variable("variable") +
    fopc_expr("expression")
)

# Logical expressions using operator precedence
fopc_expr <<= infixNotation(predicate_expr | quantified_expr,
    [
        (NOT, 1, opAssoc.RIGHT),
        (AND, 2, opAssoc.LEFT),
        (OR, 2, opAssoc.LEFT),
        (IMPLIES, 2, opAssoc.RIGHT),
        (IFF, 2, opAssoc.RIGHT)
    ]
)

# === Test Cases ===
def parse_fopc(expression):
    try:
        result = fopc_expr.parseString(expression, parseAll=True)
        print("Parsed AST:")
        print(result)
    except Exception as e:
        print("Error:", e)

# === Examples ===
examples = [
    "∀x Man(x) → Mortal(x)",
    "∃x Loves(John, x)",
    "¬Human(Socrates)",
    "Man(Socrates) ∧ Mortal(Socrates)"
]

for expr in examples:
    print(f"\nExpression: {expr}")
    parse_fopc(expr)
