import re

def add_time(start_time, duration, day=False):
    # Split start_time into hours, minutes, and period (AM/PM)
    current_time, time_format = start_time.split()
    current_hours, current_minutes = current_time.split(":")
    added_hours, added_minutes = duration.split(":")

    # Variable to track the number of days passed
    incoming_days = 0

    # Calculate total minutes and hours
    total_minutes = int(current_minutes) + int(added_minutes)
    total_hours = int(current_hours) + int(added_hours)
    
    # If total minutes exceed 60, adjust minutes and increment hours
    if total_minutes >= 60:
        total_minutes -= 60
        total_hours += 1      

    # Convert to 12-hour clock system
    if total_hours >= 12 and total_hours < 24:
        close_hours = int(total_hours / 12) * 12  # Adjust hours to 12-hour format
     
        # Toggle AM/PM format when exceeding 12 hours
        if total_hours >= 12:
            if time_format == "AM":
                time_format = "PM"
            else:
                time_format = "AM"
                incoming_days += 1  # Crossing midnight means a new day
        
        # Ensure hours stay within the 12-hour format
        if total_hours > 12:
            total_hours = total_hours - close_hours

    # Handle cases when total hours exceed 24 (multiple days added)
    if total_hours >= 24:
        incoming_days = round(total_hours / 24)  # Count how many full days pass
        close_hours = int(total_hours / 24) * 24  # Normalize hours
        total_hours = total_hours - close_hours
        
        # Toggle AM/PM format correctly
        if total_hours >= 12:
            if time_format == "AM":
                time_format = "PM"
            else:
                time_format = "AM"
        
        # Keep hours within 12-hour format
        if total_hours > 12:
            total_hours = total_hours - 12

    # Ensure minutes are properly formatted as two digits
    if total_minutes < 10:
        total_minutes = '0' + str(total_minutes)
    
    # Create a message to indicate next day(s) if applicable
    msg = ""
    if incoming_days == 1:
        msg = "(next day)"
    elif incoming_days > 1:
        msg = f'({incoming_days} days later)'
    
    # Handle weekday calculation if a day is provided
    if day:
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # Validate input day using regex search
        searched_days = re.findall(fr'{day}', "".join(days_of_the_week), re.IGNORECASE)
        if not searched_days:
            return f"\n{day} does not constitute a valid day of the week. Please provide an appropriate day.\n"
        
        refined_day = searched_days[0]  # Extract matched day
        
        # Get the index of the given day
        day_number = days_of_the_week.index(refined_day)
       
            
        # Rotate the list to start from the given day
        refined_week_days = days_of_the_week[day_number:] + days_of_the_week[:day_number]
        
        # Find the new weekday after adding days
        day_position = incoming_days
        while incoming_days > 7:
            day_position = incoming_days - 7
            incoming_days -= 7
        
        if day_position == 7:
            day_position -= 1  # Ensure valid index
        
        exact_week_day = refined_week_days[day_position]
        return f'{total_hours}:{total_minutes} {time_format}, {exact_week_day} {msg}'
    
    # Return final formatted time without weekday
    return f'{total_hours}:{total_minutes} {time_format} {msg}'


