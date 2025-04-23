import os
import anthropic
import json
from datetime import datetime


class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.history = []

    def _add_to_history(self, role: str, content: str):
        self.history.append({"role": role, "content": content})


    def chat(self, prompt: str, model: str = "claude-3-haiku-20240307") -> str:
        self._add_to_history("user", prompt)
        messages = self.history

        response = self.client.messages.create(
            model=model,
            max_tokens=1000,
            messages=messages
        )
        response_text = response.content[0].text
        self._add_to_history("assistant", response_text)
        
        return response_text
    
    def save_conversation(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"chats/conversation_{timestamp}.json"
        
        with open(filename, 'w') as file:
            json.dump(self.history, file)

