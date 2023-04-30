# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example
# marks key: value pairs are
# 'alpha': [20, 30, 40]
# 'beta': [30, 50, 70]

# The query_name is 'beta'. beta's average score is (30+50+70)/3 = 50.0

# Input Format
# The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

# Constraints
# -> 2<= n <= 10
# -> 0 <= marks[i] <=100
# -> length of marks arrays = 3

# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
sum = 0
length_of_query = len(student_marks[query_name])
if query_name in student_marks:

    for i in range (length_of_query):
        sum = sum + student_marks[query_name][i]
        avg =  sum/length_of_query
print("{:.2f}".format(avg))
# else:
#   print("the query does not match")
