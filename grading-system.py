marks = 75

if 90 <= marks < 100:
    print(f"Marks: {marks} | Grade: A")
elif 80 <= marks < 90:
    print(f"Marks: {marks} | Grade: B")
elif 70 <= marks < 80:
    print(f"Marks: {marks} | Grade: C")
elif 60 <= marks < 70:
    print(f"Marks: {marks} | Grade: D")
elif 0 <= marks < 60:
    print(f"Marks: {marks} | Grade: F (Failed)")
else:
    print("Invalid marks entered! Please enter a value between 0 and 100.")                   


