import tkinter as tk
import openai

openai.api_key = "YOUR API KEY"
model_engine = "text-davinci-003"
chatbot_prompt = """
As an advanced chatbot, your primary goal is to assist users to the best of your ability. This may involve answering questions, providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses. Use examples and evidence to support your points and justify your recommendations or solutions.
<conversation history>
User: <user input>
Chatbot:"""

def get_response(conversation_history, user_input):
    prompt = chatbot_prompt.replace(
        "<conversation history>", conversation_history).replace("<user input>", user_input)

    # Get the response from GPT-3
    response = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)
    return response.choices[0].text.strip()

def send_message(event = None):
    user_input = input_box.get()
    conversation_history = conversation_box.get(1.0, tk.END)
    response = get_response(conversation_history, user_input)
    conversation_box.insert(tk.END, f"\nUser: {user_input}")
    conversation_box.insert(tk.END, f"\nChatbot: {response}")
    input_box.delete(0, tk.END)

# Create the GUI window
window = tk.Tk()

window.config(width=600,height=600)

window.title("Chatbot")

# Add conversation history box
conversation_box = tk.Text(window, width=80, height=20,fg="green",bg="black")
conversation_box.pack(padx=10, pady=10)

# Add user input box
input_box = tk.Entry(window, width=60)
input_box.pack(side=tk.LEFT, padx=10, pady=10)

# Add send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=10)

input_box.bind("<Return>", send_message)

window.mainloop()



