score = int(input("enter a test score(0-100): "))
if score < 0 or score > 100:
  print("enter a score")
elif score >= 90:
  grade = "A"
  print("your grade is", grade)
elif score >= 80:
  grade = "B"
  print("your grade is", grade)
elif score >= 70:
  grade = "C"
  print("your grade is", grade)
elif score >= 60:
  grade = "D"
  print("your grade is", grade)
else:
  grade ="F"
  print("your grade is", grade)