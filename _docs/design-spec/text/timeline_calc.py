#!/usr/bin/env python3

# project_completion_calc.py

"""
Project Completion Date Calculator

Calculate and display the completion date for a project based on a given start date,
estimated number of weeks to complete, number of holidays, and number of developers.
The duration of the project is adjusted based on the number of developers:
- 1 developer: duration remains the same.
- 2 or more developers: duration is reduced to 75% of the original estimate.

Prompt user for:
- Project start date (e.g., January 10, 2025)
- Estimated number of weeks to complete the project
- Number of holidays during the period
- Number of developers (between 1 and 5)
"""

from datetime import datetime, timedelta

# prompt user for a date and ensure it is in the correct format ("Month Day, Year")
def get_valid_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            date_obj = datetime.strptime(date_str, "%B %d, %Y")
            return date_obj
        except ValueError:
            print("Please enter a valid date in the format 'Month Day, Year' (e.g., January 10, 2025).")

# prompt user for an integer within a specified range
def get_valid_int(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid number.")

# prompt user for confidence level with duration estimate and adjust completion date accordingly
def get_confidence_level(prompt, min_value, max_value):
    value = input(prompt)
    return value

# calculate project completion date based on provided parameters
def calculate_completion_date(start_date, weeks, holidays, developers, confidence):
    # adjust duration based on number of developers
    if developers == 2:
        weeks *= 0.75

    if developers > 2:
        weeks *= 0.667

    # adjust duration based on confidence level
    if confidence == '2':
        weeks *= 1.05

    if confidence == '3':
        weeks *= 1.15

    # convert weeks to days
    duration_days = weeks * 7

    # add holiday extension
    duration_days += holidays

    # calculate completion date
    completion_date = start_date + timedelta(days=duration_days)

    return completion_date

# Manage user input and call other functions to calculate and display the completion date
def main():
    print("\nProject Completion Date Calculator\n")
    
    start_date = get_valid_date("Enter the project start date (e.g., January 10, 2025): ")
    estimated_weeks = get_valid_int("Enter the estimated number of weeks to complete the project: ", 1, 104)
    holidays = get_valid_int("Enter the number of holidays during the period: ", 0, 366)
    developers = get_valid_int("Enter the number of developers (1-5): ", 1, 5)
    confidence = get_confidence_level("Enter your confidence level (1=optimistic, 2=neutral, 3=pessimistic): ", 1, 3)
    
    completion_date = calculate_completion_date(start_date, estimated_weeks, holidays, developers, confidence)
    print(f"\nThe estimated project completion date is: {completion_date.strftime('%B %d, %Y')}\n")

if __name__ == "__main__":
    main()