class Account(object):
    def __init__(self, b, c, d):
        self.bank_name = 'sc 은행'
        self.b = b
        self.c = c
        self.d = d

    def get_account(self):
        return f'{self.a}{self.b}{self.c}{self.d}'


    @staticmethod
    def main():
        while 1:
            menu = input('')
            if menu == 0:
                break
