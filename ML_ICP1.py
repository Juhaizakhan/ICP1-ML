# question1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()
print("Sorted list:", ages)

# Find the minimum and maximum age
min_age = ages[0]
max_age = ages[-1]
print("Min age:", min_age)
print("Max age:", max_age)

# Add the min and max age to the list
ages.extend([min_age, max_age])
print("List after adding min and max age:", ages)

# Calculate the median age
ages.sort()  # Ensure the list is sorted
length = len(ages)
if length % 2 == 0:
    median_age = (ages[length // 2 - 1] + ages[length // 2]) / 2
else:
    median_age = ages[length // 2]
print("Median age:", median_age)

# Calculate the average age
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# Calculate the range of ages
age_range = max_age - min_age
print("Range of ages:", age_range)

# question2
# Create an empty dictionary called dog and add details
dog = {}
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Pomeranian'
dog['legs'] = 4
dog['age'] = 2

print("Dog dictionary:", dog)

# Create a dictionary for a student and add details
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

print("Student dictionary:", student)

# Find the number of items in the student dictionary
print("Length of student dictionary:", len(student))

# Get the value of skills and check its data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# Add more skills to the student's skills list
student['skills'].append('HTML')
student['skills'].append('CSS')
print("Updated skills:", student['skills'])

# Get the keys of the student dictionary as a list
keys = list(student.keys())
print("Keys of student dictionary:", keys)

# Get the values of the student dictionary as a list
values = list(student.values())
print("Values of student dictionary:", values)

# question3

# Create tuples for brothers and sisters
brothers = ("Jibran",)
sisters = ("Umaima", "Jasrah", "Juhaiza")

print("Brothers:", brothers)
print("Sisters:", sisters)

# Combine brothers and sisters tuples into a single siblings tuple
siblings = brothers + sisters

print("Siblings:", siblings)

# Find out how many siblings there are
num_siblings = len(siblings)

print("Number of siblings:", num_siblings)

# Add parents' names to the siblings tuple to create a family_members tuple
family_members = siblings + ("Dad", "Mom")

print("Family members:", family_members)

# question4

# Define the initial sets and list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)

# Insert multiple IT companies to it_companies
it_companies.update(['Netflix', 'LinkedIn', 'Adobe'])
print("After adding multiple companies:", it_companies)

# Remove one company from it_companies
it_companies.remove('Adobe')  # remove raises an error if the item does not exist
print("After removing one company:", it_companies)

# Difference between remove and discard
# remove raises an error if the item does not exist
# discard does not raise an error if the item does not exist
it_companies.discard('NonExistentCompany')  # no error raised
print("After trying to discard a non-existent company:", it_companies)

# Join A and B
A_union_B = A.union(B)
print("A union B:", A_union_B)

# Find the intersection of A and B
A_intersection_B = A.intersection(B)
print("A intersection B:", A_intersection_B)

# Check if A is a subset of B
is_subset = A.issubset(B)
print("Is A a subset of B?", is_subset)

# Check if A and B are disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint?", are_disjoint)

# Join A with B and B with A
A.update(B)
B.update(A)
print("A after joining with B:", A)
print("B after joining with A:", B)

# Find the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff)

# Delete the sets completely
A.clear()
B.clear()
print("A after clearing:", A)
print("B after clearing:", B)

# Convert age list to a set and compare the lengths
age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))

# question5

import math

# Given radius
radius = 30

# Calculate the area of the circle
_area_of_circle_ = math.pi * radius ** 2
print("Area of the circle:", _area_of_circle_)

# Calculate the circumference of the circle
_circum_of_circle_ = 2 * math.pi * radius
print("Circumference of the circle:", _circum_of_circle_)

# Take radius as user input
user_radius = float(input("Enter the radius of the circle: "))

# Calculate the area with the user input radius
user_area_of_circle = math.pi * user_radius ** 2
print("Area of the circle with radius", user_radius, ":", user_area_of_circle)

# question6

# Given sentence
sentence = "I am a teacher and I love to inspire and teach people"

# Split the sentence into words
words = sentence.split()

# Convert the list of words to a set to get unique words
unique_words = set(words)

# Get the number of unique words
num_unique_words = len(unique_words)

# Print the number of unique words
print("Number of unique words:", num_unique_words)

# question7

# Print the header with tab separation
print("Name\tAge\tCountry\tCity")

# Print the details with tab separation
print("Asabeneh\t250\tFinland\tHelsinki")


# question8

# Given radius
radius = 10

# Calculate the area of the circle
area = 3.14 * radius ** 2

# Display the result using string formatting
print(f"The area of a circle with radius {radius} is {area} meters square.")

# question9

# Read the number of students from the user
num_students = int(input("Enter the number of students: "))

# Initialize an empty list to store weights in lbs.
weights_lbs = []

# Read the weights of students in lbs.
for i in range(num_students):
    weight_lbs = float(input(f"Enter weight of student {i+1} in lbs: "))
    weights_lbs.append(weight_lbs)

# Initialize an empty list to store weights in kgs.
weights_kgs = []

# Convert weights from lbs. to kgs. and append to the new list
for weight_lbs in weights_lbs:
    weight_kgs = weight_lbs * 0.453592
    weights_kgs.append(round(weight_kgs, 2))  # Round off to two decimal places

# Print the converted weights in kgs.
print("Weights in kilograms:", weights_kgs)




    
    
    
