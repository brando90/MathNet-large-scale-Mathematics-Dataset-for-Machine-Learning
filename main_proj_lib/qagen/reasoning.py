'''
This is a draft
'''
import pprint

class Reasoning:
  def __init__(self, label, description, parameters, results, subproblems):
      self.label = label
      self.description = description
      self.parameters = parameters
      self.results = results
      self.subproblems = subproblems

euclideanDivision = Reasoning(
    label = "Euclidean Division",
    description = (
        "Euclidean division is the process of finding the quotient and"
        " remainder of two integers."
        ),
    parameters = [
        "Euclidean division takes two integers as inputs.",
        "One of the inputs is called the dividend.",
        "The other input is called the divisor.",
        "The divisor must be non-zero."
        ],
    results = [
        "Euclidean division has two outputs.",
        "One of the outputs is called the quotient.",
        "One of the outputs is called the remainder.",
        ("The divisor multiplied by the quotient and then summed with"
         " the remainder is equal to the dividend."
         )
        ],
    subproblems = []
)

extendedEuclid = Reasoning(
    label = "Extended euclidean algorithm",
    description=(
        "The extended euclidean algorithm takes as inputs two integers",
        " and produces as results their greatest common divisor as well as"
        " coefficients demonstrating that the greatest common divisor is a"
        " linear combination of the input parameters."
        ),
    parameters=[
        "The extended euclidean algorithm takes two integers as input."
        ],
    results=[
        ("The extended euclidean algorithm produces three integers:"
         " the greatest common divisor of the inputs and coefficients that"
         " verify that the GCD is a linear combination of the inputs."
         ),
        ("The coefficients produced by the algorithm are coprime."
         " This implies that the GCD is the smallest integer that is a linear"
         " combination of the inputs."
         )
        ],
    subproblems = [
        (euclideanDivision, [
          ("The extended euclidean algorithm iteratively applies euclidean"
           " division starting with the input integers. The intermediate"
           " results of this iteration indicate the greatest common divisor"
           " and the coefficients which make it a linear combination of the"
           " inputs."
           ),
          ("The greatest common divisor is the last non-zero remainder in"
           " the iteration."
           ),
          ("The coefficients can be derived by the successive dividends of"
           " the iteration."
           ),
          ("The iteration ends when the remainder of an application of"
           " euclidean division results in a remainder equal to zero."
           )
          ]
        )]
    )

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(euclideanDivision.__dict__)
pp.pprint(extendedEuclid.__dict__)
