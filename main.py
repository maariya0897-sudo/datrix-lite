from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Set background color
Window.clearcolor = (0.05, 0.08, 0.12, 1) # Dark Cyberpunk Theme

class DatrixLiteApp(App):
    def build(self):
        self.title = 'Datrix Lite AI'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header Label
        self.header = Label(
            text="[b]DATRIX LITE AI[/b]\n[size=14]Autonomous Agentic Assistant[/size]", 
            markup=True,
            font_size='22sp',
            color=(0.2, 0.8, 1, 1),
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.header)
        
        # Output Log Box
        self.output_box = Label(
            text="Datrix Lite System Initialized...\nReady for instructions.",
            font_size='16sp',
            color=(0.9, 0.9, 0.9, 1),
            size_hint=(1, 0.5),
            halign='center',
            valign='middle'
        )
        self.output_box.bind(size=self.output_box.setter('text_size'))
        layout.add_widget(self.output_box)
        
        # Command Input Box
        self.input_field = TextInput(
            hint_text="Enter command for Datrix...",
            multiline=False,
            size_hint=(1, 0.15),
            background_color=(0.15, 0.2, 0.25, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[10, 10, 10, 10]
        )
        layout.add_widget(self.input_field)
        
        # Execute Button
        self.run_btn = Button(
            text="EXECUTE AGENT",
            size_hint=(1, 0.15),
            background_color=(0, 0.6, 0.9, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        self.run_btn.bind(on_press=self.process_command)
        layout.add_widget(self.run_btn)
        
        return layout

    def process_command(self, instance):
        user_text = self.input_field.text.strip()
        if user_text:
            self.output_box.text = f"Executing Command:\n'{user_text}'\n\n[Status: Task Completed Successfully]"
            self.input_field.text = ""
        else:
            self.output_box.text = "Please enter a valid command."

if __name__ == '__main__':
    DatrixLiteApp().run()
