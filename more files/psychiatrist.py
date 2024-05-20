import tkinter as tk
import openai

# Set your OpenAI API key here
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Initialize the OpenAI API
openai.api_key = OPENAI_API_KEY

# Function to get the chatbot response
def get_chatbot_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=150,
        stop=None,
    )
    return response.choices[0].text.strip()

# Function to handle user input
def send_message():
    user_input = user_entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_log.config(state=tk.DISABLED)

    # Show typing indicator
    chat_log.insert(tk.END, "Dr. ChatGPT is typing...\n", "bot")

    # Get chatbot response
    chatbot_response = get_chatbot_response(user_input)

    # Add slight delay to simulate processing time
    root.after(1000, show_chatbot_response, chatbot_response)

def show_chatbot_response(chatbot_response):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Dr. ChatGPT: " + chatbot_response + "\n", "bot")
    chat_log.config(state=tk.DISABLED)

# Create the GUI window
root = tk.Tk()
root.title("Psychiatrist Chatbot")

# Create a text widget to display the chat
chat_log = tk.Text(root, width=50, height=15)
chat_log.config(state=tk.DISABLED)
chat_log.tag_config("user", foreground="blue")
chat_log.tag_config("bot", foreground="red")

# Create an entry widget for user input
user_entry = tk.Entry(root, width=50)
user_entry.bind("<Return>", lambda event: send_message())

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)

# Greet the user with a welcome message
welcome_message = "Dr. ChatGPT: Welcome! I'm here to listen and help.\n"
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, welcome_message, "bot")
chat_log.config(state=tk.DISABLED)

# Grid layout
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
user_entry.grid(row=1, column=0, padx=10, pady=5)
send_button.grid(row=1, column=1, padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
