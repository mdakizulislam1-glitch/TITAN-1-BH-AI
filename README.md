# TITAN-1 — Scientific Image Restoration Engine
🚀 **Live Demo:** https://mdakizulislam1-titan-1-scientific-image-restoration.hf.space
🤗 **Hugging Face Space:** https://huggingface.co/spaces/mdakizulislam1/TITAN-1-Scientific-Image-Restoration

### A lightweight, reproducible framework for controlled scientific image restoration and out-of-distribution evaluation.
**Researcher:** Md. Akizul Islam
**Email:** mdakizulislam1@gmail.com
**Role:** Independent Researcher & Programmer
**Location:** Khulna, Bangladesh
**Contact:** mdakizulislam1@gmail.com | GitHub: mdakizulislam1-glitch
---

## Overview

TITAN-1 is a lightweight AI-based scientific image-restoration
prototype developed to study image denoising and restoration under
controlled synthetic scientific-image benchmarks.

The current research focuses on reproducible computational experiments
using synthetic black-hole-like ring structures, controlled noise,
morphology shifts, blur/PSF effects, and resolution changes.

The project is designed as a foundation for future scientific imaging
software and AI-for-Science workflows.

TITAN-1 is currently a research and software-development project.
Real-world scientific deployment and institutional validation have not
yet been established.

---

## Scientific Problem

A general image-restoration problem can be represented as:

`y = H(x) + n`

where:

- `x` = underlying clean image
- `H` = degradation or instrument-response operator
- `n` = noise
- `y` = observed/degraded image

TITAN-1 currently studies this problem in controlled computational
settings.

The objective is to investigate whether a lightweight neural
restoration architecture can recover useful image structure under
controlled degradation and distribution shifts while maintaining
reproducible computational behavior.

---

# Current Evidence Scope

The documented benchmark framework includes:

- 5,000 synthetic training images
- 700 unseen elliptical out-of-distribution test images
- 64 × 64 grayscale images
- Controlled Gaussian-noise conditions
- Additional controlled noise families
- Controlled PSF/blur experiments
- Resolution-shift experiments
- Morphology-shift evaluation
- Quantitative MSE, PSNR, and SSIM evaluation
- Reproducibility and provenance requirements
- Automated software regression testing

### Evidence qualification

The benchmark design and historical results are documented in the
project records.

Some scientific artifacts required for complete independent
recalculation — including the validated checkpoint binary, exact
dataset artifacts, and complete raw per-image metric arrays — are not
currently included in the public software repository.

Therefore, documented historical results are not presented as newly
recalculated independent statistical results unless the underlying
artifacts are available and verified.

---

# TITAN-1 Model

The historical canonical TITAN-1 scientific benchmark architecture
uses:

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
- Historical seed: `42`
- 14,337 trainable parameters

The historical scientific benchmark operates on:

`64 × 64` grayscale inputs.

### Parameter count

The documented architecture contains:

`14,337 trainable parameters`

This architecture description refers specifically to the historical
scientific benchmark model.

The production software framework should not be assumed to contain the
same validated checkpoint or to be identical to the historical
scientific benchmark model unless the corresponding checkpoint and
architecture artifacts are independently verified.

---

# Quantitative Evidence

A documented historical evaluation of the unseen elliptical benchmark
reported:

- **MSE:** `0.00092568 ± 0.00083884`
- **PSNR:** `32.1562 ± 4.2082 dB`
- **SSIM:** `0.9104 ± 0.0948`

These values are reported historical benchmark results.

The underlying per-image metric arrays are not currently included in
the released scientific evidence bundle. Therefore, these values should
not be interpreted as a newly recalculated independent statistical
analysis.

A separate P5.2 reproduction was performed under the documented
scientific specification. Its reported results are maintained as a
separate reproduction record and are not merged with the historical
results.

---

# Baseline Comparison

A controlled noisy-input baseline has been documented in the historical
benchmark records.

The historical evaluation reported substantial improvement in MSE,
PSNR, and SSIM relative to the corresponding degraded input under the
specified benchmark conditions.

A fixed Non-Local Means (NLM) baseline has also been defined as part of
the comparison protocol.

### NLM evidence status

Complete quantitative NLM evidence is not currently established in the
released scientific evidence bundle.

Therefore, TITAN-1 is **not** claimed to be universally superior to NLM
or to any other denoising algorithm.

Future baseline analysis should use:

- identical evaluation images
- identical preprocessing
- identical output conventions
- identical metric implementations
- paired per-image results
- documented statistical tests
- documented software/configuration versions

