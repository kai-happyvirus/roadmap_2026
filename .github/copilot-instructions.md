# Copilot Instructions for roadmap_2026

## Project Overview
A **6-month ML/CUDA/LLM engineering learning journey tracker** with dual purposes:
1. **Personal Progress Tracking**: Daily tasks, code exercises, and learning logs for ML/CUDA/LLM mastery
2. **Public Demonstration**: GitHub Pages site showing feasibility of AI-suggested learning tracks

**Core Philosophy**: Track real progress, validate learning paths, inspire others through transparency.

## Repository Structure

### Current Layout
```
roadmap_2026/
├── Tasks/
│   └── Day1/
│       └── task.md          # Daily task descriptions with objectives and goals
├── .github/
│   └── copilot-instructions.md
└── README.md
```

### Expected Evolution
```
Tasks/
├── Day1/, Day2/, ..., Day180/   # Daily folders with tasks and code
│   ├── task.md                  # Day's objectives and goals
│   ├── *.py                     # Python exercises and implementations
│   ├── *.ipynb                  # Jupyter/Colab notebooks
│   └── log.md                   # Daily learning log (optional)
docs/                             # GitHub Pages source (future)
src/roadmap_2026/                 # Reusable utilities/tools (future)
```

## Key Conventions

### Daily Task Structure
Each `Tasks/DayN/task.md` follows this template:
- 🎯 **Objective**: High-level goal for the day
- 🧭 **Goals for Today**: Specific actionable items
- Topics covered: ML concepts, CUDA programming, LLM techniques, etc.

**Example**: `Tasks/Day1/task.md` focuses on environment setup, NumPy basics, Colab GPU verification.

### Code Organization
- **Local development**: Python scripts for concepts that run on local machines
- **Colab notebooks**: `.ipynb` files for GPU-intensive ML/CUDA exercises
- **Mixed approach**: Start locally, scale to Colab for compute-heavy tasks
- Keep code minimal and focused on learning objectives (not production quality)

### File Naming
- Tasks: `task.md` (consistent across all days)
- Code: Descriptive names like `numpy_basics.py`, `cuda_intro.cu`, `transformer_practice.ipynb`
- Logs: `log.md` or `notes.md` for reflection and insights

## Development Guidelines

### When Creating Daily Content
1. **Generate complete day folders**: `Tasks/DayN/` with at minimum `task.md`
2. **Match day number to content**: Day 1 = basics, later days = advanced topics
3. **Progressive complexity**: Build on previous days' concepts
4. **Practical focus**: Include runnable code examples, not just theory

### When Writing Code
- **Python**: NumPy, PyTorch, CUDA Python (CuPy), Triton for ML/CUDA work
- **Style**: Prioritize clarity and learning over optimization (document WHY, not just WHAT)
- **Comments**: Explain concepts being demonstrated, especially mathematical operations
- **Outputs**: Include expected results or verification checks

### Environment & Tools
- **Local**: Python 3.9+, NumPy, PyTorch, Jupyter (for local notebooks)
- **Cloud**: Google Colab for GPU access (T4, V100, A100 depending on availability)
- **Version control**: Commit daily progress with descriptive messages like `"Day 5: Backpropagation from scratch"`
- **Package managers**: Use pip/conda for simplicity (this is a learning repo, not production)

## GitHub Pages Integration (Future)

The repository will host a GitHub Pages site to:
- **Visualize progress**: Daily completion tracking, streak visualization
- **Share learnings**: Key insights, concept explanations, code highlights
- **Validate roadmap**: Show that AI-suggested 6-month tracks are achievable
- **Inspire others**: Provide template for structured ML/CUDA learning

When building pages features:
- Static site generator: Jekyll (GitHub Pages default) or simple HTML/CSS
- Data source: Parse `Tasks/*/task.md` for structure, completion tracking
- Analytics: Progress charts, topic coverage, time investment

## Commands & Workflows

### Creating New Day
```bash
mkdir -p Tasks/DayN
touch Tasks/DayN/task.md
# Populate task.md with objectives and goals
```

### Running Code Locally
```bash
python Tasks/DayN/script_name.py
# Or open .ipynb files in Jupyter/VS Code
```

### Colab Workflow
1. Upload `.ipynb` to Google Drive or directly to Colab
2. Enable GPU runtime: Runtime → Change runtime type → GPU
3. Save completed notebooks back to repo

### Progress Tracking
- Update README.md with completion status (e.g., checkboxes for each day)
- Commit regularly with meaningful messages
- Optional: Create `PROGRESS.md` for detailed reflections

## AI Agent Best Practices

### When Assisting with This Repo
1. **Honor the learning journey**: Suggest code that teaches, not just solves
2. **Scaffold, don't solve**: Provide hints and structure, let user implement
3. **Explain concepts**: ML/CUDA topics may be new; include brief explanations
4. **Validate feasibility**: If tasks seem unrealistic for a day, discuss scope
5. **Celebrate milestones**: Acknowledge progress at key checkpoints (Day 30, 60, etc.)

### Generating Daily Tasks
- Research actual ML/CUDA/LLM learning paths
- Ensure prerequisites from previous days are met
- Include "stretch goals" for advanced learners
- Provide resources (papers, tutorials, documentation)

### Code Review Focus
- **Correctness**: Math and ML concepts implemented properly
- **Clarity**: Code readable by someone learning the concept
- **Completeness**: Exercises include verification/testing
- **CUDA specifics**: Memory management, kernel optimization patterns

## Notes
- This is a **live learning document** - update as the journey progresses
- Track what works well and what doesn't for future learners
- The goal is authentic progress, not perfection
