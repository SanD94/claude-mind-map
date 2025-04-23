from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input
from textual.scroll_view import ScrollView
from textual.reactive import reactive
from typing import Optional
from textual.app import App, ComposeResult

# Modular chatbot logic placeholder
def get_bot_response(message: str) -> str:
    # Replace this with your own chatbot logic
    return f"Echo: {message}"

class ChatHistory(ScrollView):
    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)
        self.messages = []

    def add_message(self, message: str):
        self.messages.append(message)
        self.update("\n".join(self.messages))

class MainConversation(ScrollView):
    def __init__(self):
        super().__init__()
        self.messages = []

    def add_message(self, speaker: str, message: str):
        self.messages.append(f"[{speaker}] {message}")
        self.update("\n".join(self.messages))


class ChatApp(App):
    CSS = """
    Screen {
        layout: vertical;
    }
    Horizontal {
        height: 1fr;
    }
    ChatHistory {
        width: 30%;
        height: 100%;
    }
    MainConversation {
        width: 100%;
        height: 1fr;
    }
    Input {
        width: 100%;
        border: heavy $accent;
    }
    """

    BINDINGS = [("ctrl+c", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        self.chat_history = ChatHistory()
        self.main_convo = MainConversation()
        self.input_field = Input(placeholder="Type your message...")

        yield Horizontal(
            self.chat_history,
            Vertical(
                self.main_convo,
                self.input_field
            )
        )

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        user_msg = message.value.strip()
        if not user_msg:
            return

        # Add to both views
        self.chat_history.add_message(f"You: {user_msg}")
        self.main_convo.add_message("You", user_msg)

        # Process chatbot response
        bot_reply = get_bot_response(user_msg)
        self.chat_history.add_message(f"Bot: {bot_reply}")
        self.main_convo.add_message("Bot", bot_reply)

        # Clear input
        self.input_field.value = ""


