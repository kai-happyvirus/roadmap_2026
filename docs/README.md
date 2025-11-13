# GitHub Pages Setup for roadmap_2026

This directory contains the Jekyll-based GitHub Pages site for documenting the 180-day ML/CUDA/LLM learning journey.

## Local Development

### Install Dependencies
```bash
cd docs
bundle install
```

### Run Local Server
```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000/roadmap_2026` to preview the site locally.

## Structure

```
docs/
├── _config.yml          # Jekyll configuration
├── _posts/              # Blog posts (learning logs)
│   └── YYYY-MM-DD-title.md
├── index.md             # Home page
├── about.md             # About the project
├── blog.md              # Blog archive page
├── progress.md          # Progress tracker
└── Gemfile              # Ruby dependencies
```

## Writing Blog Posts

Create new posts in `_posts/` with filename format:
```
YYYY-MM-DD-title.md
```

Example front matter:
```yaml
---
layout: post
title: "Day 2: Linear Algebra Deep Dive"
date: 2025-11-14
tags: [linear-algebra, numpy, math]
day: 2
---
```

## Publishing

1. Commit changes to `docs/` folder
2. Push to GitHub
3. Site automatically builds and deploys via GitHub Pages
4. Live at: https://kai-happyvirus.github.io/roadmap_2026

## Theme

Uses Minima theme (Jekyll default) for:
- Clean, readable design
- Mobile responsive
- Built-in syntax highlighting
- RSS feed generation
