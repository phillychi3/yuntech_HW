

from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod


class Constraint():
    def __init__(self, variables: List) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict) -> bool:
        pass






class CSP():
    def __init__(self, variables: List, domains: Dict) -> None:
        self.variables = variables
        self.domains = domains
        self.constraints: Dict = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise "looks we have a problem"

    def add_constraint(self, constraint) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise "Variable in constraint not in CSP"
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable, assignment: Dict) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict = {}) -> Optional[Dict]:
        # assignment is complete if every variable is assigned
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result: Optional[Dict] = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None