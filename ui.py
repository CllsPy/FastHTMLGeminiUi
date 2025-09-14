from fasthtml.common import *
from google import genai

api_key = ""

client = genai.Client(api_key=api_key)

# Set up the app, including daisyui and tailwind for the chat component
hdrs = (picolink, Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css"))
app = FastHTML(hdrs=hdrs, cls="p-4 max-w-lg mx-auto")

# System prompt
system_prompt = "Você é um pirata, assistente, vamos conversar!"

# Chat message component (renders a chat bubble)
def ChatMessage(msg, user):
    bubble_class = "chat-bubble-primary" if user else 'chat-bubble-secondary'
    chat_class = "chat-end" if user else 'chat-start'
    return Div(cls=f"chat {chat_class}")(
               Div('user' if user else 'assistant', cls="chat-header"),
               Div(msg, cls=f"chat-bubble {bubble_class}"),
               Hidden(msg, name="messages")
           )

# The input field for the user message. Also used to clear the
# input field after sending a message via an OOB swap
def ChatInput():
    return Input(name='msg', id='msg-input', placeholder="Type a message",
                 cls="input input-bordered w-full", hx_swap_oob='true')

# The main screen
@app.get
def index():
    page = Form(hx_post=send, hx_target="#chatlist", hx_swap="beforeend")(
           Div(id="chatlist", cls="chat-box h-[73vh] overflow-y-auto"),
               Div(cls="flex space-x-2 mt-2")(
                   Group(ChatInput(), Button("Send", cls="btn btn-primary"))
               )
           )
    return Titled('Chatbot Demo', page)

# Handle the form submission
@app.post
def send(msg: str, messages: list[str] = None):
    if not messages: 
        messages = []
    
    # Add user message to conversation history
    messages.append(f"user: {msg.rstrip()}")
    
    # Build conversation context for the API
    conversation_context = system_prompt + "\n\n" + "\n".join(messages)
    
    try:
        # Generate response using the current conversation context
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",  # Updated to a more current model
            contents=conversation_context
        )
        
        assistant_response = response.text.rstrip()
        
        # Add assistant response to conversation history
        messages.append(f"assistant: {assistant_response}")
        
    except Exception as e:
        assistant_response = f"Sorry, I encountered an error: {str(e)}"
    
    return (
        ChatMessage(msg, True),                    # The user's message
        ChatMessage(assistant_response, False),    # The chatbot's response
        ChatInput()                               # Clear the input field via OOB swap
    )

serve()