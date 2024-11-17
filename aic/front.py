from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter
import time

def typingEffect(text):
    for char in text:
        time.sleep(0.002)
        print(char, end='', flush=True)

def highlight_code(code, language):
    lexer = get_lexer_by_name(language)
    formatter = Terminal256Formatter(style="monokai")
    return highlight(code, lexer, formatter)
