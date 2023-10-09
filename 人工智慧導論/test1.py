from csp import Constraint, CSP



# Define the variables and their domains
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}

# Define the constraints
def different_values_constraint(A, B):
    return A != B

class AllDifferentConstraint(Constraint):
    def __init__(self, variables):
        super().__init__(variables)

    def satisfied(self, assignment):
        # If there are duplicate values then it's not a solution
        if len(set(assignment.values())) < len(assignment):
            return False

        # No constraint violated
        return True




# Create the CSP object
csp = CSP(variables, domains)

csp.add_constraint(AllDifferentConstraint(variables))

# Solve the CSP
solution = csp.backtracking_search()

# Print the solution
if solution is None:
    print("No solution found!")
else:
    print(solution)
