def main():
  lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
  }
  alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
  }
  tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
  }
  #
  # Add your function below!
  def average(lst):
    """Computes the arithmetic mean of a list of numbers."""
    return sum(lst,0.0) / len(lst)
#
def get_average(student):
  """Write a function called get_average that takes a student dictionary as input and returns his/her weighted average. Use your average function to help. Homework is 10%, quizzes are 30% and tests are 60%. """
  return (average(student["homework"]) * 0.10 + average(student["quizzes"]) * 0.30 + average(student["tests"]) * 0.60 )

if __name__ == "__main__":
  main()
