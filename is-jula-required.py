import os

def get_env(env_name):
    try:
        return os.environ[env_name]
    except Exception as e:
        print(e)
        return "ERROR"        

print(get_env('PWD'))
print(get_env('github_workspace'))