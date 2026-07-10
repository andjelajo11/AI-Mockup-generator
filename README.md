# AI Product Mockup Generation Pipeline

> **A production-oriented AI pipeline that transforms manual product mockup creation into an automated, scalable workflow using n8n, ComfyUI, Flux Kontext, prompt engineering, and Python automation.**

---

## Project Overview

Creating high-quality product mockups manually is time-consuming, repetitive, and difficult to scale while maintaining visual consistency. This project explores how AI can automate the entire creative workflow—from product analysis and prompt generation to asset delivery—while preserving commercial-quality results.

Rather than focusing only on image generation, this repository demonstrates how different technologies can be combined into a reproducible production pipeline with documentation, automation, and quality standards.

This project was built as an exploration of production-ready AI workflow design, emphasizing reproducibility, maintainability, and automation over one-off AI outputs.

---

## Highlights

- ✅ Production-ready **n8n** workflow
- ✅ **ComfyUI + Flux Kontext** integration
- ✅ Modular **prompt engineering framework**
- ✅ AI-assisted **product scene generation**
- ✅ Automated **Google Drive asset delivery**
- ✅ Python automation tools for production workflows
- ✅ Design documentation and technical guardrails
- ✅ Iterative prompt engineering process

---

# Why This Project?

Modern e-commerce platforms require thousands of product images that are:

- Visually consistent
- Brand aligned
- Commercially appealing
- Fast to produce
- Easy to reproduce

Instead of manually creating every mockup, this project investigates how AI can automate repetitive creative work while keeping designers in control of quality.

The goal is not simply generating attractive images—it is building an end-to-end system capable of supporting production workflows.

---

# System Architecture 

Complete Workflow Architecture you can find here :
➡️ [`workflow_export.json`](architecture_diagram/Workflow_Architecture.md)

**Workflow demo**: https://www.loom.com/share/8856aca056994aa7bc70adcdd1d633db

The complete workflow combines prompt engineering, workflow orchestration, AI image generation, asset management, and production automation.

📄 **n8n Workflow**
<p align="center">
  <img src="architecture_diagram/n8n workflow diagram.png" width="900">
</p>

📄 **ComfyUI Workflow**
<p align="center">
  <img src="architecture_diagram/comfyui%20workflow%20diagram.png" width="900">
</p>

---

# Workflow Overview

The automated pipeline follows these stages:

```text
Product Image
      │
      ▼
Product Analysis
      │
      ▼
Prompt Generation
      │
      ▼
Scene Generation
      │
      ▼
Flux Kontext
      │
      ▼
Generated Mockups
      │
      ▼
Google Drive Upload
      │
      ▼
Final Assets
```

The exported workflow can be found here:

➡️ [`workflow_export.json`](workflow_export.json)

---

# Core Components

## 1. Prompt Engineering

Instead of relying on a single prompt, the project uses a modular prompt architecture that separates responsibilities into reusable building blocks.

Benefits include:

- Easier prompt iteration
- Improved maintainability
- Better debugging
- Consistent outputs across products

The framework covers:

- Product identity preservation
- Scene composition
- Camera positioning
- Lighting
- Material realism
- Commercial photography principles

📖 **Read more**

➡️ [`docs/PROMPT_STRUCTURE.md`](docs/PROMPT_STRUCTURE.md)

---

## 2. Design Principles

Consistent visual quality requires more than good prompts.

The repository documents a set of design rules that guide every generated image.

Examples include:

- Product proportion preservation
- Realistic materials
- Natural lighting
- Believable shadows
- Composition balance
- Commercial photography standards

These principles serve as technical guardrails that help maintain production-quality outputs.

📖 **Read more**

➡️ [`docs/DESIGN_PRINCIPLES.md`](docs/DESIGN_PRINCIPLES.md)

---
# Design & Prompt Engineering Journey

One of the primary goals of this project was understanding **why prompts succeed or fail**, rather than simply generating attractive images.

The repository documents multiple prompt iterations showing how prompt structure evolved through experimentation.

The development process follows:

1. Initial prompt
2. Generated result
3. Visual analysis
4. Prompt refinement
5. Improved generation

This iterative approach improved:

- Realism
- Lighting
- Composition
- Product preservation
- Commercial quality

## Iteration 1 — Initial System Prompt

The first version of the system prompt focused on generating diverse product photography concepts while preserving the product's visual identity.
Although these constraints significantly improved consistency compared to an unconstrained prompt, several recurring issues remained.
The generated prompts occasionally resulted in images with unrealistic physical behavior, including: Products floating, Unrealistic positioning...

## Example Outputs

| Mockup 1 | Mockup 2 | Mockup 3 |
|----------|----------|----------|
| ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Failed_Mockup_1.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Failed_Mockup_2.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Failed_Mockup_3.jpg) |