---

# Robustness Studies

The research protocol includes controlled evaluation under several
distribution shifts and degradation families.

## Noise

The planned/documented robustness families include:

- Gaussian noise
- Salt-and-pepper noise
- Poisson noise
- Speckle noise

## PSF / Blur

Controlled Gaussian PSF experiments are included in the research
protocol to examine restoration behavior under synthetic blur and noise.

## Resolution

Resolution-shift experiments are included to examine performance when
evaluation conditions differ from the nominal training configuration.

## Morphology

Elliptical ring structures are used as an unseen morphology distribution
relative to the circular training distribution.

### Robustness evidence status

The stress-test families and experimental protocol are documented.

Complete condition-by-condition quantitative results, severity-wise
tables, confidence intervals, and worst-case failure analysis are not
currently presented as fully established public evidence.

---

# Statistical Methodology

Publication-grade future analyses are intended to preserve:

- Per-image MSE values
- Per-image PSNR values
- Per-image SSIM values
- Paired differences
- Sample counts
- Exact statistical test definitions
- Alternative hypotheses
- Significance threshold
- Effect-size definitions
- Confidence intervals
- Multiple-comparison treatment
- Pre-specified exclusion rules

No sample should be selectively removed after observing an outcome
without a documented and pre-specified exclusion rule.

Historical statistical results are retained as historical records and
should not be interpreted as independently recalculated statistics
unless the underlying per-image data are available.

---

# Failure Analysis

Future complete scientific validation should include systematic
failure analysis covering:

- High-MSE examples
- Low-SSIM examples
- Severe-noise failures
- Morphology-shift failures
- Blur/PSF failures
- Resolution-shift failures
- Structural distortions
- Intensity bias
- Hallucination-like structures
- Error maps
- Worst-case examples

The objective is not only to demonstrate average performance but also
to identify conditions under which restoration quality degrades.

---

# Software & Reproducibility

The project includes a product-oriented software foundation with:

- Input validation
- Deterministic inference infrastructure
- Quality-control checks
- Metadata generation
- CLI workflow
- Python inference interface
- REST API infrastructure
- Automated regression tests
- Configuration auditing
- Artifact integrity checks
- SHA-256 provenance tracking
- Runtime diagnostics
- Logging and audit infrastructure

The software release has undergone structured internal forensic and
reproducibility audits.

Software-engineering verification is kept separate from scientific
benchmark validation.

A passing software test suite does not by itself establish scientific
validity.

---

# Scientific Reproducibility

TITAN-1 follows an evidence-controlled reproducibility workflow:

`Specification → Artifact Verification → Execution → Measurement → Statistical Analysis → Evidence Freeze`

A complete scientific reproduction requires, at minimum:

- Exact release identity
- Source-code integrity
- Python/runtime environment
- Dependency versions
- Model checkpoint
- Checkpoint SHA-256
- Dataset identity
- Dataset provenance
- Preprocessing configuration
- Random seeds
- Determinism settings
- Hardware information
- Inference configuration
- Metric implementation
- Baseline configuration
- Per-image results
- Statistical analysis outputs

---

# Scientific Artifact Status

The current public software repository contains the software,
documentation, manifests, and reproducibility infrastructure.

The following scientific artifacts are not currently established as
complete public artifacts:

- Validated historical checkpoint binary
- Exact historical dataset archive
- Exact dataset generator implementation
- Complete raw per-image metric arrays
- Complete NLM raw results
- Complete robustness raw-results package
- Complete architecture-ablation raw-results package

This is an evidence-completeness limitation, not a claim that historical
artifacts never existed.

---

# Real EHT Data — Current Status

Official Event Horizon Telescope M87 visibility data has been examined
as a research-data foundation.

The work includes:

- Source-data integrity verification
- UV visibility extraction
- Fourier-domain analysis
- Direct Fourier dirty-image reconstruction
- Reconstruction consistency checks

## Important limitation

**Quantitative TITAN-1 inference or validation on real EHT observations
has not yet been established.**

The current real-data work therefore should not be described as:

- Real EHT denoising validation
- An official EHT reconstruction engine
- Black-hole parameter inference
- Astrophysical discovery
- Institutional validation

The real-data work currently serves as a research foundation for future
instrument-aware and observational validation studies.

---

# What TITAN-1 Is Not

TITAN-1 is currently **not**:

