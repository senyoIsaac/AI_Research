class PasswordSecuritySystem:
    def __init__(self):
        self.attempts = 3
        self.blocked = False
        self.password = ""

    def set_password(self, password):
        if len(password) < 7:
            print("Password length must be at least 7 characters.")
            return
        self.password = password.lower()

    def login(self, password):
        if self.blocked:
            print("You have been blocked due to excessive attempts.")
            return
        if password.lower() != self.password:
            self.attempts -= 1
            print(f"Incorrect password. {self.attempts} attempts left.")
            if self.attempts == 0:
                self.blocked = True
            return
        print("Login successful!")

# Example usage:
security_system = PasswordSecuritySystem()
security_system.set_password("SecretPassword")
while True:
    password = input("Enter password: ")
    security_system.login(password)
