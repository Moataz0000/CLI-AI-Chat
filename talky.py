import os
import sys
import cmd
from termcolor import colored
from google import genai
from timer import ThinkingTimer
import time
from formater import clear_last_lines




class TalkyCLI(cmd.Cmd):
    prompt = colored("Ask >> ", color="yellow")
    intro = colored(
        "Hey — I'm Talky, your personal AI sidekick. Ready to roll? Type \"help\" for commands.\n",
        color="green"
    )
    def __init__(self, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        api_key = None

        if not api_key:
            print(colored("Missing GOOGLE_API_KEY in environment.", "red"), file=sys.stderr)
            api_key = input(colored("Please enter your Google API key: ", "yellow")).strip()

        self.client = genai.Client(api_key=api_key)

    def ask_ai(self, question: str):
        """Send a question to Gemini and print the answer."""
        if not question.strip():
            print(colored("Please type a question.", "red"))
            return
        
        lowered = question.strip().lower()
        if any(kw in lowered for kw in ["your name", "who are you", "what's your name", "what is your name", "yourname"]):
            print(colored("🤖 My name is Talky AI — your friendly terminal assistant!", "cyan"))
            print()
            return
        
        try:
            spinner = ThinkingTimer("Thinking")
            spinner.__enter__()

            # Ask Gemini
            resp = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Please provide a short, professional answer to the following question: {question}"
            )

            spinner.stop()
            clear_last_lines(1)

            print(colored(resp.text.strip(), "cyan"), end="\n")
            print("-"*100, end="\n")

        except Exception as e:
            try:
                spinner.stop()
                clear_last_lines(1)
            except Exception:
                pass
            print(colored(f"[Error] {e}", "red"), file=sys.stderr)

    def do_ask(self, line):
        """ask <question> — Send a question to the AI."""
        self.ask_ai(line)

    def default(self, line: str):
        self.ask_ai(line)

    def emptyline(self):
        pass



    def do_clear(self, line):
        """Clear the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")
        print(colored("Screen cleared!", "green"))

    def do_quit(self, line) -> bool:
        """Exit the CLI."""
        return True
    
    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        print()
        return stop


if __name__ == "__main__":
    TalkyCLI().cmdloop()
