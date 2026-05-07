import personality_config
from openai import OpenAI
import os

# Set your OpenAI API key here
api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None

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

def chat_with_leggy():
    print("hewo! im leggy! eee!")
    print("type quit to stop. eee\n")

    system_prompt = personality_config.personality_config['system_prompt']
    messages = [{"role": "system", "content": system_prompt}]

    while True:
        user_input = input("you: ")
        if user_input.lower() == 'quit':
            print("leggy: bye! *kicks* eee")
            break

        messages.append({"role": "user", "content": user_input})

        if client:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # or gpt-4 if available
                    messages=messages,
                    max_tokens=150,
                    temperature=0.8  # for creativity
                )
                ai_response = response.choices[0].message.content.strip()
                print(f"leggy: {ai_response}")
                messages.append({"role": "assistant", "content": ai_response})
            except Exception as e:
                print(f"leggy: oops! error: {str(e)} eee")
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