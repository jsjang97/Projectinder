import sys


def update_list(issue_title, issue_url, preference):
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
    try:
        for line in issue_body.split('\n'):
            print(line)
            if (
                line.strip().lower().startswith("project teaming")
                or line.strip().lower().startswith("project preference")
                or line.strip().lower().startswith("**project teaming")
                or line.strip().lower().startswith("**project preference")
            ):
                print(line)
                preference = line.split(":")[1].strip()
    except:
        print()
    return preference


def update_date(date):
    with open('./README.md', 'r') as file_handler:
        lines = file_handler.readlines()
    new_lines = lines
    for row, line in enumerate(lines):
        if line.lower().startswith("*updated:"):
            new_lines[row] = f"*updated: {date}*\n"
    with open('./README.md', 'w') as file_handler:
        file_handler.writelines(new_lines)


if __name__ == "__main__":
    issue_title = sys.argv[1]
    issue_url = sys.argv[2]
    issue_body = sys.argv[3]
    date = sys.argv[4]

    preference = get_preference(issue_body)

    update_list(issue_title, issue_url, preference)
    
    update_date(date)
