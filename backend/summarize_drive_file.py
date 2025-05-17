import os
from drive_utils import list_files, download_file
import openai

# Set your OpenAI API key if not using a backend endpoint
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_file(file_id, file_name):
    local_path = f"/tmp/{file_name}"
    download_file(file_id, local_path)

    # Read file contents
    try:
        with open(local_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return f"❌ Failed to read file: {e}"

    # Summarize content
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Summarize this document for a smart assistant."},
                {"role": "user", "content": content[:4000]}  # Token-safe trim
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Failed to summarize file: {e}"

def run_summary_workflow(filename_match):
    files = list_files(limit=20)
    for f in files:
        if filename_match.lower() in f['name'].lower():
            print(f"✅ Found file: {f['name']}")
            summary = summarize_file(f['id'], f['name'])
            print(f"\n📄 Summary of {f['name']}:\n{summary}")
            return
    print("❌ No matching file found.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 summarize_drive_file.py 'filename keyword'")


    else:
        run_summary_workflow(sys.argv[1])
