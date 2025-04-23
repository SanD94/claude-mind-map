from api import ClaudeClient
from tui import BoardApp
from dotenv import load_dotenv
import atexit

# if __name__ == "__main__":
#     load_dotenv()
#     client = ClaudeClient()
#     # Register save method to be called on exit
#     atexit.register(client.save_conversation)
#     while True:
#         user_input = input("User: ")
# 
#         if user_input.lower() == "quit":
#             print("Conversation ended.")
#             break
#         response = client.chat(user_input)
#         print(response)

if __name__ == "__main__":
    app = BoardApp()
    app.run()
    

