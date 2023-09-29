from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App


Builder.load_file("QuizPage.kv")
class QuizPageApp(App):
    def build(self):
        return QuizManager()


class QuizManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class Question2Screen(Screen):
    def answer_question(self, answer):
        if answer=="purple":
            self.manager.current = "correct"
        else:
            self.manager.current = "error"
class CorrectScreen(Screen):
    def next_question(self):
        self.manager.current = "question2"

class ErrorScreen(Screen):
    def next_question(self):
        self.manager.current = "question2"



QuizPageApp().run()