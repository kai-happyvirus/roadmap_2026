# Prepare, Orient, and Build Core Tools

🎯 Objective
Prepare your development environment and establish the foundation for your 6-month ML/CUDA/LLM engineering journey.
Today focuses on tool setup, Python numerical basics, and GPU readiness using Colab.

🧭 Goals for Today
- Install and configure all local tools needed for ML/CUDA learning.
- Verify Google Colab GPU runtime functionality.
- Practice basic NumPy operations to prepare for deeper math.
- Create your personal "ML Journey" GitHub repository.
- Write your first learning log entry.

## 1. Install Local Tools
```bash
# Install Homebrew 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Core tools
brew install python git visual-studio-code
```

## 2. Create Your Workspace
```bash
mkdir Day1
cd Day1
```

## 3. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate

pip install numpy matplotlib jupyter
```

## 4. Math + NumPy Workout

```python
import numpy as np
A = np.array([[3.,2.,0.],[1.,-1.,0.],[0.,5.,1.]])
b = np.array([2.,4.,-1.])
x = np.linalg.solve(A, b)       # solve Ax=b
A_inv = np.linalg.inv(A)
np.allclose(A @ A_inv, np.eye(3))
```

NumPy internally handles the conversion to homogeneous arrays.  
It follows a type hierarchy and promotes everything to the "highest" common type:
```
# Boolean → Integer → Float → Complex → String (Object)
bool < int < float < complex < str
```

---

## What I Did Today
- Installed Python, VS Code, and Homebrew.
- Set up virtual environment.
- Created first Jupyter notebook using NumPy.
- Verified Google Colab GPU access.

## What I Learned
- Arrays, matrices, transpose, and dot product.
- Difference between CPU vs GPU computations.
- How my local machine and Colab will work together for ML/CUDA learning.

## Tomorrow's Goal
- Deep dive into linear algebra (vectors, matrix multiplication, basis, rank).
- Start preparing for PyTorch tensor fundamentals.