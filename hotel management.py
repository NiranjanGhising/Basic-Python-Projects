"""
Restaurant Management System
APU Degree Program - Group Assignment
"""
import os
from datetime import datetime

# File Constants
USER_FILE = "users.txt"
MENU_FILE = "menu.txt"
ORDERS_FILE = "orders.txt"
FEEDBACK_FILE = "feedback.txt"
INGREDIENTS_FILE = "ingredients.txt"
STAFF_FILE = "staff.txt"
PROFILE_FILE = "profile.txt"

# User Roles
ROLES = ["admin", "manager", "chef", "customer"]

# Initialize Files
def initialize_files():
    for file in [USER_FILE, MENU_FILE, ORDERS_FILE, FEEDBACK_FILE, INGREDIENTS_FILE, STAFF_FILE]:
        if not os.path.exists(file):
            open(file, 'w').close()

# File Operations
def read_data(filename):
    try:
        with open(filename, 'r') as f:
            data = [line.strip().split(';') for line in f]
            1
            return data
    except FileNotFoundError:
        return []

def write_data(filename, data):
    with open(filename, 'a') as f:
        f.write(';'.join(map(str, data)) + '\n')

# Validation Functions
def validate_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def validate_phone(phone):
    return len(phone) == 10 and phone.isdigit()