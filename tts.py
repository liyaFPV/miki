import torch
import sounddevice as sd
import soundfile as sf
from lorder import *
config = get_config()
device = torch.device(config.get('device')) 


model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                   model='silero_tts',
                                   language='ru',
                                   speaker='v3_1_ru')
model.to(device)

def say(text):
    audio = model.apply_tts(text,
                           speaker=config.get('speaker'),
                           sample_rate=48000)
    sd.play(audio, 48000)
    sd.wait()
    
def wav(text):
    audio = model.apply_tts(text,
                           speaker=config.get('speaker'),
                           sample_rate=48000)
    sf.write("audio.wav", audio, 48000)

def wavp(file_path):
    try:
        audio, sample_rate = sf.read(file_path)
        sd.play(audio, sample_rate)
        sd.wait()
    except Exception as e:
        print(f"Ошибка при воспроизведении файла {file_path}: {e}")