def calculate_duration(age, unit):
    # Conversion factors
    months_per_year = 12
    weeks_per_year = 52.1775
    days_per_year = 365.25
    hours_per_day = 24
    minutes_per_hour = 60
    seconds_per_minute = 60

    # Calculate the duration based on the chosen unit
    if unit in ['m', 'months', 'M', 'Months']:
        return age * months_per_year
    elif unit in ['w', 'weeks', 'W', 'Weeks']:
        return age * weeks_per_year
    elif unit in ['d', 'days', 'D', 'Days']:
        return age * days_per_year
    elif unit in ['h', 'hours', 'H', 'Hours']:
        return age * days_per_year * hours_per_day
    elif unit in ['min', 'minutes', 'Min', 'Minutes']:
        return age * days_per_year * hours_per_day * minutes_per_hour
    elif unit in ['s', 'seconds', 'S', 'Seconds']:
        return age * days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
    else:
        return None


def main():
    # Get user input
    age = float(input("What's your age? "))
    unit = input(
        "Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. Note: You can write the first letter or the full name of the time unit. ")

    # Calculate the duration
    duration = calculate_duration(age, unit)

    if duration is not None:
        # Display the result with the appropriate unit
        if unit in ['m', 'months', 'M', 'Months']:
            print(f"You lived for {duration} Months")
        elif unit in ['w', 'weeks', 'W', 'Weeks']:
            print(f"You lived for {duration:.2f} Weeks")
        elif unit in ['d', 'days', 'D', 'Days']:
            print(f"You lived for {duration:.2f} Days")
        elif unit in ['h', 'hours', 'H', 'Hours']:
            print(f"You lived for {duration:.2f} Hours")
        elif unit in ['min', 'minutes', 'Min', 'Minutes']:
            print(f"You lived for {duration:.2f} Minutes")
        elif unit in ['s', 'seconds', 'S', 'Seconds']:
            print(f"You lived for {duration:.2f} Seconds")
    else:
        print("Invalid time unit selected. Please try again.")


if __name__ == "__main__":
    main()
    