from dotenv import load_dotenv
from dotenv import load_dotenv
from ice_breaker.linkedin import getLinkedInProfile
from ice_breaker.simpleChain import simplePromptChain

load_dotenv()

# Connect Application To Linkedin


def main():
    profile_data = getLinkedInProfile()
    data = simplePromptChain(profile_data)
    print(data)


if __name__ == "__main__":
    main()
