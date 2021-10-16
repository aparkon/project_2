# Import necessary libraries
import questionary
import sys

# Ask the users name
name = questionary.text("What is your first name?").ask()

# Welcome user to app
print(f"Hello {name}! Thank you for allowing us to join your journey to automated stock success! Please complete this brief questionnaire so that we can best serve your needs.")

# Ask user what their risk level is
risk_level = questionary.select("What is your risk level?", choices=["Conservative", "Moderate", "Risky"]).ask()

# If statements to determine the % gain associated with the user's risk level
conservative_gain = '3-7%'
moderate_gain = '7-12%'
risky_gain = '12+%'

if risk_level == 'Conservative':
    percent_gain = conservative_gain
elif risk_level == 'Moderate':
    percent_gain = moderate_gain
else:    
    percent_gain = risky_gain

# Print their risk level along with the associated percentage gain
print(f"At a {risk_level} risk level, you can expect a {percent_gain} percent gain.")
questionary.confirm("Would you like to proceed?").ask()

# Ask user what stock they would like to look analyze
if risk_level == 'Conservative':
    stock_choice = questionary.select("What stock would you like to analyze?", choices=["JNJ", "PG", "KO"]).ask()
elif risk_level == 'Moderate':
    stock_choice = questionary.select("What stock would you like to analyze?", choices=["MSFT", "AAPL", "NFLX"]).ask()
else:
    stock_choice = questionary.select("What stock would you like to analyze?", choices=["BTC", "TKAT", "TSLA"]).ask()

# Ask user what their ideal timeframe is to reach their goal
timeframe = questionary.select("When would you like to reach your goal?", choices = ["one day", "one week", "one month", "one year"]).ask()

# Print the summary of the users choices and ask user if they would like to proceed
print(f"You have chosen to analyze {stock_choice} at a {risk_level} risk level that will expect a {percent_gain} percentage gain over {timeframe}.")
confirm = questionary.text("Would you like to proceed? Please type Yes or No.").ask()

if confirm == 'Yes':
    print("Let's get started!")
else:
    sys.exit("Please review your options and chooes again.")
