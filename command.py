from thefuzz import fuzz
from thefuzz import process
import os
from lorder import *
from tts import *

def run(type, runs):
    if type == "run":
        exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), runs)
        os.startfile(exe_path)
    elif type == "say":
        say(runs)
    elif type == "wavp":
        wavp(runs)

def command_check(text):
    commands = load_commands()
    for cmd in commands:
        print(cmd['run'])
        val = fuzz.ratio(text, cmd['text'])
        if val >= 60:
            run(cmd['type'], cmd['run'])
            
            return