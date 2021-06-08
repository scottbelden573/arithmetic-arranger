def arithmetic_arranger(problems):
    return 1

class Problem:
    """Common base class for all problems"""
    problemCount = 0

    def __init__(self, term1, term2):
        self.term1 = term1
        self.term2 = term2
        Problem.problemCount += 1
        print('I am constructed')

    def get_terms(self):
        "for problem in list"
        problem ="32 + 698"

    def solve_problem():
        """if +, add
        if -, subtract
        result ="""

    def format_problem(self):
        print "Term 1 : ", self.term1, ", Term 2: ", self.term2

    def len(self):
        """for determining length of list. return error if more than 5 problems """
        if len() > 5
            return "Error: Too many problems."
# This would create first object of Problem class
prob1 = Problem(32, 698)
# This would create second object of Problem class
prob2 = Problem(3801, 2)

prob1.format_problem()
prob2.format_problem()