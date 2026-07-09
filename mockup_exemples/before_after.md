# Improving Product Mockup Generation

This section documents the evolution of the prompt engineering process used to generate realistic product mockups from a single original product image.

The primary objective was to preserve the product's identity while generating high-quality lifestyle and marketing imagery suitable for e-commerce applications.

## Original Product

| Product | 
|----------|
| ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/original_product_image/bottle1_d4uqko.jpg)
---

# Iteration 1 — Initial System Prompt

## Objective

The first version of the system prompt focused on generating diverse product photography concepts while preserving the product's visual identity.

The model was instructed to:

- Preserve the product's shape, color, branding, and proportions
- Generate three different photographic compositions
- Follow a selected visual style (Cinematic, Editorial, or Fashion)
- Produce photorealistic, high-resolution imagery

Although these constraints significantly improved consistency compared to an unconstrained prompt, several recurring issues remained.

---

## Observed Limitations

The generated prompts occasionally resulted in images with unrealistic physical behavior, including:

- Products floating in mid-air without visible support
- Objects partially intersecting with surrounding props
- Unrealistic positioning that ignored gravity
- Slight reinterpretations of product materials
- Inconsistent preservation of product geometry
- Reduced branding readability in some scenes

These artifacts reduced the realism of the generated marketing images.

---

## Example Output

| Mockup 1 | Mockup 2 | Mockup 3 |
|----------|----------|----------|
| ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Failed_Mockup_1.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Failed_Mockup_2.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Failed_Mockup_3.jpg) |


---

# Analysis

Although the generated images were visually appealing, the prompt relied primarily on **identity preservation** while leaving physical constraints implicit.

Modern image generation models often optimize for aesthetics before physical realism. Without explicit instructions about object placement and scene physics, the model occasionally prioritized artistic composition over believable photography.

This motivated a second iteration focused on enforcing real-world photographic constraints.

---

# Iteration 2 — Physical Realism Constraints

The second iteration extended the system prompt with several additional constraint groups designed to reduce unrealistic generations.

## Added Constraint Categories

### Physical Realism Locks

Explicit rules were introduced to ensure that the product behaves as a real photographed object.

New constraints included:

- Product must always rest on a physical surface
- No floating or levitating products
- No unsupported positioning
- No merging with props or environment
- Preserve original materials (glass remains glass, plastic remains plastic, etc.)
- No added accessories that modify product identity
- Maintain branding readability under all lighting conditions

---

### Identity Preservation Hard Rule

An additional instruction clarified the intended interpretation of the input image.

Instead of recreating the product, the model was instructed to treat it as:

> A real-world photographed object being placed into a new photographic environment.

This significantly reduced redesigns and unwanted stylistic modifications of the product itself.

---

### Composition Rule

Another constraint explicitly defined acceptable photographic compositions.

The product should be:

- resting naturally on a surface
- positioned according to realistic product photography practices
- centered or following the rule of thirds
- never suspended in abstract space

---

# Improved Results

Adding explicit physical constraints produced noticeably more consistent mockups.

Observed improvements included:

- Physically grounded products
- Stable object placement
- Better interaction between product and surrounding props
- Improved identity preservation
- Consistent branding visibility
- More believable commercial photography compositions

---

## Example Output

| Mockup 1 | Mockup 2 | Mockup 3 | Mockup 4 |
|----------|----------|----------|----------|
| ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_1.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_4.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_5.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_8.jpg) |

---

# Comparison

| Aspect | Iteration 1 | Iteration 2 |
|---------|-------------|-------------|
| Product Identity | ✅ Good | ✅ Excellent |
| Physical Grounding | ❌ Inconsistent | ✅ Consistent |
| Floating Objects | Frequently observed | Eliminated |
| Material Preservation | Moderate | Excellent |
| Object-Prop Interaction | Sometimes unrealistic | Natural |
| Branding Consistency | Good | Excellent |
| Overall Photorealism | High | Very High |

---

# Key Takeaways

This iteration demonstrates an important principle of prompt engineering for image generation:

> Preserving product identity alone is insufficient for producing reliable commercial product photography.

Explicitly encoding physical constraints into the system prompt substantially improved generation quality by encouraging the model to treat the product as a real object governed by real-world physics rather than as an artistic element that could be freely repositioned or reinterpreted.

The resulting prompts consistently generated more realistic, production-ready mockups suitable for e-commerce, advertising, and marketing workflows.
