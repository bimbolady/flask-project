### Healthcare Survey Analysis - Flask, MongoDB, and Data Visualization

This project explores income and spending data collected through a web survey to support the launch of a new healthcare product.

Key Technologies:
Flask: Creates a user-friendly web interface for collecting survey data.
MongoDB: Stores user responses efficiently in a NoSQL database.
Python (pandas & matplotlib): Processes and visualizes the collected data to identify trends.

Functionality:

1. Web Survey: A Flask app serves an HTML form for users to enter their age, gender, total income, and expenses in various categories (utilities, entertainment, school fees, shopping, healthcare).
2. Data Storage: User data is submitted to the Flask app and stored in a MongoDB collection.
3. Data Processing: A separate Python script retrieves data from MongoDB, creates a CSV file for further analysis, and performs data cleaning if needed.
4. Data Visualization: A Jupyter Notebook utilizes pandas for data manipulation and matplotlib for creating visualizations. It generates two charts:
     Age with Highest Income: Shows the average income for each age group.
     Gender Distribution of Spending: Visualizes how spending is distributed across categories for each gender (stacked bar chart).

Getting Started:

1. Ensure you have Python, Flask, pymongo, pandas, and matplotlib installed.
2. Replace the placeholder connection details in the code for MongoDB if needed.
3. Run the Flask app (`app.py`) to launch the survey webpage (usually accessible at http://127.0.0.1:5000/ in your browser).
4. Fill out the survey and submit it. 
5. Run the data processing script (`data_processing.py`) to generate the CSV file and visualizations in a Jupyter Notebook.


I hope this README provides a clear overview of the project!


#### Author
Abimbola Oreoluwa