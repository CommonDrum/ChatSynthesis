import os
import platform

def get_shell_path():
    shell = os.environ.get('SHELL')
    
    if shell.endswith('zsh'):
        file_path = os.path.expanduser('~/.zshrc')
    elif shell.endswith('bash'):
        file_path = os.path.expanduser('~/.bash_profile')
    else:
        raise Exception(f"Unsupported shell: {shell}")
    
    return file_path
    
    

def delete_persistent_variable(name):
    os_type = platform.system()

    if os_type == "Windows":
        import winreg as reg
        key_path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        try:
            with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_SET_VALUE | reg.KEY_WOW64_64KEY) as env_key:
                reg.DeleteValue(env_key, name)
                print(f"{name} removed from system environment variables")
        except PermissionError:
            print("Administrator privileges are required to set system environment variables on Windows.")
        
    elif os_type in ["Linux", "Darwin"]:
        file_path = get_shell_path()
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if not line.startswith(f'export {name}='):
                    file.write(line)

    else:
        print(f"Unsupported OS type: {os_type}")


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

        file_path = get_shell_path()
        with open(file_path, 'a') as file:
            file.write(f'export {name}="{value}"\n')

    else:
        print(f"Unsupported OS type: {os_type}")


def set_variable_if_not_exists(name):
    existing_value = os.environ.get(name)

    if existing_value is None:
        new_value = input(f"Environment variable {name} not found. Please enter its value: ")
        
        save_persistent_variable(name, new_value)
    else:
        print(f"Environment variable {name} already exists with value: {existing_value}")

