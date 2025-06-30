import os
import subprocess
import sys
import re

def read_multiline(label):
    print(f"\n🔹 {label} (Paste here and press Ctrl+Z then enter (for Windows) or ctrl+D for (Linux/macOS) to finish):\n")
    return sys.stdin.read().strip()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📘 HackerRank Problem Archiver")

        problem_name = input("🔹 Problem name: ").strip()
        folder_name = re.sub(r'[\\/*?:"<>|]', "", problem_name.lower().replace(' ', '_').replace('-', '_'))

        print("Now enter the following sections:")

        print("📖 Problem Description:")
        description = read_multiline("Problem Description")

        print("📥 Sample Input/Output:")
        examples = read_multiline("Sample Input/Output")

        print("💻 Your Solution Code:")
        code = read_multiline("Solution Code")

        os.makedirs(folder_name, exist_ok=True)

        with open(f"{folder_name}/README.md", "w", encoding="utf-8") as f:
            f.write(f"# {problem_name}\n\n")
            f.write("## Problem Description\n")
            f.write(description + "\n\n")
            f.write("## Example Input/Output\n")
            f.write("```\n" + examples + "\n```\n")

        with open(f"{folder_name}/solution.py", "w", encoding="utf-8") as f:
            f.write(code + "\n")

        print(f"\n✅ Files saved to `{folder_name}/`")

        try:
            subprocess.run(["git", "add", folder_name], check=True)
            subprocess.run(["git", "commit", "-m", f"Add: {problem_name}"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("🚀 Pushed to GitHub successfully.\n")
        except subprocess.CalledProcessError as e:
            print("❌ Git operation failed:", e)
            print("💡 Make sure you're inside your Git repo and logged in.")

        cont = input("\n🔁 Add another problem? (y/n): ").strip().lower()
        if cont != 'y':
            print("👋 Done. Exiting.")
            break

if __name__ == "__main__":
    main()