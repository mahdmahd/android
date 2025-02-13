import openai
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# Set your OpenAI API key
openai.api_key = ".."

def call_openai(prompt):
    """
    Send the prompt to the OpenAI API and return the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini-2024-07-18",  # adjust your model if needed
            messages=[
                {"role": "system", "content": "تو یک دستیار پژوهش حرفه ای و آکادمیک هستی که هر سوالی که از تو می‌شود فقط به فارسی پاسخ می‌دهد."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling OpenAI API: {e}"

class TranslationTab(BoxLayout):
    def __init__(self, **kwargs):
        super(TranslationTab, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Selected Text input.
        self.selected_text_input = TextInput(
            hint_text="Selected Text: Enter the selected text here...",
            size_hint_y=None,
            height=150
        )
        self.add_widget(self.selected_text_input)

        # Context input.
        self.context_input = TextInput(
            hint_text="Context: Enter the context here...",
            size_hint_y=None,
            height=150
        )
        self.add_widget(self.context_input)

        # Button to send prompt.
        self.send_button = Button(
            text="Send to OpenAI",
            size_hint_y=None,
            height=50
        )
        self.send_button.bind(on_release=self.send_to_openai)
        self.add_widget(self.send_button)

        # Response output.
        self.response_output = TextInput(
            text="",
            readonly=True,
            halign='right',
            font_name="Tahoma",
            font_size=14
        )
        self.add_widget(self.response_output)

    def send_to_openai(self, instance):
        selected_text = self.selected_text_input.text.strip()
        context = self.context_input.text.strip()

        if not selected_text:
            self.response_output.text = "Please enter some selected text."
            return

        if not context:
            self.response_output.text = "Please enter some context."
            return

        prompt = (
            "Please give me the content-aware translation of '{}' in the following text. "
            "Explain its literal meaning and contextual significance and meaning in the paragraph:\n\n"
            "...{}..."
        ).format(selected_text, context)

        self.response_output.text = "Sending prompt:\n" + prompt + "\n\n"
        response = call_openai(prompt)
        self.response_output.text += "Response:\n" + response

class ExplainTab(BoxLayout):
    def __init__(self, **kwargs):
        super(ExplainTab, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Prompt text input.
        self.prompt_text_input = TextInput(
            hint_text="Prompt Text: Enter the text to be explained...",
            size_hint_y=None,
            height=150
        )
        self.add_widget(self.prompt_text_input)

        # Button to send prompt.
        self.send_button = Button(
            text="Send to OpenAI",
            size_hint_y=None,
            height=50
        )
        self.send_button.bind(on_release=self.send_to_openai)
        self.add_widget(self.send_button)

        # Response output.
        self.response_output = TextInput(
            text="",
            readonly=True,
            halign='right',
            font_name="Tahoma",
            font_size=14
        )
        self.add_widget(self.response_output)

    def send_to_openai(self, instance):
        prompt_text = self.prompt_text_input.text.strip()

        if not prompt_text:
            self.response_output.text = "Please enter some text for explanation."
            return

        prompt = (
            "Please give me the content-aware translation the following text. "
            "Explain its literal meaning and contextual significance and the paragraph meaning: {}"
        ).format(prompt_text)

        self.response_output.text = "Sending prompt:\n" + prompt + "\n\n"
        response = call_openai(prompt)
        self.response_output.text += "Response:\n" + response

class MainTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super(MainTabbedPanel, self).__init__(**kwargs)
        self.do_default_tab = False  # we'll add our own tabs

        # Create the Translation tab.
        translation_tab = TabbedPanelItem(text="Translation")
        translation_tab.content = TranslationTab()
        self.add_widget(translation_tab)

        # Create the Explain tab.
        explain_tab = TabbedPanelItem(text="Explain")
        explain_tab.content = ExplainTab()
        self.add_widget(explain_tab)

class OpenAIApp(App):
    def build(self):
        # Optionally set a background color for the window.
        Window.clearcolor = (1, 1, 1, 1)  # white background
        return MainTabbedPanel()

if __name__ == '__main__':
    OpenAIApp().run()
