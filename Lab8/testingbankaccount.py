import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):
    # 1
    def setUp(self):
        self.account = BankAccount("Bugs", 1000)

    # 2
    def test_account(self):
        self.assertEqual(self.account.owner, "Bugs")
        self.assertEqual(self.account.get_balance(), 1000)

    # 3 1000 + 500 = 1500 
    def test_deposit(self):
        self.account.deposit(500)

        self.assertEqual(self.account.get_balance(), 1500)

    # 4 1000 - 100 = 900
    def test_withdraw(self):
        self.account.withdraw(100)
    
        self.assertEqual(self.account.get_balance(), 900)

    # 5 1000 -2000 : Value exception error
    def test_exception(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    # 6 
    def test_transaction(self):
        # Start at 1000
        self.assertEqual(self.account.get_balance(), 1000)
        
        # 1000 + 500 = 1500
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

        # 1500 - 100 = 1400
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 1400)

        # 1400 - 1400 = 0
        self.account.withdraw(1400)
        self.assertEqual(self.account.get_balance(), 0) 

        # 0 + 1000 = 1500
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000) 

        # Check Final Balance is 1000
        self.assertEqual(self.account.get_balance(), 1000) 
       
if __name__ == "__main__":
    unittest.main()
