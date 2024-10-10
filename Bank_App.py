class Account:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def create_account(self, acc_no, name, mobile_no, address):
        self.accounts[acc_no] = {
            'name': name,
            'mobile_no': mobile_no,
            'address': address,
            'balance': 0
        }
        print(f"Account created for {name} with Account Number: {acc_no}")

    def view_account_details(self, acc_no):
        if acc_no in self.accounts:
            return self.accounts[acc_no]
        else:
            return "Account not found."

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            if self.accounts[acc_no]['balance'] >= amount:
                self.accounts[acc_no]['balance'] -= amount
                self.transactions.append(f"Withdrawn {amount} from Account {acc_no}")
                return f"Withdrawal successful. New balance: {self.accounts[acc_no]['balance']}"
            else:
                return "Insufficient balance."
        else:
            return "Account not found."

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no]['balance'] += amount
            self.transactions.append(f"Deposited {amount} to Account {acc_no}")
            return f"Deposit successful. New balance: {self.accounts[acc_no]['balance']}"
        else:
            return "Account not found."

    def fund_transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc]['balance'] >= amount:
                self.accounts[from_acc]['balance'] -= amount
                self.accounts[to_acc]['balance'] += amount
                self.transactions.append(f"Transferred {amount} from Account {from_acc} to Account {to_acc}")
                return "Fund transfer successful."
            else:
                return "Insufficient balance."
        else:
            return "One or both accounts not found."

    def print_transactions(self):
        return self.transactions

Account_obj = Account()
while True:
    choice = int(input('''Enter the value of the related service you want
                     1. Create Account
                     2. View Account Details by AccNO
                     3. Withdraw
                     4. Deposit
                     5. Fund Transfer
                     6. Print Transactions
                     7. Exit
                     '''))
    if choice == 1:
        acc_no = input("Enter Account Number: ")
        name = input("Enter Account Holder Name: ")
        mobile_no = input("Enter Mobile Number: ")
        address = input("Enter Address: ")
        Account_obj.create_account(acc_no, name, mobile_no, address)
    elif choice == 2:
        acc_no = input("Enter Account Number: ")
        details = Account_obj.view_account_details(acc_no)
        print(details)
    elif choice == 3:
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter amount to withdraw: "))
        result = Account_obj.withdraw(acc_no, amount)
        print(result)
    elif choice == 4:
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter amount to deposit: "))
        result = Account_obj.deposit(acc_no, amount)
        print(result)
    elif choice == 5:
        from_acc = input("Enter your Account Number: ")
        to_acc = input("Enter recipient's Account Number: ")
        amount = float(input("Enter amount to transfer: "))
        result = Account_obj.fund_transfer(from_acc, to_acc, amount)
        print(result)
    elif choice == 6:
        transactions = Account_obj.print_transactions()
        for transaction in transactions:
            print(transaction)
    elif choice == 7:
        break
    else:
        print("Invalid choice. Please try again.")
