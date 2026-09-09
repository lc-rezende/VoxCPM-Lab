# Pretrained Models

This folder contains pretrained model checkpoints used by the VoxCPM lab.

## VoxCPM2

Download VoxCPM2 from the repository root:

```bash
hf download openbmb/VoxCPM2 --local-dir ./models/pretrained_models/VoxCPM2
```

Or, from inside this folder:

```bash
hf download openbmb/VoxCPM2 --local-dir ./VoxCPM2
```

The generation script expects this path:

```text
models/pretrained_models/VoxCPM2
```

## Verify

After downloading, the model directory should include files such as:

```text
config.json
model.safetensors
audiovae.pth
tokenizer.json
```

The downloaded `VoxCPM2/README.md` is the upstream model card from Hugging Face and should be left intact.

## Git

Pretrained model files are local artifacts and should not be committed.
