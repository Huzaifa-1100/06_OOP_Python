class Bank:
    bank_name = "Global Bank" #class variable
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
        
# Example Usage
b1 = Bank()
b2 = Bank()
print(F"Bank Name: {Bank.bank_name}") # Global Bank
Bank.change_bank_name("National Bank")
print(f"Updated Bank Name: {Bank.bank_name}") #National Bank