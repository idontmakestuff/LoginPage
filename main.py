
#
# class Question1Screen(Screen):
#     def answer_question(self, bool):
#         if bool:
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "error"
#
# class Question2Screen(Screen):
#     def answer_question(self, answer):
#         if answer.lower()=="purple":
#             self.manager.current = "correct"
#         else:
#             self.ids.invalid_guess.text = "Invalid guess. \n Try again!"
#             self.ids.invalid_guess.color = "red"
# class CorrectScreen(Screen):
#     def next_question(self):
#         self.manager.current = "question2"
#
# class ErrorScreen(Screen):
#     def next_question(self):
#         self.manager.current = "question2"
#
#
#
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
#
#
Builder.load_file("LoginPage.kv")


class LoginPageApp(App):
    def build(self):
        return LoginManager()

#
#
class LoginManager(ScreenManager):
    pass

class WelcomeScreen(Screen):
    def logout(self):
        self.manager.current="login"
class LoginScreen(Screen):
    def login(self,username,password):
        if username in users:
            if password==users[username]:
                self.manager.current="welcome"
            else:
                self.ids.notif.text="Incorrect Password!"
        else:
            self.ids.notif.text = "User does not exist"
    def gosignup(self):
        self.manager.current="signup"

class SignupScreen(Screen):

    def signup(self,newuser,newpass,newpass2):
        global users
        if newuser in users:
            self.ids.sign_notif.text = "Username taken"
        else:
            if caps in newpass:
                if lowercase in newpass:
                    if nums in newpass:
                        if special_chars in newpass:
                            if len(newpass)>= 8:
                                if newpass==newpass2:

                                    users[newuser]=newpass
caps= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums=["0","1","2","3","4","5","6","7","8","9"]
special_chars=["!","@","#","$","%","^","&","*","(",")","_","-","+","=","[","]","{","}",".",","]
users = {"MrGreen":"$$$$$$"}
LoginPageApp().run()

print("AAAAAAA")