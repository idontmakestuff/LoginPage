
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


class LoginScreen(Screen):
    pass

LoginPageApp().run()