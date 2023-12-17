class RangeItem:
    def __init__(self, text, min_value, max_value, current_value, step=1):
        self.text = text
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = current_value
        self.step = step

    def set(self, pos):
        pass


class SelectedItem:
    def __init__(self, text, selection_list, selected=0):
        self.text = text
        self.selection_list = selection_list
        self.selected = selected

    def set(self, ind):
        pass

    def get(self):
        return self.selection_list[self.selected]


class ToggleItem:
    def __init__(self, text, toggle_value):
        self.text = text
        self.toggle_value = toggle_value

    def toggle(self):
        self.toggle_value = not self.toggle_value


class GameSetting:
    def __init__(self):
        self.sound_volume = RangeItem('Громкость', 1, 100, 50)
        self.is_mute = ToggleItem('Без звука', False)
        self.display_sizes = SelectedItem('Расширение экрана',
                                          [(600, 500), (1280, 800)])

    def get_display_size(self):
        return self.display_sizes.get()

    def load(self, path):
        pass

    def save(self, path):
        pass

