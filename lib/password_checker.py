import re
from collections import defaultdict

class PasswordStrengthChecker:
    def __init__(self):
        self.min_length = 8
        self.common_passwords = {
            'password', '123456', 'qwerty', 'admin',
            'letmein', 'welcome', 'monkey', 'dragon'
        }
        
    def check_strength(self, password):
        """Check password strength and return score and feedback."""
        score = 0
        feedback = []
        
        # Check length
        if len(password) < self.min_length:
            feedback.append(f"Password should be at least {self.min_length} characters")
        else:
            score += 2
            
        # Check for common passwords
        if password.lower() in self.common_passwords:
            feedback.append("Password is too common")
            return "Weak", feedback
            
        # Check for character types
        if re.search(r'[A-Z]', password):
            score += 2
        else:
            feedback.append("Add uppercase letters")
            
        if re.search(r'[a-z]', password):
            score += 2
        else:
            feedback.append("Add lowercase letters")
            
        if re.search(r'\d', password):
            score += 2
        else:
            feedback.append("Add numbers")
            
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 2
        else:
            feedback.append("Add special characters")
            
        # Determine strength level
        if score >= 8:
            strength = "Strong"
        elif score >= 6:
            strength = "Moderate"
        else:
            strength = "Weak"
            
        return strength, feedback