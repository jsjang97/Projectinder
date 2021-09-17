import sys


def update(issue_title, issue_url, preference):
    new_line = f"| [{issue_title}]({issue_url}) | |\n"
    if preference:
        new_line = f"| [{issue_title}]({issue_url}) | {preference} |\n"
    with open('./README.md', 'r') as file_handler:
        lines = file_handler.readlines()
    lines.insert(15, new_line)
    with open('./README.md', 'w') as file_handler:
        file_handler.writelines(lines)

def get_preference(issue_body):
    preference = None
    for line in issue_body.split('\n'):
        print(line)
        if line.strip().lower().startswith("project team") or line.strip().lower().startswith("project preference"):
            print(line)
            preference = line.split(":")[1].strip()
    
    return preference
    


if __name__ == "__main__":
    issue_title = sys.argv[1]
    issue_url = sys.argv[2]
    issue_body = sys.argv[3]
    
    preference = get_preference(issue_body)

    update(issue_title, issue_url, preference)
