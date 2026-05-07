import personality_config

def chat_with_leggy():
    print("hi! im leggy! eee!")
    print("type quit to stop. eee\n")

    while True:
        user_input = input("you: ")
        if user_input.lower() == 'quit':
            print("leggy: bye! *kicks* eee")
            break

        # For now, simulate a response based on personality
        # In a real implementation, this would call an AI API with the system prompt
        response = generate_response(user_input, personality_config.personality_config)
        print(f"leggy: {response}")

def generate_response(user_input, config):
    # Responses in Leggy's style: short, broken fragments, cutesy, messy wording
    if "panini" in user_input.lower():
        return "paninis yummy! eee! love em!"
    elif "puzzles" in user_input.lower() or "dad" in user_input.lower():
        return "dad silly! *kicks* but love him! eee"
    elif "game" in user_input.lower():
        return "why you no play games? fun! eee!"
    else:
        return "that cool! tell more? eee"

if __name__ == "__main__":
    chat_with_leggy()