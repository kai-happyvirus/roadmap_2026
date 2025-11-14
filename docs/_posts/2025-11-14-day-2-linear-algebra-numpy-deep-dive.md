---
layout: post
title: "Day 2: Core Linear Algebra for ML + NumPy Deep Dive"
date: 2025-11-14
tags: [linear-algebra, numpy, matrices, foundations]
day: 2
---

# Day 2: Core Linear Algebra for ML + NumPy Deep Dive

**Focus**: Linear algebra fundamentals and NumPy implementation

## 🎯 Today's Objectives

- Understand GPU architecture and why it matters for ML
- Master NumPy array operations and dimensional reasoning
- Learn essential linear algebra: vectors, matrices, dot products, norms
- Connect mathematical concepts to future neural network applications

## ✅ What I Accomplished

### 1. GPU Fundamentals

Watched NVIDIA's introduction to GPUs and learned:
- **CPUs**: Good for sequential tasks (few powerful cores)
- **GPUs**: Designed for parallel tasks (thousands of smaller cores)
- **Why this matters**: Matrix operations in neural networks are highly parallelizable
- Deep learning requires millions of matrix multiplications → GPUs are essential

### 2. NumPy Deep Dive

Mastered key `ndarray` attributes:

```python
import numpy as np

a = np.arange(15).reshape(3, 5)

# Key attributes
a.ndim      # Number of dimensions (2)
a.shape     # Dimensions tuple (3, 5) - 3 rows, 5 columns
a.size      # Total elements (15)
a.dtype     # Data type (int64)
a.itemsize  # Bytes per element (8 for int64)
a.data      # Memory buffer (rarely needed directly)
```

### 3. Understanding Dimensions

**The progression from 0D to 4D:**

```python
# Scalar (0D) - Single number
scalar = np.array(5)              # ndim=0, shape=()

# Vector (1D) - List of numbers
vector = np.array([1, 2, 3])      # ndim=1, shape=(3,)

# Matrix (2D) - Table of numbers
matrix = np.array([[1, 2, 3],     # ndim=2, shape=(2, 3)
                   [4, 5, 6]])

# Tensor (3D+) - Multi-dimensional array
tensor = np.arange(24).reshape(2, 3, 4)  # ndim=3, shape=(2, 3, 4)
```

**Real-world mapping:**
- **Scalar**: Single data point (e.g., loss value)
- **Vector**: Feature vector, word embedding
- **Matrix**: Batch of features, weight matrix
- **3D Tensor**: Grayscale images (height × width × batch)
- **4D Tensor**: RGB images (batch × channels × height × width)

### 4. Matrix Multiplication Rules

**Key insight**: Inner dimensions must match!

```python
# For A @ B to work:
# If A is (m, n) and B is (p, q)
# Then n must equal p
# Result will be (m, q)

A = np.arange(6).reshape(2, 3)    # Shape (2, 3)
B = np.arange(7, 13).reshape(3, 2) # Shape (3, 2)
C = A @ B                          # Shape (2, 2) ✓

# Why: For each element in result, we need:
# - A row from A (length 3)
# - A column from B (length 3)
# - Multiply corresponding pairs and sum
```

**Visual:**
```
A (2×3) @ B (3×2) = C (2×2)
       ↑     ↑
       Must match!
```

### 5. Dot Product Deep Dive

The dot product measures "how much two vectors point in the same direction":

```python
a = np.array([0, 1, 2])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)  # 0×4 + 1×5 + 2×6 = 0 + 5 + 12 = 17
# Also: a @ b

# Geometric interpretation:
# dot(a, b) = |a| × |b| × cos(θ)
# where θ is the angle between vectors
```

**Special cases:**
- `dot(a, b) = 0` → Vectors are **orthogonal** (perpendicular)
- `dot(a, b) > 0` → Vectors point in similar directions
- `dot(a, b) < 0` → Vectors point in opposite directions

### 6. Transpose Operations

Flip rows and columns - critical for dimension matching!

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])  # Shape (2, 3)

A_T = A.T  # Shape (3, 2)
# [[1, 4],
#  [2, 5],
#  [3, 6]]
```

**Why it matters for neural networks:**
- Forward pass: `output = input @ weights`
- Backward pass (gradient): `grad_input = grad_output @ weights.T`
- Transpose enables dimension matching during backpropagation!

### 7. Identity Matrix

The "do nothing" matrix - like multiplying by 1:

```python
I = np.eye(3)  # 3×3 identity matrix
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

A = np.array([[2, 3], [4, 5]])
print(A @ np.eye(2))  # Returns A unchanged

