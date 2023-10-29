import flask
import json
from datetime import datetime
from flask import render_template, app, request, redirect   
import secrets


# Start the app & The Static folder that contains the css and js files
app = flask.Flask("budget_tracker", static_folder='static')

app.secret_key = secrets.token_hex(16)

# Start with Income Class that contains CRUD operations on income items
class Income:
   def __init__(self, type, name, description, amount, date):
      self.type = type
      self.name = name
      self.description = description
      self.amount = amount
      self.date = date
   # Method to get all income items from json file if there is any
   def get_all(type):
      # Open json file
      # with: handles the open and close of the file
      with open('data.json', 'r+') as data_file:
         # Loads the data from the file in Python data structure
         data = json.load(data_file)
         # check the type of the input
         value_type = 'income' if type == 'income' else 'expenses'
         # Check if there is income inside json file or not
         if len(data[value_type]) > 0:
            data = data[value_type]
         else:
            data = "No Data Found!"
         return data
   
   # Method to Get income item By Id => returns the item if existed and none if not
   def get_by_id(type, id):
      # Open json file
      with open('data.json', 'r+') as data_file:
         # Loads the data from the file in Python data structure
         data = json.load(data_file)
         # check the type of the input
         value_type = 'income' if type == 'income' else 'expenses'
         # Check if the item exists or not
         for item in data[value_type]:
            if item['id'] == id:
               return item
         return None
   
   # Method to Create new income item => returns True if created successfully
   def create(self):
      # Open json file in write mode
      with open('data.json', 'r+') as data_file:
         # Loads the data from the file in Python data structure
         data = json.load(data_file)
         # check the type of the input
         value_type = 'income' if self.type == 'income' else 'expenses'
         if data[value_type]:
            # create new id based on number of income resources
            new_id = max(item['id'] for item in data[value_type]) + 1
         else:
            # if there is no income resources
            new_id = 1
         # assign the values of the new income resource
         new_income = {'id': new_id, 'name': self.name, 'description': self.description, 'amount': self.amount, 'date': self.date}
         # append the new income the the file
         data[value_type].append(new_income)
         # Move file pointer to the beginning of the file
         data_file.seek(0)
         # Write the modified data to the file
         json.dump(data, data_file, indent=3)
         # Remove any remaining data
         data_file.truncate()
         return new_income

   # Method to Update income item => returns True if updated successfully
   def update(self, id):
      # Open json file in read and write mode
      with open('data.json', 'r+') as data_file:
         # Loads the data from the file in Python data structure
         data = json.load(data_file)
         # check the type of the input
         value_type = 'income' if self.type == 'income' else 'expenses'
         # Loop over items inside income object and check if the item of this id exists 
         for item in data[value_type]:
            if item['id'] == id:
               # If the item exists => assign the new values to update
               item['name'] = self.name
               item['description'] = self.description
               item['amount'] = self.amount
               item['date'] = self.date
               # Move file pointer to the beginning of the file
               data_file.seek(0)
               # Write the modified data to the file
               json.dump(data, data_file, indent=3)
               # Truncate the remaining data
               data_file.truncate()
               return True
      return False

   # Method to delete income item => returns True if deleted successfully
   def delete(type, id):
      # Open json file in read and write mode
      with open('data.json', 'r+') as data_file:
         # Loads the data from the file in Python data structure
         data = json.load(data_file)
         # check the type of the input
         value_type = 'income' if type == 'income' else 'expenses'
         for i, item in enumerate(data[value_type]):
               if item['id'] == id:
                  del data[value_type][i]
                  # Move file pointer to the beginning of the file
                  data_file.seek(0)
                  # Write the modified data to the file
                  json.dump(data, data_file, indent=3)
                  # Remove any remaining data
                  data_file.truncate()
                  return True
         return False

# Function to validate form input fields
def validate_income(name, description, amount, date):
   errors = []
   # check if source is empty or none
   if not name or not name.strip():
      errors.append("Name requried!")
   # check if description is empty or none
   if not description or not description.strip():
      errors.append("Description required!")
   # check if amount   is empty or none or not number
   if not amount or not amount.strip() or not amount.isdigit():
      errors.append("Amount should be a valid number!")
   # date also requried
   if not date or not date.strip():
      errors.append("Date is required!")
   return errors

# Make this function a global to pass templates the variables we want to make global all over the project
@app.context_processor
def global_variables():
   # Time variable where I used it all over the project
   current_year = datetime.now().year
   # Return a dectionary containing all variables I want to make global
   return {'current_year': current_year}

