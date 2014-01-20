def main():
  grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
  print_grades(grades)
  print grades_sum(grades)


def print_grades(grades):
	for grade in grades:
		print grade

		
def grades_sum(scores):
	total = 0
	for grade in scores:
		total+=grade
	return total

if __name__ == "__main__":
    main()
