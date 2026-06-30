import sys as s

if __name__ == "__main__":
    if s.base_prefix == s.prefix:
        print("MATRIX STATUS: You’re still plugged in\n")
        print(f"Current Python: {s.executable}")
        print("Virtual Env: None detected\n")
        print("WARNING: You’re in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv .matrix_env")
        print("source .matrix_env/bin/activate # On Unix")
        print("source .matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {s.executable}")
        print(f"Virtual Env: {s.prefix.split("/")[-1]}")
        print(f"Environment path: {s.prefix}\n")
        print("SUCCESS: You’re in an isolated environment")
        print(
            "Safe to install packages without affecting the global system.\n"
        )
        print(f"Package installation path:\
{s.prefix}/lib/python3.11/site-packages\n")
