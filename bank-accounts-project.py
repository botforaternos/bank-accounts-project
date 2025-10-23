# Bank Account Simulator by Bhasker Pandey

# File to save balance data
filename = "account_balance.txt"

def read_balance():
    try:
        with open(filename, "r") as f:
            balance = float(f.read())
    except (FileNotFoundError, ValueError):
        balance = 0.0  # default balance if no file or invalid content
    return balance

def write_balance(balance):
    with open(filename, "w") as f:
        f.write(str(balance))

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Deposit amount must be positive.")
    return balance

def withdraw(balance, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
    return balance

def check_balance(balance):
    print(f"Current balance: ${balance:.2f}")

def main():
    balance = read_balance()
    while True:
        print("\n--- Bank Account Simulator ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                balance = deposit(balance, amount)
                write_balance(balance)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                balance = withdraw(balance, amount)
                write_balance(balance)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using the Bank Account Simulator.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
