import os
import openai

def get_openai_api_key():
    """
    Retrieves the OpenAI API key from the environment variable 'OPENAI_API_KEY'.
    If not set, prompts the user to manually define it in the code.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found. Please set the environment variable 'OPENAI_API_KEY' or hardcode the key in the script (not recommended).")
    return api_key

def llm_storytelling():
    """
    Initiates a collaborative storytelling loop between the player and OpenAI's language model.
    """
    print("Welcome to the Collaborative Storytelling Adventure!")
    print("Here, you'll co-create a story with the power of AI.")

    # Retrieve API key and set up OpenAI
    openai.api_key = get_openai_api_key()

    # Initial prompt to start the story
    system_prompt = "You are a creative AI helping a player co-write an epic adventure story. Start with an opening.")

    print("\nThe AI will begin the story. Afterward, you can add your input to continue it.")
    context = ""  # This will store the evolving story as context

    # Start collaborative storytelling loop
    while True:
        # AI response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context}
            ]
        )
        ai_part = response.choices[0].message.content.strip()
        print("\nAI says:")
        print(ai_part)

        # Append AI output to context
        context += f"\nAI: {ai_part}"

        # Player input
        user_input = input("\nYour turn! Add your part to the story: ")
        context += f"\nPlayer: {user_input}"

        print("\nStory so far:")
        print(context)

        # Option to continue or exit
        continue_prompt = input("Do you want to continue the story? (yes/no): ").strip().lower()
        if continue_prompt in ("no", "n"):
            break

    print("\nThank you for playing! Your story has been saved.")

if __name__ == "__main__":
    try:
        llm_storytelling()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please configure your OpenAI API key and try again.")