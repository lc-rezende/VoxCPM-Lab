# Models

This folder stores local model assets for the VoxCPM lab.

Model files are large runtime artifacts and are ignored by Git. Keep downloaded checkpoints under `models/pretrained_models/`.

## VoxCPM2

Download the VoxCPM2 checkpoint from the repository root:

```bash
hf download openbmb/VoxCPM2 --local-dir ./models/pretrained_models/VoxCPM2
```

After download, the expected model directory is:

```text
models/pretrained_models/VoxCPM2
```

See `models/pretrained_models/README.md` for more details.
