import os
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from command import *

MODEL_PATH = "model"  # Путь к модели

if not os.path.exists(MODEL_PATH):
    exit(1)

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Параметры аудиопотока
SAMPLE_RATE = 16000
CHANNELS = 1
BLOCK_SIZE = 4096  # Размер блока данных для обработки

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    recognizer.AcceptWaveform(indata.tobytes())
    text = eval(recognizer.Result())["text"]
    if text:
        print(text)
        command_check(text)

try:
    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        callback=audio_callback,
        blocksize=BLOCK_SIZE,
        dtype='int16'
    ):
        while True:
            sd.sleep(1000)

except KeyboardInterrupt:
    print(" ")