from logic import *

AKnight, AKnave = Symbol("A is a Knight"), Symbol("A is a Knave")
BKnight, BKnave = Symbol("B is a Knight"), Symbol("B is a Knave")
CKnight, CKnave = Symbol("C is a Knight"), Symbol("C is a Knave")

A = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))
B = And(Or(BKnight, BKnave), Not(And(BKnight, BKnave)))
C = And(Or(CKnight, CKnave), Not(And(CKnight, CKnave)))

knowledge0 = And(A,
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))))

knowledge1 = And(A, B,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))))

same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
knowledge2 = And(A, B,
    Implication(AKnight, same),
    Implication(AKnave, Not(same)),
    Implication(BKnight, Not(same)),
    Implication(BKnave, same))

saidKnight = And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight)))
saidKnave = And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
knowledge3 = And(A, B, C,
    Or(saidKnight, saidKnave),
    Implication(BKnight, saidKnave),
    Implication(BKnave, Not(saidKnave)),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)))

symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
puzzles = [knowledge0, knowledge1, knowledge2, knowledge3]

for i in range(4):
    print("Puzzle", i)
    for symbol in symbols:
        if model_check(puzzles[i], symbol):
            print("   ", symbol)
