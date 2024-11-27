import os
import json
import google.generativeai as genai
import aic.prompt as Prompt
import aic.front as Front
from rich.console import Console
from rich.table import Table

API_KEY = "GEMINI_API_KEY"

console = Console()

def no_api_key_message():
    print("\u2800")
    console.print(f"⚠ ERRO: {API_KEY} not set", style="bold red")
    console.print(f"You need to set the {API_KEY} environment variable. \n")

    console.print("You can get your gemini API key from: https://aistudio.google.com/app/apikey \n")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Platform")
    table.add_column("Instructions")

    table.add_row("Linux", "export GEMINI_API_KEY=<your-api-key>")
    table.add_row("Windows", "setx GEMINI_API_KEY <your-api-key>")

    console.print(table)

    exit()

def use():
    GEMINI_API_KEY = os.environ.get(API_KEY)
    response = None

    if GEMINI_API_KEY is None:
        no_api_key_message()

    genai.configure(api_key=GEMINI_API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")

    console.print("★ AIC (type exit to finish)", style="bold green")
    Question = input("Type something: ")

    if Question == "exit":
        exit()

    try:
        response = model.generate_content(Prompt.text(Question))
    except Exception as e:
        console.print(f"⚠ ERROR: {e}", style="bold red")
        exit()

    json_response = json.loads(response.text.replace("```json", "").replace("```", ""))

    print("——————————————")

    for item in json_response["response"]:
        if item["type"] == "text" and item["content"] != "":
            Front.typing_effect(item["content"])
            print("\u2800")
            print("\u2800")
        elif item["type"] == "code":
            Front.typing_effect(Front.highlight_code(item["content"], item["language"]))
            print("\u2800")
