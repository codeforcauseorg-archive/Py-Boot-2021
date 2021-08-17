import pvporcupine
import pyaudio
import struct
import pvrhino

keywords = ["alexa"]
sensitivities = [.9]

porcupine = pvporcupine.create(
    keywords=keywords,
    sensitivities=sensitivities,
    model_path=pvporcupine.MODEL_PATH,
    library_path=pvporcupine.LIBRARY_PATH
)

rhino = pvrhino.create(
    model_path=pvrhino.MODEL_PATH,
    library_path=pvrhino.LIBRARY_PATH,
    context_path="./light.rhn"
)

pa = pyaudio.PyAudio()

audio_stream = pa.open(
    rate=rhino.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=rhino.frame_length,
    input_device_index=5
)

print("We are listening")

while True:
    data = audio_stream.read(rhino.frame_length)
    data_tup = struct.unpack_from("h"*rhino.frame_length, data)

    is_finalized = rhino.process(data_tup)

    if is_finalized:
        inference = rhino.get_inference()
        if inference.is_understood:
            print('{')
            print("  intent : '%s'" % inference.intent)
            print('  slots : {')
            for slot, value in inference.slots.items():
                print("    %s : '%s'" % (slot, value))
            print('  }')
            print('}\n')
        else:
            print("Didn't understand the command.\n")
    # print(result)
    #
    # if result >= 0:
    #     print("You just spoke", keywords[result])



# print(pvporcupine.KEYWORDS)
