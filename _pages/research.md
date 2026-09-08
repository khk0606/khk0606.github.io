---
title: "Research & Projects"
permalink: /research/
author_profile: true
---

I study how scene geometry, language, and interaction history can support human motion generation and embodied behavior. The work below includes ongoing research and implementation projects; it is not a list of peer-reviewed publications.

## Affordance-aware motion generation
{: #affordance-aware-motion-generation }

<p class="research-status">Ongoing research · Human–scene interaction</p>

I am developing a purpose- and history-conditioned affordance pipeline that combines a 3D scene, text, and past interactions. The research design uses a frozen teacher with LoRA adaptation and a mixture-of-experts student to model spatial and temporal context.

- Designed an affordance representation over **8,192 scene points and six body parts**.
- Implemented training and evaluation components for teacher adaptation, contact supervision, point alignment, and checkpoint auditing.
- Maintained reproducible experiment setup and documented validation gates. The current Teacher-v10.2 candidate **has not passed the strict all-three-object evaluation gate**; end-to-end improvements remain under evaluation.

<figure class="research-figure">
  <img src="{{ '/images/research/affordance-pipeline.png' | relative_url }}" alt="Research architecture combining a frozen teacher, a purpose-scene-history MoE student, and a frozen motion generator." width="1774" height="887">
  <figcaption>Proposed research pipeline. This diagram describes the research design, not a claim that every component has been validated end to end.</figcaption>
</figure>

[Code and experiment documentation](https://github.com/khk0606/ADM-MoE-Teacher)

## Temporal diagnostics for interaction representations

<p class="research-status">Experimental analysis · 200 motion sequences</p>

I analyzed what temporal information is lost when an interaction representation is pooled over time. For each sequence, I compared the original motion with its time-reversed version.

- Max-pooled interaction intensity weights (IIW) were identical under reversal for all **200 analyzed sequences**.
- Time-resolved IIW curves retained order-dependent differences, with a median mean absolute difference of **0.323**.
- This is a diagnostic study of a proxy representation, not an evaluation of the complete Afford-Motion system. Temporal compression did not consistently outperform the static baseline in the accompanying order-classification experiment.

<figure class="research-figure">
  <img src="{{ '/images/research/temporal-diagnostics.png' | relative_url }}" alt="Histograms: static max-pooled IIW differences are zero for 200 sequences, while temporal IIW differences are nonzero." width="1800" height="720">
  <figcaption>Original versus reversed motion: max pooling removes order information, while time-resolved curves can preserve it.</figcaption>
</figure>

## Motion data processing and validation

<p class="research-status">Research infrastructure · YBot / HumanML263</p>

I built and validated a motion-data pipeline for affordance-conditioned sitting motions, converting Unity/YBot motion into HumanML263 and preserving natural approach trajectories.

- Constructed a validated **162-sequence** dataset with source-disjoint train/validation/test splits of **136 / 13 / 13**.
- Checked consistency across motion arrays, text, sample IDs, affordance metadata, and splits.
- Verified zero source-split leakage and a maximum reconstructed endpoint error of **2.27 × 10⁻⁷ m** in the natural-trajectory dataset.
- Rejected synthetic trajectory warps after visual and numerical checks exposed unrealistic movement.

## Video-to-robot motion transfer
{: #video-to-robot-motion-transfer }

<p class="research-status">Simulation prototype · Quadruped control</p>

This project connects reference-video analysis to a structured MotionSpec, generated reward functions, and Dial-MPC control for a Unitree Go2 model in MuJoCo/MJX.

- Integrated language-model-based motion interpretation with JAX reward definitions and model-predictive control.
- Worked on startup holds, velocity ramps, warm starts, and joint-limit safeguards to improve the control workflow.
- The project is simulation-focused; it does not establish physical-robot deployment or general zero-shot transfer performance.

[Code](https://github.com/khk0606/Zero-Shot-Video-to-Robot-Motion-Transfer)

## Korean text robustness
{: #korean-text-robustness }

<p class="research-status">Evaluation project · NLP robustness</p>

I evaluated Korean hate-speech classification under text obfuscation using a balanced **500-comment K-MHaS subset**, with five variants per comment and **2,500 predictions per system**.

- Compared character-based models, KoELECTRA, and Qwen-based pipelines with normalization and calibration.
- The normalization + character TF-IDF MLP achieved **0.772 worst-condition balanced accuracy** on this benchmark.
- Examined false-negative and false-positive trade-offs across perturbation levels. These results are specific to the evaluated subset and do not imply universal model superiority.

[Code and benchmark results](https://github.com/khk0606/Korean-Hate-Speech-Robustness-under-Text-Obfuscation)
