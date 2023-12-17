from abc import ABC, abstractmethod


class IState(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def handle_input(self, event):
        pass


class GameStateManager:
    def __init__(self):
        self.states = {}  # Словарь для хранения состояний
        self.current_state = None

    def add_state(self, state_name, state_instance: IState):
        self.states[state_name] = state_instance

    def set_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]
        else:
            print(f"Состояние '{state_name}' не найдено.")

    def update(self):
        if self.current_state:
            self.current_state.update()

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)

    def handle_events(self, event):
        if self.current_state:
            self.current_state.handle_input(event)
