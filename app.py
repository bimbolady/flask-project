from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def survey():
  return render_template("survey.html")

@app.route("/submit", methods=["POST"])
def submit():
  # Extract user data from form
  age = request.form.get("age")
  gender = request.form.get("gender")
  income = request.form.get("income")
  expenses = {
      "utilities": request.form.get("utilities"),
      "entertainment": request.form.get("entertainment"),
      "school_fees": request.form.get("school_fees"),
      "shopping": request.form.get("shopping"),
      "healthcare": request.form.get("healthcare")
  }

  return "Thank you for your participation!"

if __name__ == "__main__":
  app.run(debug=True)


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["users"]

def process_data(age, gender, income, expenses):
  user_data = {
      "age": age,
      "gender": gender,
      "income": income,
      "expenses": expenses
  }
  # Insert data into MongoDB collection
  collection.insert_one(user_data)
