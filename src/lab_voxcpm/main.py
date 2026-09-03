import datetime as dt
import os
import warnings

import soundfile as sf
from dotenv import load_dotenv
from voxcpm import VoxCPM

warnings.filterwarnings("ignore")

load_dotenv()

project_root = os.getenv("VOXCPM_PROJECT_ROOT")
pretrained_model = f"{project_root}/models/pretrained_models/VoxCPM2"

def _log_now():
    _now =  dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M:%S")
    return _now

print(f"\n{_log_now()} | Loading model...")
model = VoxCPM.from_pretrained(
    pretrained_model,
    load_denoiser=False,
    local_files_only=True
)
print(f"{_log_now()} | ✅ Model loaded")

print(f"\n{_log_now()} | Generating audio...")
wav = model.generate(
    text="VoxCPM2 is the current recommended release for realistic multilingual speech synthesis.",
    cfg_value=2.0,
    inference_timesteps=10
)
print(f"{_log_now()} | ✅ Audio generated")

print(f"\n{_log_now()} | Saving audio...")
output_audio = f"{project_root}/output/demo.wav"
sf.write(output_audio, wav, model.tts_model.sample_rate)
print(f"{_log_now()} | ✅ Audio saved at: {output_audio}")
