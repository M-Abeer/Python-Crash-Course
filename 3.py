# Define some common greetings
greetings = ["hi", "hello", "hey", "howdy"]

# Define a dictionary to map user phrases to responses
responses = {
    "how are you": "I'm doing well, thanks for asking! How about you?",
    "what can you do": "I can engage in simple conversations. Ask me anything about the weather, or tell me a joke!",
    "weather": "Hmm, I don't have real-time weather information, but what's the weather like for you today?",
    "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "goodbye": "Bye! Have a nice day.",
    "quit": None  # Special case to exit the conversation loop
}

def greet(user_input):
  """Greets the user based on their input."""
  if user_input.lower() in greetings:
    return "Hi there!"
  else:
    return None  # No greeting detected

def respond(user_input):
  """Provides a response based on keywords in the user input."""
  return responses.get(user_input.lower(), "Sorry, I don't understand what you mean by '{}'.".format(user_input))

# Start the conversation loop
while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break

  # Handle greetings first
  greeting_response = greet(user_input)
  if greeting_response:
    print("Chatbot:", greeting_response)
    continue

  # Provide a relevant response based on user input
  bot_response = respond(user_input)
  print("Chatbot:", bot_response)

