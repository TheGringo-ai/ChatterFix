import os

def write_code_to_file(file_path: str, content: str, comment_tag: str = "# === AI GENERATED CODE ==="):
    tagged_content = f"{comment_tag}\n{content}"
    with open(file_path, "w") as f:
        f.write(tagged_content)