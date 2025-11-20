# ✅ 📅 Day 1 (19 Nov) — Set Up Your Foundation

## Theme: Tools + Python Refresh

This day is light but essential. After this, everything else becomes smoother.

---

## 🎯 Objectives for Today

- Prepare your local development environment (MacBook Pro)
- Refresh Python essentials (so later algorithms + PyTorch feel natural)
- Start light math prep (needed for linear algebra & autograd)
- Open and verify Google Colab GPU (your main GPU tool for now)
- Create your "ML Journey" GitHub repo to track work

**This is about building the base you'll use for the next 6 months.**

---

## 🧠 Why This Matters

Your long-term goal includes:
- CUDA
- C/C++
- ML + DL + LLMs
- Optimization
- OS, algorithms, databases
- Joining a top-tier team like Unsloth

All these require:
- ✅ Strong environment
- ✅ Strong Python foundations
- ✅ Strong linear algebra foundations

**Today prepares that ground.**

🕒 **Time Required:** ~3 hours total

---

## 📌 Day 1 Detailed Task List

### 1️⃣ Install / Verify Your Environment (30 min)

**On your MacBook:**

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python, Git, and VS Code
brew install python git
brew install --cask visual-studio-code

# Create your ML workspace
mkdir ~/ml_journey
cd ~/ml_journey
```

### 2️⃣ Create Your Python Virtual Environment (10 min)

```bash
python3 -m venv env
source env/bin/activate
pip install numpy matplotlib jupyter
```

### 3️⃣ Quick Python Refresh (20–30 min)

**Open VS Code → new file → `day1_python_basics.py`**

Practice:
- Lists
- Loops
- Functions
- List comprehensions
- Dictionaries

Sample warm-up:
```python
def square_list(xs):
    return [x*x for x in xs]

print(square_list([1,2,3,4]))
```

### 4️⃣ NumPy Warm-up (20 min)

**Create a Jupyter notebook:**

```bash
jupyter notebook
```

**Inside notebook:**

```python
import numpy as np

A = np.array([[1,2,3],[4,5,6]])
print(A.T)

v = np.array([1,2,3])
print(A @ v)
```

Goal: feel comfortable with arrays → these become tensors in PyTorch.

### 5️⃣ Verify Google Colab GPU (10 min)

Go to: https://colab.research.google.com

**Runtime → Change runtime → GPU**

Run:
```python
!nvidia-smi
import torch
print(torch.cuda.is_available())
```

If it prints `True`, you're ready for PyTorch GPU training.

### 6️⃣ Create GitHub Repo (10–15 min)

Create repo: `ml_journey`

Push your Day 1 files:
```bash
git init
git add .
git commit -m "Day 1 setup"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### 7️⃣ Light Math Review (20 min)

Watch or read:

**"How GPUs work — NVIDIA (3 minutes)"**  
👉 https://youtu.be/0fKQVvr5moY  
(short, beginner-friendly overview)

**NumPy Quickstart**  
👉 https://numpy.org/doc/stable/user/quickstart.html

---

## 🏁 End of Day Checklist

- ✅ Python works
- ✅ VS Code works
- ✅ Jupyter Notebook works
- ✅ NumPy works
- ✅ Colab GPU works
- ✅ GitHub repo created
- ✅ You understand basic arrays & matrix ops

**If all checked → you're perfectly set for Day 2: NumPy + Linear Algebra tomorrow.**
