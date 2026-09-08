---
title: "Research & Projects"
permalink: /research/
author_profile: true
---

I study how scene geometry, language, and interaction history can support human motion generation and embodied behavior. The work below includes ongoing research and implementation projects; it is not a list of peer-reviewed publications.

## Affordance-aware motion generation
{: #affordance-aware-motion-generation }

<p class="research-status">Ongoing research · Human–scene interaction</p>

I am developing a purpose- and history-conditioned affordance pipeline that combines a 3D scene, text, and past interactions. The research design holds an ADM + LoRA affordance teacher fixed during weighting-branch training. Separate relation and history MoE branches predict spatial weights, which reweight the base affordance before AMDM motion generation.

- Designed an affordance representation over **8,192 scene points and six body parts**.
- Implemented training and evaluation components for teacher adaptation, contact supervision, point alignment, and checkpoint auditing.
- Established strict multi-object evaluation gates and documented checkpoint limitations; end-to-end performance remains under evaluation.

<figure class="research-figure">
  <img src="{{ '/images/research/relafford-dual-weight-moe.png' | relative_url }}" alt="Fixed affordance teacher, separate relation and history MoE weighting branches, and AMDM motion generation." width="1418" height="835">
  <figcaption>Proposed research pipeline. This diagram describes the research design, not a claim that every component has been validated end to end.</figcaption>
</figure>

[Code and experiment documentation](https://github.com/khk0606/ADM-MoE-Teacher)

## Video2Unity: Transformer-based motion refinement
{: #video2unity }

<p class="research-status">AI & ML course project · Fall 2025 · Video-driven animation</p>

This project connects BlazePose 3D landmark extraction, a TensorFlow/Keras Transformer refinement model, and Unity character animation.

- Refined **33-joint poses from 30-frame sequences**.
- Applied root-centered normalization, denoising training, Savitzky-Golay smoothing, and floor alignment to address jitter and grounding artifacts.
- Integrated motion into a Unity dance performance with interpolation, scripted camera tracking, and lighting.

### Results from the course report

The following graphs are cropped from the original report. They illustrate example sequences rather than aggregate benchmark improvements; the repository documents implementation differences and data-split checks needed for reproducibility.

<figure class="research-figure">
  <img src="{{ '/images/research/video2unity/joint-stability.png' | relative_url }}" alt="Left-wrist Y-position comparison between raw baseline and refined output." width="1840" height="610" loading="lazy">
  <figcaption>Joint stability. The curves have different vertical offsets and should not be treated as absolute pose-error measurements.</figcaption>
</figure>

<figure class="research-figure">
  <img src="{{ '/images/research/video2unity/motion-smoothness.png' | relative_url }}" alt="Nose Y-velocity comparison showing raw fluctuations and a smoother refined curve." width="1840" height="604" loading="lazy">
  <figcaption>Motion smoothness in the displayed interval. This comparison does not isolate the Transformer from post-processing.</figcaption>
</figure>

<figure class="research-figure">
  <img src="{{ '/images/research/video2unity/foot-contact-stability.png' | relative_url }}" alt="Left-heel height before and after refinement relative to the zero-height reference." width="1760" height="580" loading="lazy">
  <figcaption>Heel-height alignment. Height alone does not establish physical contact accuracy or elimination of horizontal foot sliding.</figcaption>
</figure>

[Code, methods, and reproducibility notes](https://github.com/khk0606/Video2Unity-Transformer-Based-Motion-Refinement)

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
