from kivy.app import App
from kivy.uix.widget import Widget
from gamified_checklist.utils.logger import log_info

class GamifiedChecklistApp(App):
    def build(self):
        log_info("Building Gamified Checklist App", "App")
        return Widget()

if __name__ == '__main__':
    log_info("Starting Gamified Checklist App", "Main")
    GamifiedChecklistApp().run()
