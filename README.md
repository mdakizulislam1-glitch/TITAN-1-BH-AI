# TITAN-1 — Scientific Image Restoration Engine

### A Controlled PyTorch CNN Benchmark for Image Denoising, Baseline Comparison, and Robustness Evaluation

**Researcher:** Md. Akizul Islam  
**Role:** Independent Researcher & Programmer  
**Location:** Bangladesh

---

## Overview

TITAN-1 is a lightweight AI-based scientific image restoration prototype developed to study image denoising under controlled synthetic scientific-image benchmarks.

The current research focuses on reproducible computational experiments using synthetic black-hole-like ring structures, controlled noise, morphology shifts, blur/PSF effects, and resolution changes.

The project is designed as a foundation for future scientific imaging software and AI-for-Science workflows.

---

## Scientific Problem

A general image-restoration problem can be represented as:

`y = H(x) + n`

where:

- `x` = underlying clean image
- `H` = degradation or instrument-response operator
- `n` = noise
- `y` = observed/degraded image

TITAN-1 currently studies this problem in controlled computational settings.

---

## Current Validated Scope

The benchmark framework includes:

- 5,000 synthetic training images
- 700 unseen elliptical out-of-distribution test images
- 64 × 64 grayscale images
- Controlled Gaussian-noise conditions
- Multiple additional noise families
- Controlled PSF/blur experiments
- Resolution-shift experiments
- Morphology-shift evaluation
- Fixed Non-Local Means (NLM) baseline comparison
- Quantitative MSE, PSNR, and SSIM evaluation
- Reproducibility and provenance checks
- Automated software regression testing

---

## TITAN-1 Model

The canonical TITAN-1 CNN uses:

`1 → 32 → 32 → 16 → 1`

with:

- 3 × 3 convolutional layers
- ReLU activations
- Final Sigmoid activation
- MSE loss
- Adam optimizer
- Learning rate: `0.001`
- Batch size: `32`
- 30 training epochs
- 14,337 trainable parameters

The model operates on 64 × 64 grayscale inputs.

---

## Quantitative Evidence

On the independently evaluated unseen elliptical benchmark, the canonical TITAN-1 model achieved:

- **MSE:** 0.00092568 ± 0.00083884
- **PSNR:** 32.1562 ± 4.2082 dB
- **SSIM:** 0.9104 ± 0.0948

The benchmark also includes controlled robustness experiments covering multiple noise families, PSF/blur conditions, resolution changes, and morphology shifts.

These results describe performance on the controlled benchmark and should not be interpreted as validation on real astronomical observations.

---

## Robustness Studies

TITAN-1 has been evaluated under several controlled distribution shifts.

### Noise

The benchmark includes multiple noise families, including:

- Gaussian noise
- Salt-and-pepper noise
- Poisson noise
- Speckle noise

### PSF / Blur

Controlled Gaussian PSF experiments were used to examine restoration performance under synthetic blur and noise.

### Resolution

Resolution-shift experiments examined performance under multiple controlled resolution conditions.

### Morphology

Elliptical ring structures were used as an unseen morphology distribution relative to the circular training distribution.

---

## Baseline Comparison

A fixed Non-Local Means (NLM) baseline was evaluated under the controlled resolution + PSF + noise benchmark.

TITAN-1 produced lower MSE than the fixed NLM baseline across the evaluated conditions.

This does **not** establish universal superiority over all denoising algorithms.

---

## Software & Reproducibility

The project includes a product-oriented software foundation with:

- Input validation
- Deterministic inference
- Quality-control checks
- Metadata generation
- CLI workflow
- Python inference interface
- Automated regression tests
- Configuration auditing
- Artifact integrity checks
- SHA-256 provenance tracking

The product foundation and regression suite have been independently audited.

---

## Real EHT Data — Current Status

Official Event Horizon Telescope M87 visibility data has been examined as a research-data foundation.

The work includes:

- Source-data integrity verification
- UV visibility extraction
- Fourier-domain analysis
- Direct Fourier dirty-image reconstruction
- Reconstruction consistency checks

### Important limitation

**Quantitative TITAN-1 inference/validation on real EHT observations has not yet been established.**

The current real-data work therefore should not be described as:

- real EHT denoising validation
- an EHT reconstruction engine
- black-hole parameter inference
- astrophysical discovery
- institutional validation

---

## What TITAN-1 Is Not

TITAN-1 is currently **not**:

- An official Event Horizon Telescope pipeline
- A NASA-validated system
- An ESA-validated system
- A CERN-validated system
- A production telescope pipeline
- A clinically or commercially validated product
- A black-hole parameter inference system
- A new-physics model
- A universally superior denoising method

These are future possibilities requiring additional evidence and validation.

---

## Research Direction

The long-term objective is to develop TITAN-1 toward a broader scientific image-restoration and AI-for-Science software platform.

Potential future directions include:

1. Independent reproducibility
2. GPU acceleration
3. Larger scientific datasets
4. Instrument-specific degradation models
5. Real observational data validation
6. Additional learned and classical baselines
7. External scientific-user evaluation
8. Scalable scientific software and API workflows

Future capabilities will only be claimed after corresponding experiments and validation are completed.

---

## Technology Stack

- Python
- PyTorch
- NumPy
- SciPy
- Pandas
- Matplotlib
- Astropy
- Google Colab
- Git / GitHub

---

## Reproducibility Philosophy

TITAN-1 follows a controlled computational research approach:

**Build → Verify → Record Evidence → Freeze → Extend**

Experimental claims are separated from future goals, and benchmark results are accompanied by reproducibility and provenance requirements whenever possible.

---

## Project Status

**Synthetic benchmark:** Validated  
**Software foundation:** Complete  
**Reproducibility foundation:** Established  
**Real EHT data foundation:** Established  
**Real EHT TITAN-1 validation:** Not yet established  
**Production validation:** Not established  
**Commercial validation:** Not established

---

## Researcher

**Md. Akizul Islam**  
Independent Researcher & Programmer  
Bangladesh

Research interests:

- Scientific Computing
- AI for Science
- Scientific Image Processing
- Astronomy & Space Data
- Machine Learning
- Research Software Engineering

---

## Repository

This repository contains the ongoing TITAN-1 research and computational development work.

For reproducibility and scientific integrity, experimental results should always be interpreted within their stated benchmark conditions and limitations.

---

## License

Research and software licensing information will be specified as the project matures.
