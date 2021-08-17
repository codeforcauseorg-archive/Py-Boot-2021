import pvporcupine
import pyaudio
import struct

keywords = ["alexa"]
sensitivities = [.9]

porcupine = pvporcupine.create(
    keywords=keywords,
    sensitivities=sensitivities,
    model_path=pvporcupine.MODEL_PATH,
    library_path=pvporcupine.LIBRARY_PATH
)

pa = pyaudio.PyAudio()

audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length,
    input_device_index=5
)

print("We are listening")

while True:
    data = audio_stream.read(porcupine.frame_length)
    data_tup = struct.unpack_from("h"*porcupine.frame_length, data)

    result = porcupine.process(data_tup)
    # print(result)

    if result >= 0:
        print("You just spoke", keywords[result])



# print(pvporcupine.KEYWORDS)
