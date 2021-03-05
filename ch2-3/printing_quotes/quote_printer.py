class QuotePrinter(object):
    def ask_quotes(self):
        self.quotes = input("What is the quote? ")

    def ask_who_said(self):
        self.who_said = input("Who said it? ")

    def show_quotes_said(self):
        print(self.who_said + " says, " + "\"" + self.quotes + "\"")