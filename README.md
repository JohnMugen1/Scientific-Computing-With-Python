# Time Calculator

## Overview
This Python program calculates the resulting time after adding a duration to a given start time. It supports 12-hour AM/PM format and optionally determines the new weekday if provided.

## Features
- Handles time addition in 12-hour format (AM/PM).
- Determines the number of days passed after time addition.
- Computes the new weekday if an initial day is provided.
- Returns results in a human-readable format.

## Usage
```python
from time_calculator import add_time

# Example 1: Basic time addition
print(add_time("3:30 PM", "2:12"))  # Output: "5:42 PM"

# Example 2: Handling AM/PM transition
print(add_time("11:55 AM", "3:12"))  # Output: "3:07 PM"

# Example 3: Adding multiple days
print(add_time("9:15 PM", "25:00"))  # Output: "10:15 PM (next day)"

# Example 4: With weekday input
print(add_time("2:59 AM", "24:00", "Saturday"))  # Output: "2:59 AM, Sunday (next day)"
