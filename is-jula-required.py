import os

def get_env(env_name):
    try:
        return os.environ[env_name]
    except Exception as e:
        print(e)
        return "ERROR"        
    
def print_file_tree(start_path, prefix=""):
    # Iterate over the items in the directory
    items = os.listdir(start_path)
    items.sort()  # Sort items to list directories and files alphabetically

    for index, item in enumerate(items):
        path = os.path.join(start_path, item)
        # Check if the item is the last one in the directory to determine the prefix
        is_last = index == len(items) - 1
        
        if os.path.isdir(path):
            # If the item is a directory, print it and recurse into it
            print(prefix + "├── " + item if not is_last else prefix + "└── " + item)
            # Determine the new prefix for the child items
            new_prefix = prefix + "│   " if not is_last else prefix + "    "
            print_file_tree(path, new_prefix)
        else:
            # If the item is a file, just print it
            print(prefix + "├── " + item if not is_last else prefix + "└── " + item)    

root_path = get_env('github_workspace')
print(root_path)
print_file_tree(root_path)