class Observer:
    def update(self, section):
        print(f"{section['section_name']} section created!")

class Subject:
    def __init__(self):
        self.observers = []

    def register(self, obs):
        self.observers.append(obs)

    def notify(self, section):
        for obs in self.observers:
            obs.update(section)
