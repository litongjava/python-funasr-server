from funasr import AutoModel
import os
model = AutoModel(model="paraformer-zh-streaming")
wav_file = os.path.join(model.model_path, "example/asr_example.wav")

print(wav_file)