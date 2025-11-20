# 📅 Day 2 — NumPy & Core Math Foundations (20 Nov)

**Time Required:** 1–3 hours depending on free time

---

## 🎯 Objective of Day 2

Build a solid numerical computing foundation because:

- PyTorch tensors behave almost exactly like NumPy arrays
- CUDA kernels operate on arrays/tensors
- Every ML algorithm begins with matrix operations
- Understanding broadcasting and vectorization leads to model-level optimization later
- Linear algebra underpins all neural networks & attention mechanisms

**Today = your first "real ML math + code" day.**

---

## ✔️ Day 2 Tasks (Step-by-Step)

### 1️⃣ NumPy Fundamentals Review

**Time:** 30–45 min

**Learn/Review:**
- Array creation: `np.array`, `np.zeros`, `np.ones`, `np.random.randn`
- Shapes & dimensions: `.shape`, `.ndim`
- Indexing & slicing
- Broadcasting rules (VERY important — used everywhere in ML & CUDA)

**✅ Code to practice:**

Run these in a Jupyter notebook on your MacBook:

```python
import numpy as np

A = np.random.randn(3, 4)
B = np.random.randn(4,)

print("A shape:", A.shape)
print("B shape:", B.shape)

C = A + B   # broadcasting
print("C shape:", C.shape)
```

**Understand why this works** — because NumPy automatically expands B.

---

### 2️⃣ Core Matrix Operations

**Time:** 30–45 min

**Learn:**
- Matrix addition
- Dot product / matrix multiplication
- Row & column norms
- Transpose

**✅ Exercises:**

```python
A = np.random.randn(4, 3)
B = np.random.randn(3, 2)

# Matrix multiply
C = A @ B

# Column norms
col_norms = np.linalg.norm(A, axis=0)

# Row norms
row_norms = np.linalg.norm(A, axis=1)
```

**You MUST be comfortable reading shapes and predicting results without running.**

---

### 3️⃣ Mini ML Exercise

**Time:** 20–30 min

This simulates the computation used in logistic regression & linear models.

**Problem:**

Given:
- Matrix `X` of shape `(1000, 3)`
- Weight vector `w` of shape `(3, 1)`

Compute predictions: `y = Xw`

**Code:**

```python
X = np.random.randn(1000, 3)
w = np.random.randn(3, 1)

y = X @ w
print(y.shape)  # should be (1000, 1)
```

**Understand why this shape works** — this is the basis of ALL linear neural layers.

---

### 4️⃣ Optional Deepening (Highly Recommended)

**Time:** 15–20 min

Try to write logistic regression forward pass without PyTorch:

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

y_hat = sigmoid(X @ w)
```

This is the seed idea behind all neural networks:

**linear → activation → output**

---

### 5️⃣ Reading Assignment

**Time:** 15–30 min

**📖 Required:**

**Khan Academy — Linear Algebra (Vectors & Matrices)**  
👉 https://www.khanacademy.org/math/linear-algebra

Study these:
- Vectors & spaces
- Matrix multiplication
- Transformations

**📖 Optional (but recommended):**

**NumPy Quickstart**  
👉 https://numpy.org/doc/stable/user/quickstart.html

---

## 🧠 Day 2 Understanding Checklist

By end of today, you should confidently answer:

### Conceptual
- [ ] What is broadcasting? When does it work?
- [ ] Why is vectorization faster than Python loops?
- [ ] Why is `X @ w` fundamental in ML?

### Mechanical
- [ ] Predict the shape of `A + B` or `A @ B`
- [ ] Perform dot products mentally
- [ ] Explain what a "row norm" is
