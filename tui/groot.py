from __future__ import annotations

from textual.app import App, ComposeResult
from textual.scroll_view import ScrollView
from textual.widgets import Static

class GrootApp(App):
    """I am Groot."""
    
    def compose(self) -> ComposeResult:
        """I am Groot."""
        with ScrollView() as groot_view:
            # I am Groot
            groot_phrases = [
                "I am Groot.",
                "I am Groot?",
                "I am Groot!",
                "I... am... Groot.",
                "I AM GROOT!",
                "I am Groot...",
                "I. Am. GROOT.",
            ]
            
            # I am Groot!
            for i in range(50):
                yield Static(groot_phrases[i % len(groot_phrases)])
    
    def on_mount(self) -> None:
        """I am Groot."""
        groot_view = self.query_one(ScrollView)
        groot_view.scroll_to(y=0, animate=True)
