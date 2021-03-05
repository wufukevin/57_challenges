class MadLib(object):
    def ask_verb(self):
        self.verb = input("Enter a verb: ")

    def ask_noun(self):
        self.noun = input("Enter a noun: ")

    def ask_adv(self):
        self.adv = input("Enter an adv: ")

    def ask_adj(self):
        self.adj = input("Enter an adj: ")

    def tell_story(self):
        print(f"Do you {self.verb} your {self.adj} {self.noun} {self.adv}? That's hilarious!")