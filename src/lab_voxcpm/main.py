import os
import soundfile as sf
from dotenv import load_dotenv
from voxcpm import VoxCPM

load_dotenv()
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

project_root = os.getenv("VOXCPM_PROJECT_ROOT")
pretrained_model = f"{project_root}/models/pretrained_models/VoxCPM2"

model = VoxCPM.from_pretrained(
    pretrained_model,
    load_denoiser=False,
    device="mps",
    optimize=False,
    local_files_only=True
)

text = "This is just a VoxCPM lab project. Its main purpose is to test this package."

wav = model.generate(
    reference_wav_path=f"{project_root}/input/input.wav",
    text=text,
    cfg_value=2.5,
    inference_timesteps=15
)

output_audio = f"{project_root}/output/demo.wav"
sf.write(output_audio, wav, model.tts_model.sample_rate)
print(f"\nSample rate: {model.tts_model.sample_rate}")
