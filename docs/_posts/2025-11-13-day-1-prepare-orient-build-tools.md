---
layout: post
title: "Day 1: Prepare, Orient, and Build Core Tools"
date: 2025-11-13
tags: [setup, numpy, environment, foundations]
day: 1
---

# Day 1: Prepare, Orient, and Build Core Tools

**Focus**: Environment setup, NumPy fundamentals, and GPU verification

## 🎯 Today's Objectives

- Install and configure local development tools
- Set up Python virtual environment with ML packages
- Practice NumPy basics: arrays, matrices, operations
- Verify Google Colab GPU access
- Understand core concepts: scalars, vectors, tensors

## ✅ What I Accomplished

### 1. Development Environment Setup
Successfully installed and configured:
- Homebrew (macOS package manager)
- Python 3.12
- Visual Studio Code
- Git for version control

Created virtual environment and installed core packages:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy matplotlib jupyter
```

### 2. NumPy Fundamentals

Practiced essential NumPy operations:

**Array Creation & Inspection:**
```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)  # (2, 3) - 2 rows, 3 columns
```

**Matrix Operations:**
```python
# Transpose - flip rows and columns
print(A.T)  # (3, 2) matrix

# Dot product of row vectors
dot_result = np.dot(A[0], A[1])  # 1*4 + 2*5 + 3*6 = 32
```

**Linear Algebra (From task.md):**
```python
# Solve system of linear equations: Ax = b
A = np.array([[3.,2.,0.],[1.,-1.,0.],[0.,5.,1.]])
b = np.array([2.,4.,-1.])
x = np.linalg.solve(A, b)

# Matrix inversion and verification
A_inv = np.linalg.inv(A)
np.allclose(A @ A_inv, np.eye(3))  # True - confirms A * A_inv = I
```

### 3. Created Learning Notebook

Built `day1_numpy_intro.ipynb` with:
- Hands-on NumPy exercises
- Notes on matrices and transpose
- Explanations of why these matter for deep learning

## 💡 Key Learnings

### Understanding Core Concepts

**Scalar** → Single number (e.g., `temperature = 25.5`)

**Vector** → List of numbers (e.g., `position = [3, 4]`)

**Matrix** → 2D grid of numbers (rows and columns)

**Tensor** → Multi-dimensional array (generalization of vectors and matrices)

### NumPy's Type System

Learned that NumPy arrays are **homogeneous** (all elements same type):
```python
# Mixed input gets promoted to common type
mixed = np.array([1, 2.5, 3])  # All become float64: [1.  2.5 3. ]
```

**Type hierarchy**: `bool < int < float < complex < str`

This homogeneous constraint enables:
- Fast vectorized operations (SIMD)
- Predictable memory layout
- Efficient linear algebra operations
- Foundation for GPU computing (crucial for future CUDA work!)

### Why This Matters for Deep Learning

1. **Neural networks are matrix multiplications** - Every layer transforms inputs using matrices
2. **Batch processing** - Process multiple samples simultaneously using tensors
3. **Transpose for dimension matching** - Align dimensions for valid matrix operations
4. **Backpropagation requires transpose** - Gradient flow needs transposed weight matrices

## 🤔 Challenges & Questions

- Initially confused about "heterogeneous" vs "homogeneous" data
- Understanding REPL (Read-Eval-Print Loop) for quick experimentation
- How NumPy internally handles type promotion - fascinating system!

## 🔗 Resources Used

- NumPy official documentation
- Linear algebra review (matrix operations)
- Google Colab for GPU verification

## 🎯 Tomorrow's Plan (Day 2)

- Deep dive into linear algebra concepts
- Vectors, matrix multiplication, basis, rank
- Start preparing for PyTorch tensor fundamentals
- More complex NumPy operations

## 📊 Progress Stats

- **Time spent**: ~3 hours
- **Code written**: NumPy exercises, linear algebra solver
- **Concepts mastered**: 5 (scalar, vector, tensor, homogeneous arrays, type promotion)
- **Tools configured**: 4 (Python, VS Code, Git, Jupyter)

---

**Reflection**: Great start! The foundation is solid. Understanding why NumPy requires homogeneous arrays (performance + GPU readiness) was a key insight. Excited to build on this tomorrow with deeper linear algebra.

**Mood**: 😊 Motivated and energized!
