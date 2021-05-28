class bank:
    def __init__(self,name,account,password,) :
        self.name=name
        self.account=account
        self.password=password
    def card(self):
        return f"hello this is{self.name} my account number {self.account} password  {self.password} "

    def withraw(self):
        withraw=385000
        save=277800
        return "I will withdraw KES {} and save KES {}.".format(withraw,save,)
