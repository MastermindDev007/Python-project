import random
import pandas as pd

# Define the form questions and options
questions = {
    "age": ["22-25", "26-30", "31-35", "36-40"],
    "education": ["Master's", "Doctoral", "Other"],
    "field_of_study": ["Business", "Engineering", "Arts", "Sciences", "Other"],
    "financial_literacy": [1, 2, 3, 4, 5],
    "course_taken": ["Yes", "No"],
    "saving_frequency": [1, 2, 3, 4, 5],
    "investing": ["Yes", "No"],
    "credit_report_frequency": [1, 2, 3, 4, 5]
}

# Generate 200 fake responses
responses = []
for i in range(200):
    response = {
        "age": random.choice(questions["age"]),
        "education": random.choice(questions["education"]),
        "field_of_study": random.choice(questions["field_of_study"]),
        "financial_literacy": random.choice(questions["financial_literacy"]),
        "course_taken": random.choice(questions["course_taken"]),
        "saving_frequency": random.choice(questions["saving_frequency"]),
        "investing": random.choice(questions["investing"]),
        "credit_report_frequency": random.choice(questions["credit_report_frequency"])
    }
    responses.append(response)

# Convert the responses to a Pandas DataFrame
df = pd.DataFrame(responses)

# Save the DataFrame to a CSV file
df.to_csv("fake_responses.csv", index=False)