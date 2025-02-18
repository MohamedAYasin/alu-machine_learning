#!/usr/bin/env python3

def main():
    while True:
        user_input = input("Q: ").strip()

        if user_input.lower() in ["exit", "quit", "goodbye", "bye"]:
            print("A: Goodbye")
            break
        else:
            print("A: ")

if __name__ == "__main__":
    main()