# Index or Home page Route
@app.route("/")
# Route Function and to get data from the Json File
def home_page():
   # Total amount expenses
   expenses = Income.get_all('expenses')
   expenses_total_amount = 0
   if expenses != 'No Data Found!':
      for expense in expenses:
         if int(expense['amount']):
            expenses_total_amount += int(expense['amount'])

   # Total amount income
   income_total_amount = 0
   incomes = Income.get_all('income')
   if incomes != 'No Data Found!':
      for income in incomes:
         if int(income['amount']):
            income_total_amount += int(income['amount'])
   # Return index template and pass it the data we want to get from json file
   return render_template("index.html", income=incomes, expenses=expenses,
                        expenses_total_amount=expenses_total_amount,
                        income_total_amount=income_total_amount)

# Add Income Page Route
@app.route("/add-income")
def add_income_page():
   return render_template("add-income.html")

# Add Income Page Route
@app.route("/create-income", methods=["POST"])
# Create New Income Function
def add_income():
   name = request.form['name']
   description = request.form['description']
   amount = request.form['amount']
   date = request.form['date']
   # Validate all input the user enters
   errors = validate_income(name, description, amount, date)
   # if there is no validation errors
   if len(errors)  == 0:
      # Creating an Instance of the Income Class
      new_income = Income('income', name, description, amount, date)
      # Calling the create class method
      new_income.create()
      return redirect("/")
   # if there is validation errors send them to view in template
   else:
      return render_template("add-income.html", errors=errors)

# Add Expense pAGE Route
@app.route("/add-expense")
def add_expense_page():
   return render_template("add-expense.html")

# Add Expense Page Route
@app.route("/create-expense", methods=["POST"])
# Create New Expense Function
def add_expense():
   name = request.form['name']
   description = request.form['description']
   amount = request.form['amount']
   date = request.form['date']
   # Validate all input the user enters
   errors = validate_income(name, description, amount, date)
   # if there is no validation errors
   if len(errors)  == 0:
      # Creating an Instance of the Income Class
      new_expense = Income('expense', name, description, amount, date)
      # Calling the create class method
      new_expense.create()
      return redirect("/")
   # if there is validation errors send them to view in template
   else:
      return render_template("add-expense.html", errors=errors)

# Update Income Page Route
@app.route("/edit-income/<int:id>")
def edit_inc(id):
   income = Income.get_by_id('income',id)
   return render_template("update-income.html", income=income)

# Update Income Item Route
@app.route("/update-income/<int:id>", methods=['POST'])
# Update Income Item Function
def update_income(id):
   # Get updated data from request (update form)
   name = request.form['name']
   description = request.form['description']
   amount = request.form['amount']
   date = request.form['date']
   # Validate updated input
   errors = validate_income(name, description, amount, date)
   if len(errors) == 0:
      # call the method to update income item info in case there is no errors
      update_income = Income('income' ,name, description, amount, date)
      update_income.update(id)
      return redirect("/")
   else:
      # to view the same item we were trying to update
      income = Income.get_by_id('income', id)
      # if there is errors, go back to the same page and view the errors
      return render_template("update-income.html", errors=errors, income=income)

# Update Expense Page Route
@app.route("/edit-expense/<int:id>")
def edit_exp(id):
   expense = Income.get_by_id('expense', id)
   return render_template("update-expense.html", expense=expense)

# Update Expense Item Route
@app.route("/update-expense/<int:id>", methods=['POST'])
# Update Expenses Item Function
def update_expense(id):
   # Get updated data from request (update form)
   name = request.form['name']
   description = request.form['description']
   amount = request.form['amount']
   date = request.form['date']
   # Validate all input the user enters
   errors = validate_income(name, description, amount, date)
   # if there is no validation errors
   if len(errors)  == 0:
      # call the method to update expense item info
      update_expense = Income('expense', name, description, amount, date)
      update_expense.update(id)
      return redirect("/")
   else:
      # to view the same item we were trying to update
      expense = Income.get_by_id('expense', id)
      # if there is validation errors send them to view in template
      return render_template("update-expense.html", errors=errors, expense=expense)

# Delete Income Route
@app.route("/delete-income/<int:id>")
def del_inc(id):
   Income.delete('income', id)
   return redirect("/")

# Delete Expense Route
@app.route("/delete-expense/<int:id>")
def del_exp(id):
   Income.delete('expense', id)
   return redirect("/")

# Search Route and Function
@app.route('/search', methods=['GET', 'POST'])
def search():
   # For security reasons we check the request method if it is POST
   if request.method == 'POST':
      search_text = request.form['search']
      # Search for income results
      income_results = [] # empty array to store results inside
      incomes = Income.get_all('income')
      if incomes != 'No Data Found!':
         for income_item in incomes:
            if income_item['name'].lower().find(search_text.lower()) != -1:
               income_results.append(income_item)
      # Search for expense results
      expense_results = [] # empty array to store results inside
      expenses = Income.get_all('expenses')
      if expenses != 'No Data Found!':
         for expense_item in expenses:
            if expense_item['name'].lower().find(search_text.lower()) != -1:
               expense_results.append(expense_item)
      return render_template("search-results.html", search_text=search_text, income_results=income_results, expense_results=expense_results)

   return render_template("search-result.html")
