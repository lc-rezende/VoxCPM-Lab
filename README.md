# VoxCPM Lab

Local lab project for experimenting with [VoxCPM2](https://huggingface.co/openbmb/VoxCPM2) text-to-speech generation and reference-audio voice cloning.

The current script loads a local VoxCPM2 checkpoint, uses `input/input.wav` as the reference voice sample, synthesizes a fixed demo sentence, and writes the generated audio to `output/demo.wav`.

## Requirements

- Python 3.12 or newer
- `uv`
- VoxCPM2 model weights downloaded locally
- A reference WAV file at `input/input.wav`

The current implementation is configured for Apple Silicon via `device="mps"` and enables `PYTORCH_ENABLE_MPS_FALLBACK=1`.

## Setup

Install the Python dependencies:

```bash
uv sync
```

Create a local environment file:

```bash
cp .env.example .env
```

Edit `.env` so `VOXCPM_PROJECT_ROOT` points to this repository:

```bash
VOXCPM_PROJECT_ROOT="/absolute/path/to/VoxCPM-Lab"
```

## Model Download

Download VoxCPM2 into the expected local path:

```bash
hf download openbmb/VoxCPM2 --local-dir ./models/pretrained_models/VoxCPM2
```

The script loads the model from:

```text
models/pretrained_models/VoxCPM2
```

Model files are large local artifacts and should not be committed.

## Input Audio

Place the reference voice sample at:

```text
input/input.wav
```

The repository may also contain source audio such as `input/input.m4a`, but the current script reads the WAV file.

## Run

Generate the demo audio:

```bash
uv run python -m lab_voxcpm.main
```

The generated file is written to:

```text
output/demo.wav
```

## Project Layout

```text
.
├── input/                  # Local reference audio
├── models/                 # Local model files
├── output/                 # Generated audio
├── src/lab_voxcpm/         # Python package source
├── pyproject.toml          # Project metadata and dependencies
└── uv.lock                 # Locked dependency graph
```

## Notes

- `local_files_only=True` is enabled, so the model must already exist under `models/pretrained_models/VoxCPM2`.
- The console script `lab-voxcpm` currently points to a placeholder package entrypoint; use `uv run python -m lab_voxcpm.main` for the TTS demo.
- Keep private voice samples and generated audio out of commits unless they are intentionally shared.
