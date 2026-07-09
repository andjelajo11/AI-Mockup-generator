# Design Principles

## Overview

This document defines the visual design standards that govern the AI Product Mockup Generator.

Rather than generating aesthetically pleasing images at random, the workflow follows a consistent set of creative principles inspired by professional product photography, e-commerce production, and DTC (Direct-to-Consumer) brand imagery.

These principles serve as the foundation for prompt generation and ensure that every generated image remains visually consistent, commercially usable, and faithful to the original product.

The objective is not to redesign products, but to place existing products into new photographic environments while preserving their visual identity.

---

# Design Goals

The workflow is designed around five core objectives:

- Preserve product identity with pixel-level consistency whenever possible.
- Generate commercially viable product photography rather than artistic reinterpretations.
- Produce visually diverse marketing assets through scene variation instead of product variation.
- Maintain physical realism across every generated image.
- Create reusable prompts that scale across different products and visual styles.

---

# Product Photography Principles

## Composition

Composition determines how the viewer's attention is directed toward the product.

The generated scene should always prioritize product visibility over environmental complexity.

### Current Implementation:
Rule of thirds
Centered hero shot
Natural placement

### Future Enhancements:
visual hierarchy
leading lines
foreground/background balance
framing
copy space
marketplace optimization


Avoid:

- Cluttered environments
- Occluded products
- Distracting foreground objects
- Abstract or surreal compositions

---

## Camera

Camera language should resemble real commercial photography.

Preferred camera perspectives include:

- Hero shot
- Eye-level perspective
- 45° product angle
- Top-down composition
- Close-up detail shots
- Lifestyle perspective when appropriate

Depth of field should enhance subject isolation while maintaining sufficient product clarity.

Camera positioning should always reinforce product readability.

---

## Lighting

Lighting establishes mood while preserving product accuracy.

Preferred lighting setups include:

### Studio

- Soft diffused key light
- High-key ecommerce lighting
- Controlled shadow transitions
- Even illumination

### Editorial

- Soft directional lighting
- Natural window light
- Neutral contrast
- Subtle shadow depth

### Cinematic

- Rim lighting
- Motivated practical lighting
- High contrast
- Film-inspired color grading
- Controlled atmospheric depth

Lighting should enhance realism without hiding important product details.

---

## Materials

Material fidelity is critical.

The AI should preserve the physical characteristics of every surface.

Maintain:

- Surface roughness
- Reflection behavior
- Transparency
- Gloss level
- Metallic appearance
- Fabric texture
- Plastic finish
- Wood grain
- Glass properties

Never reinterpret or redesign materials.

Examples:

- Glass remains glass.
- Metal remains metal.
- Leather remains leather.
- Fabric weave should remain believable.

---

## Color Management

Color consistency is essential for commercial product photography.

The workflow should preserve:

- Original product colors
- Logo colors
- Packaging colors
- Brand identity

Images should maintain:

- Neutral white balance
- Controlled saturation
- Accurate contrast
- Realistic exposure

Avoid:

- Oversaturation
- Unrealistic color shifts
- Stylized color casts affecting the product

Scene color grading may change, but product color should remain visually accurate.

---

# Product Identity Preservation

The workflow follows a strict identity preservation philosophy.

The product is treated as an existing physical object being photographed.

The workflow does **not** generate a new interpretation of the product.

The following attributes must remain unchanged:

- Shape
- Proportions
- Branding
- Logos
- Labels
- Materials
- Product geometry
- Surface details
- Manufacturing features

Environmental storytelling may change.

The product itself may not.

---

# Physical Realism

Every generated scene should obey real-world photographic constraints.

Products should always:

- Rest on a believable supporting surface
- Interact naturally with gravity
- Cast realistic shadows
- Exhibit physically plausible reflections
- Maintain proper scale relative to surrounding objects

The workflow intentionally avoids:

- Floating objects
- Impossible perspectives
- Product deformation
- Unrealistic material behavior
- Merged geometry
- Surreal positioning

The result should resemble a professionally photographed product rather than AI-generated artwork.

---

# Visual Styles

The workflow currently supports three primary creative directions.

## Editorial

Characteristics:

- Clean compositions
- Sophisticated styling
- Neutral palettes
- Minimal environments
- Magazine-quality imagery
- Crisp product focus

---

## Cinematic

Characteristics:

- Dramatic storytelling
- Directional lighting
- Moody atmosphere
- Film-inspired grading
- Environmental context
- Shallow depth of field

---

## Fashion

Characteristics:

- Bold styling
- Dynamic compositions
- Lifestyle environments
- High visual energy
- Trend-oriented aesthetics
- Strong contrast

Additional styles can be introduced without changing the underlying creative principles.

---

# Scene Variation Strategy

Creative diversity should come from the scene—not the product.

Variation is introduced through:

- Camera angle
- Lighting setup
- Environment
- Background
- Props
- Surface material
- Color palette
- Mood
- Composition

The product remains constant across every generated image.

---

# Prompt Design Philosophy

The prompt generation process follows a layered approach.

Every prompt is constructed from four conceptual components:

1. Product Identity
2. Creative Direction
3. Photographic Composition
4. Physical Constraints

This separation ensures that artistic variation never compromises product fidelity.

---

# Commercial Photography Standards

Generated images should resemble assets produced by professional commercial photographers.

Images should be suitable for:

- Ecommerce listings
- Marketplace hero images
- Shopify stores
- Amazon listings
- Product launches
- Social media campaigns
- Brand marketing
- Digital advertising

The workflow prioritizes production-ready outputs over experimental artistic expression.

---

# Future Evolution

These principles are intended to evolve alongside the workflow.

Future iterations may introduce:

- Automated composition selection
- Material-aware prompting
- Camera presets
- Lens simulation
- Brand-specific creative guidelines
- Automated quality validation
- Multi-image consistency checks
- Marketplace-specific composition rules

Regardless of future improvements, the core philosophy remains unchanged:

> Preserve the product. Enhance the photography.
