import sys
from application import Application
import openai
import platform
import os


def save_persistent_variable(name, value):
    os_type = platform.system()

    if os_type == "Windows":
        import winreg as reg
        key_path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        try:
            with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_SET_VALUE | reg.KEY_WOW64_64KEY) as env_key:
                reg.SetValueEx(env_key, name, 0, reg.REG_SZ, value)
                print(f"{name}={value} added to system environment variables")
        except PermissionError:
            print("Administrator privileges are required to set system environment variables on Windows.")
        
    elif os_type in ["Linux", "Darwin"]:
        profile_path = os.path.expanduser("~/.profile")
        with open(profile_path, "a") as f:
            f.write(f"\nexport {name}={value}\n")
            print(f"{name}={value} added to {profile_path}")

    else:
        print(f"Unsupported OS type: {os_type}")


def set_variable_if_not_exists(name):
    existing_value = os.environ.get(name)

    if existing_value is None:
        new_value = input(f"Environment variable {name} not found. Please enter its value: ")
        
        save_persistent_variable(name, new_value)
    else:
        print(f"Environment variable {name} already exists with value: {existing_value}")





import os

if len(sys.argv) > 1:
    if "OPENAI_API_KEY" not in os.environ:
        raise Exception("OPENAI_API_KEY environment variable not set")
    if "AWS_ACCESS_KEY" not in os.environ:
        raise Exception("AWS_ACCESS_KEY environment variable not set")
    if "AWS_SECRET_KEY" not in os.environ:
        raise Exception("AWS_SECRET_KEY environment variable not set")
        
    
    openai.api_key = os.environ["OPENAI_API_KEY"]

    prompt = " ".join(sys.argv[1:])
    #app = Application()
    #app.run(prompt) #TODO: this is too much code change it later
else:
    set_variable_if_not_exists("OPENAI_API_KEY")
    set_variable_if_not_exists("AWS_ACCESS_KEY")
    set_variable_if_not_exists("AWS_SECRET_KEY") 

    print("All keys ready. Use ./ChatSynthesis.py <prompt> to generate text for speech synthesis.")