## Iteration 2 — Physical Realism Constraints

The second iteration extended the system prompt with several additional constraint groups designed to reduce unrealistic generations.

### Added Constraint Categories: 
 - Physical Realism Locks (Product must always rest on a physical surface, no floating or levitating products...)
 - Identity Preservation Hard Rule (A real-world photographed object being placed into a new photographic environment)
 - Composition Rule ( resting naturally on a surface, positioned according to realistic product photography practices)

## Improved Outputs

| Mockup 1 | Mockup 2 | Mockup 3 | Mockup 4 |
|----------|----------|----------|----------|
| ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_1.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_4.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_5.jpg) | ![](https://github.com/andjelajo11/AI-Mockup-generator/blob/main/mockup_exemples/products_images/Improved_Mockup_8.jpg) |


> **Note:** Replace the filenames above with the actual image names from `mockup_exemples/products_images/`.

Additional examples, prompt comparisons, development notes, and lessons learned are available here:

➡️ [`mockup_exemples/before_after.md`](mockup_exemples/before_after.md)

---

## Python Automation

AI generation is only one part of a production workflow.

To eliminate repetitive manual work, the repository includes Python utilities for asset organization and delivery.

### Included Utilities

### `batch_rename.py`

Automatically renames generated images using a consistent naming convention, making large batches easier to organize.

### `asset_packager.py`

Packages final deliverables into structured folders ready for clients or downstream workflows.

Example:

```text
deliveries/
└── Product001/
    ├── images/
    ├── manifest.txt
    └── Product001.zip
```

Repository:

➡️ [`python_scripts/`](python_scripts)

---

# Future Improvements

Potential future work includes:

- Automated product segmentation
- Batch processing for large product catalogs
- Multi-product workflows
- Automated quality evaluation
- Refined instructions focusing on: Composition, Lightning, Materials, Visual Style
- Testing different Generative models for image generation 
- Prompt versioning
- AI model benchmarking
- Metadata generation
- Additional cloud storage integrations
- Monitoring & logging
- Fully parameterized workflow templates

---

# Documentation

The repository is intentionally documented to improve reproducibility, maintainability, and communication of technical decisions.

| Document | Description |
|-----------|-------------|
| [README.md](README.md) | Project overview |
| [docs/PROMPT_STRUCTURE.md](docs/PROMPT_STRUCTURE.md) | Prompt architecture |
| [docs/DESIGN_PRINCIPLES.md](docs/DESIGN_PRINCIPLES.md) | Visual design rules |
| [mockup_exemples/before_after.md](mockup_exemples/before_after.md) | Prompt iteration examples |
| [workflow_export.json](workflow_export.json) | n8n workflow |
| [python_scripts](python_scripts) | Production automation utilities |

---

# Technical Highlights

This repository demonstrates experience across multiple disciplines required for production AI systems.

| Skill | Demonstrated Through |
|--------|----------------------|
| AI Workflow Design | n8n production workflow |
| Prompt Engineering | Modular prompt architecture |
| AI Image Generation | Flux Kontext + ComfyUI |
| Workflow Automation | n8n orchestration |
| Python Scripting | Asset management utilities |
| Documentation | Technical documentation |
| Production Mindset | Automation & reproducibility |
| Visual Consistency | Design principles & prompt refinement |

---

# Lessons Learned

Building reliable AI creative workflows requires significantly more than writing effective prompts.

Throughout development, several important insights emerged:

- Prompt structure matters more than prompt length.
- Clear visual design rules dramatically improve consistency.
- Automation extends beyond AI generation—asset organization and delivery are equally important.
- Documentation makes workflows easier to reproduce and maintain.
- Iterative experimentation is essential for achieving production-quality outputs.

These lessons influenced every stage of the project—from prompt engineering to workflow architecture.

---

# Repository Structure

```text
AI-Mockup-generator-main/
│
├── README.md
├── workflow_export.json
│
├── architecture_diagram/
│   ├── comfyui workflow diagram.png
│   └── n8n workflow diagram.png
│
├── docs/
│   ├── DESIGN_PRINCIPLES.md
│   └── PROMPT_STRUCTURE.md
│
├── mockup_exemples/
│   ├── before_after.md
│   └── products_images/
│
└── python_scripts/
    ├── asset_packager.py
    └── batch_rename.py
```

---

# Project Goal

This repository is not intended to showcase a single AI model or prompt.

Instead, it demonstrates how multiple technologies—including workflow automation, prompt engineering, scripting, documentation, and production design principles—can be combined into a maintainable creative system.

The emphasis is on designing workflows that are reproducible, scalable, and capable of reducing manual effort while maintaining commercially usable output.

This reflects the same engineering mindset required when building AI-powered creative pipelines for production environments.
