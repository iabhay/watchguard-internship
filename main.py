from register.register import Register
from login.login import Login
from config.config import Config


class QuizLix:
    def __init__(self):
        self.register = Register()
        self.login = Login()

    def menu(self):
        print("QuizGuard  : Smart Quiz, Simply Played!!")
        ask = int(input(Config.MAIN_PROMPT))
        if 1 > ask or ask > 2:
            print("Bye! Thanks for playing.")
        while 0 < ask < 3:
            if ask == 1:
                self.register.register_module()
            elif ask == 2:
                self.login.loginmodule()
            else:
                print("Please Select Carefully!")
            ask = int(input(Config.MAIN_PROMPT))
            if ask == 3:
                print("Bye! Thanks for playing.")


if __name__ == "__main__":
    # Config = Config.load()
    Config.load()
    quiz_obj = QuizLix()
    quiz_obj.menu()
