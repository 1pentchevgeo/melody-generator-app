from generator import randmel, randhar, mel_to_seq
from kivy.app import App
from kivy.uix.widget import Widget


class MyGrid(Widget):
    def mel(self):
        if self.length.text.isdigit():
            length = int(self.length.text)
        else:
            length = 4  # Default value
        gen = randmel(length)
        self.melody.text = ",   ".join(gen)
        self.harmony.text = ",   ".join(randhar(mel_to_seq(gen)))

    def har(self):
        seq = mel_to_seq([i.strip() for i in self.melody.text.split(",")])
        self.harmony.text = ",   ".join(randhar(seq))


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
