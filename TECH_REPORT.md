TITAN-1: Lightweight Scientific Image Restoration

Author: Md. Akizul Islam
Location: Bangladesh
Report status: Engineering evidence report — in progress

Scope

TITAN-1 is a lightweight image-restoration model and software engineering project. This report distinguishes verified software checks from scientific validation and deployment claims.

Model Configuration

- Input: single-channel 64 × 64 images
- Architecture: Conv 1 → 32 → 32 → 16 → 1
- Activation: ReLU between convolution layers; Sigmoid output
- Parameter count: 14,337
- Checkpoint: C0.1 controlled reconstruction

Verified Evidence

- Checkpoint and manifest integrity were checked in the recorded M1.1 audit.
- Strict checkpoint loading and architecture parameter count were checked in M1.4.
- CPU inference shape, finite output, and range were checked in M1.5.
- Reusable model loading was checked in M1.6.
- Five automated regression tests passed in M1.7 (5 passed in 2.91 seconds, according to the recorded output).
- Input validation checks passed in M1.8 for valid input, wrong shape, NaN values, out-of-range values, integer tensors, and non-tensor input.

These results establish only the scope of the tests listed above.

Pending Evidence and Limitations

- Independent reproduction from a clean environment: pending.
- Reproduction of all historical benchmark results: not established.
- Controlled PSNR/SSIM evaluation: must be recorded with its dataset, degradation procedure, baseline, and exact checkpoint.
- Real NASA image restoration quality against clean ground truth: not established.
- Docker build and container execution: not established.
- External institutional review, customer validation, and NASA endorsement: not established.
- Production deployment and commercial readiness: not established.

Reproduction

From the project workspace, run:

bash reproduce.sh

The script runs the existing automated regression tests. It does not claim to reproduce every scientific benchmark or validate NASA data.
