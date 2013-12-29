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
  print get_letter_grade(get_average(lloyd))
  print get_class_average([lloyd,alice,tyler])
  print avg
  print get_letter_grade(avg)

  #
  # Add your function below!
def average(lst):
  """Computes the arithmetic mean of a list of numbers."""
  return sum(lst,0.0) / len(lst)
#
def get_average(student):
  """Write a function called get_average that takes a     student dictionary as input and returns his/her weighted average. Use your average function to help. Homework is 10%, quizzes are 30% and tests are 60%. """
  return (average(student["homework"]) * 0.10 + average(student["quizzes"]) * 0.30 + average(student["tests"]) * 0.60 )
#
def get_letter_grade(score):
  if (score >= 90):
    return "A"
  elif (score < 90 and score >= 80):
    return "B"
  elif (score < 80 and score >= 70):
    return "C"
  elif (score < 70 and score >= 60):
    return "D"
  else:
    return "F"
#
def get_class_average(classlist):
  averages = []
  for student in classlist:
    averages.append(get_average(student)) 
  return average(averages)
#
if __name__ == "__main__":
  main()
