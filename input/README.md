# Input Audio

This folder stores local reference audio used by the VoxCPM lab.

## Expected File

The current generation script reads:

```text
input/input.wav
```

Use a clean WAV file with the voice you want VoxCPM2 to reference. Short, clear speech samples with minimal background noise usually work best.

## Source Audio

You can keep source recordings here, such as `input.m4a`, but convert or export the final reference clip to `input.wav` before running the script.

## Privacy

Reference audio can contain personal voice data. The folder ignores local audio files by default, so keep private samples out of commits unless they are intentionally shared.
