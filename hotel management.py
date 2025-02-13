"""
Restaurant Management System
APU Degree Program - Group Assignment
"""
import os
from datetime import datetime

# Symbolic Constants
USER_FILES = {
    'admin': 'admin.txt',
    'manager': 'manager.txt',
    'chef': 'chef.txt',
    'customer': 'customer.txt'
}
MENU_FILE = 'menu.txt'
ORDERS_FILE = 'orders.txt'
FEEDBACK_FILE = 'feedback.txt'
INGREDIENTS_FILE = 'ingredients.txt'
MAX_LOGIN_ATTEMPTS = 3

def validate_password(password):
    """Basic password validation"""
    return len(password) >= 8  # Simple validation for demonstration
