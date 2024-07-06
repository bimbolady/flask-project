from pymongo import MongoClient
import csv

class User:
  def __init__(self, age, gender, income, expenses):
    self.age = age
    self.gender = gender
    self.income = income
    self.expenses = expenses

# Connect to MongoDB 
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["users"]

users = []
for document in collection.find():
  user = User(document["age"], document["gender"], document["income"], document["expenses"])
  users.append(user)

# Write user data to CSV
with open("survey_data.csv", "w", newline="") as csvfile:
  fieldnames = ["age", "gender", "income", "utilities", "entertainment", "school_fees", "shopping", "healthcare"]
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for user in users:
    writer.writerow({
      "age": user.age,
      "gender": user.gender,
      "income": user.income,
      **user.expenses
    })

print("Data saved to survey_data.csv")