# Property: A @ I = I @ A = A
```

### 8. Vector Norms (L1 and L2)

Norms measure the "magnitude" or "length" of a vector:

**L1 Norm (Manhattan distance):**
```python
v = np.array([3, -4, 5])
l1_norm = np.linalg.norm(v, ord=1)  # |3| + |-4| + |5| = 12
# Sum of absolute values - like walking on a city grid
```

**L2 Norm (Euclidean distance):**
```python
v = np.array([3, -4])
l2_norm = np.linalg.norm(v)  # √(3² + 4²) = √25 = 5
# Straight-line distance
```

**Comparison:**
```python
v = np.array([3, 4])
print(f"L1 norm: {np.linalg.norm(v, ord=1)}")  # 7 (taxi cab)
print(f"L2 norm: {np.linalg.norm(v, ord=2)}")  # 5 (as crow flies)
```

**ML Applications:**
- **L1**: Sparse solutions (feature selection), used in Lasso regression
- **L2**: Regularization in neural networks, gradient descent optimization

### 9. Orthogonality Check

```python
u = np.array([1, -1])
w = np.array([1, 1])
print(np.dot(u, w))  # 1×1 + (-1)×1 = 0 → Orthogonal! ✓

# Orthogonal vectors are independent - crucial for:
# - Principal Component Analysis (PCA)
# - Attention mechanisms in Transformers
# - Weight initialization in neural networks
```

## 💡 Key Insights

### Connection to Neural Networks

1. **Matrix Multiplication = Layer Operations**
   ```python
   # Every neural network layer does:
   output = activation(input @ weights + bias)
   #                    ↑
   #           This is matrix multiplication!
   ```

2. **Dot Product = Similarity Measure**
   - Transformers use dot product attention: `Q @ K.T` measures query-key similarity
   - Word embeddings: `word1 @ word2` measures semantic similarity

3. **Norms for Optimization**
   - Gradient clipping uses L2 norm to prevent exploding gradients
   - Batch normalization normalizes using L2 norms
   - Weight decay is L2 regularization

4. **Transpose in Backpropagation**
   - Forward: `h = x @ W`
   - Backward: `dW = x.T @ dh` (transpose needed!)

### GPU Parallelism Connection

Matrix multiplication is **embarrassingly parallel**:
```python
# Computing C = A @ B
# Each element C[i,j] is independent:
C[i,j] = sum(A[i,:] * B[:,j])

# GPU can compute ALL elements simultaneously!
# This is why GPUs accelerate deep learning 100x-1000x
```

## 🤔 Day 2 Reflections

### What surprised me about matrix multiplication?

The **dimension matching rule** (inner dimensions must align) initially seemed arbitrary, but now I understand it's fundamental to the operation itself. Each output element requires pairing elements from a row and column of matching length.

Also surprising: Matrix multiplication is **not commutative** (`A @ B ≠ B @ A`). This contrasts with scalar multiplication and has huge implications for neural network design.

### Why is the dot product fundamental for neural networks?

**Three key reasons:**

1. **It's the building block of matrix multiplication** - Every element in a matrix product is a dot product
2. **It measures similarity** - Used in attention mechanisms to compare queries and keys
3. **It's computationally efficient on GPUs** - Parallel multiply-add operations are what GPUs excel at

The entire Transformer architecture (foundation of LLMs) relies on scaled dot-product attention!

### How will these operations map onto GPU parallelism?

**Matrix multiplication parallelizes beautifully:**
- Each element of the output can be computed independently
- GPU assigns one thread per output element
- Thousands of threads compute simultaneously

**Later in CUDA (Month 3)**, I'll write kernels that:
- Assign threads to compute individual dot products
- Use shared memory to cache matrix tiles
- Optimize memory access patterns for coalescing

Understanding shapes NOW makes CUDA memory layouts intuitive LATER.

## 📊 Progress Stats

- **Time spent**: ~2 hours
- **Concepts mastered**: 8 (ndarray attributes, dimensions, matrix mult, dot product, transpose, identity, norms, orthogonality)
- **Code exercises**: 7 (all NumPy operations practiced)
- **Notebook cells**: 28 (comprehensive coverage)

## 🎯 Tomorrow's Plan (Day 3)

- Vector operations and advanced matrix multiplication
- NumPy broadcasting rules (crucial for efficiency!)
- Advanced indexing and slicing techniques
- Introduction to eigenvalues and eigenvectors
- Begin connecting math to neural network operations

## 🔗 Resources Used

- [NVIDIA GPU Introduction](https://www.nvidia.com/en-us/drivers/what-is-gpu/)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Khan Academy: Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [Matrix Multiplication Visualizer](https://matrixmultiplication.xyz/)

---

**Reflection**: Day 2 solidified the mathematical foundation for everything ahead. Every concept learned today - matrix multiplication, dot products, norms - appears hundreds of times in neural network code. The connection between linear algebra and GPU parallelism is becoming clear. Excited to build on this tomorrow!

**Mood**: 💪 Confident and energized - the math is clicking!

**Key Takeaway**: *Linear algebra isn't just abstract math - it's the language of deep learning. Every operation in a neural network is a matrix operation at its core.*