- An official Event Horizon Telescope pipeline
- A NASA-validated system
- An ESA-validated system
- A CERN-validated system
- A production telescope pipeline
- A clinically validated system
- A commercially validated scientific deployment
- A black-hole parameter inference system
- A new-physics model
- A universally superior denoising method

These capabilities would require additional experiments, independent
validation, and appropriate institutional or domain-specific review.

---

# Research Collaboration

TITAN-1 is available for discussion as an independent research and
software project.

Potential collaboration modes include:

1. Independent technical evaluation
2. Scientific imaging pilot studies
3. Dataset-specific restoration experiments
4. Algorithm comparison
5. GPU/HPC evaluation
6. Instrument-aware simulation
7. Reproducibility studies
8. Scientific-user evaluation
9. Joint research development
10. Research-software integration

Potential application domains include:

- Scientific imaging
- Astronomy and space data
- Detector and experimental imaging
- Computational imaging
- AI for Science
- Scientific image-processing workflows

No institutional validation or partnership is claimed unless formally
established and independently documented.

---

# Research Direction

The long-term objective is to develop TITAN-1 toward a broader
scientific image-restoration and AI-for-Science software platform.

Potential future directions include:

1. Recovery and verification of historical scientific artifacts
2. Complete independent reproducibility
3. GPU/CUDA acceleration
4. Larger scientific datasets
5. Instrument-specific degradation models
6. Real observational-data validation
7. Additional learned and classical baselines
8. Complete robustness analysis
9. Uncertainty quantification
10. External scientific-user evaluation
11. Independent institutional replication
12. Scalable scientific software and API workflows

Future capabilities will only be claimed after corresponding
experiments and validation are completed.

---

# Computational Performance

A CPU reference benchmark has been documented for the software
inference workflow.

The historical CPU measurement record includes repeated inference
timings and throughput measurements.

GPU/CUDA execution has not yet been independently performed in the
current validated evidence record.

Therefore:

- No GPU speedup claim is made.
- No CUDA performance claim is made.
- No HPC performance claim is made.

GPU benchmarking remains a future technical milestone.

---

# Technology Stack

Core technologies include:

- Python
- PyTorch
- NumPy
- SciPy
- Pandas
- Matplotlib
- Astropy
- Git
- GitHub
- Google Colab

---

# Reproducibility Philosophy

TITAN-1 follows an evidence-first computational research philosophy:

**Build → Verify → Measure → Record Evidence → Freeze → Extend**

The project separates:

- Historical results
- Independent reproductions
- Verified software behavior
- Supported evidence
- Missing evidence
- Future research

Experimental claims are limited to their documented benchmark
conditions and available evidence.

---

# Project Status

| Component | Status |
|---|---|
| Historical scientific architecture | Documented |
| Historical synthetic benchmark protocol | Established |
| Historical benchmark results | Documented |
| P5.2 independent reproduction | Established |
| Software foundation | Complete |
| Reproducibility infrastructure | Established |
| Scientific artifact completeness | Not yet complete |
| NLM complete quantitative evidence | Not established |
| Complete robustness evidence | Not established |
| Complete raw statistical package | Not established |
| GPU/CUDA execution | Not yet established |
| Real EHT data foundation | Established |
| Real EHT TITAN-1 validation | Not established |
| External institutional replication | Not established |
| Production scientific validation | Not established |
| Commercial scientific validation | Not established |

---

# Researcher

**Md. Akizul Islam**  
Independent Researcher & Programmer  
Bangladesh

### Research Interests

- Scientific Computing
- AI for Science
- Scientific Image Processing
- Astronomy & Space Data
- Machine Learning
- Research Software Engineering
- Reproducible Computational Research

---

# Repository

This repository contains the ongoing TITAN-1 research and computational
development work.

For reproducibility and scientific integrity, experimental results
should always be interpreted within their stated benchmark conditions,
provenance, and limitations.

---

# External Collaboration

For research or technical collaboration, please refer to the project's
public documentation and repository materials.

Potential collaborators are encouraged to request or independently
evaluate the underlying evidence before drawing conclusions about
scientific or real-world performance.

---

# License

Research and software licensing information will be specified as the
project matures.

Until an explicit license is published, users should not assume that
the repository contents are available for unrestricted commercial
reuse.

---

## Evidence Policy

TITAN-1 follows a simple rule:

> **No evidence, no claim.**

Documented historical results remain identified as historical results.
New scientific claims require corresponding reproducible evidence.

---

**TITAN-1 — Scientific Image Restoration Engine**  
**Independent Research & Software Project**  
**Md. Akizul Islam**
