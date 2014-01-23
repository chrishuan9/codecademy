def main():
  grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
  print_grades(grades)
  print grades_sum(grades)
  print grades_average(grades)
  print grades_variance(grades,grades_average(grades))


def print_grades(grades):
	for grade in grades:
		print grade

		
def grades_sum(scores):
	total = 0
	for grade in scores:
		total+=grade
	return total

def grades_average(grades):
    sum = grades_sum(grades)
    average = float(sum) / len(grades)
    return average

def grades_variance(scores,average):
    variance = 0
    for grade in scores:
        variance += (grade - average) ** 2
    return float(variance) / len(scores)


if __name__ == "__main__":
    main()
