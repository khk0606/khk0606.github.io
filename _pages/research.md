---
title: "Research"
permalink: /research/
author_profile: true
---

<section class="content-panel" markdown="1">

## Purpose- and History-Conditioned Reweighting of Affordance Maps
{: #affordance-reweighting }

<p class="research-status">Ongoing research · In preparation for submission · Human–scene interaction</p>

People often give instructions that do not name the target, such as "Sit on something to watch TV." This work selects where the interaction should take place from the 3D scene, the stated purpose, and the person's observed movement history.

- Built a teacher–student framework in which a LoRA-adapted affordance diffusion model (ADM) provides maps over **8,192 scene points and six joints**, and relation/history mixture-of-experts branches reweight them point-wise across a variable number of seat candidates.
- Constructed motion-derived proximity references by aligning seated motions to Unity scenes; implemented preprocessing, coordinate validation, and training/evaluation pipelines.
- Ran a pre-registered held-out comparison with a GT-only baseline (**34 scenes, 44 conditions**); diagnosed a nearest-seat bias caused by missing seat-orientation cues, and am now adding an auxiliary seat-orientation objective to address it.

<figure class="research-figure">
  <img src="{{ '/images/research/relafford-dual-weight-moe.png' | relative_url }}" alt="Teacher–student pipeline: a fixed ADM + LoRA affordance teacher, relation and history MoE weighting branches, and a downstream motion generation stage." width="1418" height="835">
  <figcaption>Teacher–student pipeline for purpose- and history-conditioned affordance reweighting. Motion generation (c) has not yet been evaluated.</figcaption>
</figure>

[Code](https://github.com/khk0606/ADM-MoE-Teacher)

</section>
