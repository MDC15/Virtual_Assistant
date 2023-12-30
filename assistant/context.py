
class Context:
    def __init__(self):
        self.user_name = ""
        self.user_preferences = {}

    def set_user_name(self, name):
        self.user_name = name

    def get_user_name(self):
        return self.user_name

    def set_user_preferences(self, preferences):
        self.user_preferences = preferences

    def get_user_preferences(self):
        return self.user_preferences

