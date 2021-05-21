class Account(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.BANK_NAME = 'SC은행'
        self.acc_number = self.create_acc_number()

    def create_acc_number(self):
        pass

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':
                break
            elif menu == '1':
                pass
            elif menu == '2':
                pass
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            else :
                print('Wrong Number')
                continue

Stock.main()

