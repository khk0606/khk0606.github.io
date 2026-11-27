---
title: "Research"
permalink: /research/
author_profile: true
---

<section class="content-panel" markdown="1">

## Intended-Seat Affordance Maps by Adapting a Pretrained Affordance Diffusion Model
{: #intended-seat-affordance }

<p class="research-authors"><strong>Hyunkyu Kang</strong>, Taeil Jin</p>
<p class="research-status">Journal manuscript in preparation · Human–scene interaction</p>

In games and XR, users often state a purpose rather than an object, as in "Sit on something to watch TV," while the system observes how they move. This work predicts the affordance map of the seat the user intends to use from a 3D scene, an instruction that does not name the target, and a short movement history.

<figure class="research-figure">
  <img src="{{ '/images/research/intended-seat-architecture.jpg' | relative_url }}" alt="Architecture: an affordance teacher (ADM adapted with LoRA) on top and an intent adapter with relationship and history mixture-of-experts branches on the bottom; the final map is the product of the teacher map and the adapter weights." width="2400" height="1072">
  <figcaption>Affordance teacher (top) and intent adapter (bottom). The final map is the pointwise product of the teacher map and the adapter weights.</figcaption>
</figure>

- **Affordance teacher.** The pretrained Affordance Diffusion Model (ADM), adapted with LoRA to mark every sittable object for a generic sitting instruction.
- **Intent adapter.** A mixture-of-experts network with relationship and history branches that predicts a weight for every scene point and body joint from the scene, the instruction, and an eight-frame movement history.
- **Data.** A game-engine procedure that aligns existing sitting motions to every seat of rule-generated layouts and pairs them with instructions that state only an action or a purpose.
- **Evaluation.** On 40 new layouts with target seats annotated before inference, the adapter has the highest seat-selection accuracy among the compared models, although the margins are not statistically significant. Its maps also agree with motion-derived references better than those of the same network trained without the teacher.

</section>
