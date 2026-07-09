# 🚀 AI Product Mockup Generator

Generate professional AI-powered product mockups from a single product image.

This n8n workflow automatically transforms a product photo into **three unique, high-quality marketing mockups** using AI while preserving the product's original appearance, branding, shape, and materials.

1. Upload a product image.
2. Select a visual style (Editorial, Cinematic, Fashion, or any custom style).
3. AI creates 3 unique scene prompts while preserving the exact product identity.
4. Flux Kontext generates 3 photorealistic mockups.
5. Generated images are downloaded and automatically uploaded to Google Drive.

<img width="713" height="343" alt="workflow ai mocku" src="https://github.com/user-attachments/assets/47ea9efc-ead3-45f8-aeb0-82324a5775c4" />
---

# Workflow Overview

```
Product Onboarding
      │
      ▼
Image Preprocessing
      │
      ▼
Prompt Engine
      │
      ▼
Prompt Processing
      │
      ▼
Image Mockup Generation
      │
      ▼
Image Download
      │
      ▼
Asset Managment
```

---

# Workflow Documentation

## 📦 1. Product Onboarding & Preroccesing

The workflow begins by loading the source product image.

The image can come from:

* HTTP URL
* Cloudinary
* Google Drive
* Any storage provider
* User upload (easy to replace)

Basic image processing is done -> background removal via api. Depending on the use case it could be extended for any other functionality (Resolution upscaling, Reflection and shadow removal, product detection & cropping...) 

**Output**

* Original product image

---

## 🎨 2. Prompt Engine

The Prompt Engine is responsible for creating creative scene descriptions.

Instead of directly generating images, an AI Agent in role of Visual Art Director first analyzes:

* the product
* the selected visual style
* brand photography principles

It then produces **three completely different prompts** that describe three unique product photography scenes.

Each prompt follows strict rules:

* Follows composition rules (lightning, surface...)
* Physical locks
* Preserve product identity 
* Preserve branding
* Preserve materials
* Preserve proportions
* Never redesign the product
* Only change the surrounding environment

Example styles:

* Editorial
* Cinematic
* Fashion
* Luxury
* Lifestyle
* Minimal
* Any custom style

**Output**

Three production-ready prompts.

---

## ✂️ 3. Prompt Processing

The generated prompts are separated into individual items.

This allows all three image generations to run independently.

Benefits:

* Faster execution
* Independent generations
* Easy scaling to more than three outputs

---

## ✨ 4. Mockup Generation

Each prompt is sent to the Flux Kontext API.

Flux receives:

* Original product image
* Scene prompt
* Generation settings

The model creates a realistic marketing image while keeping the product visually identical to the source image.

Each generation produces a different composition, lighting setup, and background.


---


## 📥 5. Download & Storage

After generation completes, the workflow:

* Downloads each image
* Converts it into a binary file
* Rename image files into predefined names
* Uploads it directly to Google Drive

The generated mockups are immediately ready for use.

---

## 🖼 Final Result

The workflow produces:

* 3 unique product mockups
* Consistent branding
* Professional product photography
* Marketing-ready images
* Automatic cloud storage

---

# Features

* ✅ AI-generated product photography
* ✅ Automatic prompt engineering
* ✅ Three unique mockups per execution
* ✅ Product identity preservation
* ✅ Parallel image generation
* ✅ Automatic download
* ✅ Google Drive integration
* ✅ Easily customizable visual styles
* ✅ Modular n8n workflow

---

# Technologies Used

* **n8n**
* **Flux Kontext Pro**
* **Mistral Large**
* **Google Drive**
* **HTTP Request Nodes**
* **JavaScript Code Node**

---

# Customization

This workflow is designed to be easily extended.

You can:

* Add new photography styles
* Generate more than three mockups
* Replace Flux with another image generation model
* Store outputs in AWS S3, Dropbox, Cloudinary, or other storage providers
* Connect it to forms, webhooks, APIs, or chatbots

---

# Example Use Cases

* E-commerce product photography
* Amazon listings
* Shopify stores
* Social media content
* Advertising creatives
* Product launches
* Brand campaigns
* Creative asset generation

---

# Future Improvements

* Style selector input
* Multiple aspect ratios
* Batch product processing
* Automatic background removal
* Metadata generation
* SEO image naming
* Watermark support
* Webhook/API trigger
* Gallery output page

---





