import os
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    # Read md file and store contents
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    # Read template file and store contents
    template_path = open(template_path, "r")
    template = template_path.read()
    template_path.close()

    # Convert md file to HTML string
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Grab  title from md file    
    title = extract_title(markdown_content)
    # Replace placeholders with HTML and title generated
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Write the new full HTML page
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        # Create directories if they do not exists
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")