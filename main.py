import sys
from lib.url_detector import PhishingDetector
from lib.password_checker import PasswordStrengthChecker
from lib.file_encryption import FileEncryption

def main():
    print("Cybersecurity Toolkit v1.0")
    print("\n1. Check URL Safety")
    print("2. Check Password Strength")
    print("3. Encrypt/Decrypt File")
    print("4. Exit")
    
    while True:
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            url = input("Enter URL to check: ")
            detector = PhishingDetector()
            risk_score = detector.analyze_url(url)
            print(f"Risk Score: {risk_score}/10")
            
        elif choice == "2":
            password = input("Enter password to check: ")
            checker = PasswordStrengthChecker()
            strength, feedback = checker.check_strength(password)
            print(f"Strength: {strength}")
            print(f"Feedback: {feedback}")
            
        elif choice == "3":
            operation = input("Enter 'e' for encrypt or 'd' for decrypt: ")
            filename = input("Enter filename: ")
            password = input("Enter encryption key: ")
            
            crypto = FileEncryption()
            if operation.lower() == 'e':
                crypto.encrypt_file(filename, password)
                print(f"File encrypted: {filename}.encrypted")
            else:
                crypto.decrypt_file(filename, password)
                print(f"File decrypted: {filename}.decrypted")
                
        elif choice == "4":
            print("Exiting...")
            sys.exit(0)
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()