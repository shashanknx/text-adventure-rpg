# Import required modules
import openai

# Function to validate OpenAI API key
def validate_api_key(api_key):
    try:
        # Example validation: Use an OpenAI API call to test the key
        openai.api_key = api_key
        openai.Model.list()
        return True
    except Exception as e:
        print("Invalid API key. Please check and try again.")
        return False

# Main function of the game
def main():
    print("Welcome to Text Adventure RPG!")

    # Prompt user for OpenAI API key
    while True:
        api_key = input("Please enter your OpenAI API key: ")
        if validate_api_key(api_key):
            print("API key validated successfully!")
            break
        else:
            print("Failed to validate the API key. Make sure it is correct.")

    # Example: Assign the validated API key for later use
    openai.api_key = api_key

    # Rest of the game logic
    print("Starting the game...")

if __name__ == "__main__":
    main()