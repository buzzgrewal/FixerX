# **FixerX – Turning Math Mishaps into Math Masterpieces! 🎯✨**  
![FixerX](https://img.shields.io/badge/FixerX-AI%20Math%20Meme%20Fixer-blueviolet)  
🚀 **FixerX** is an AI-powered tool that **detects and corrects incorrect viral math memes** using the **DeepSeek-Math 7B RL** model. Whether it's misinterpreted order of operations or a basic algebra mistake, **FixerX ensures math accuracy with a touch of sass!** 😆

---

## 📌 **Table of Contents**  
- [🧠 Introduction](#-introduction)  
- [🎯 Features](#-features)  
- [⚙️ Tech Stack](#️-tech-stack)  
- [📂 Dataset](#-dataset)  
- [📌 Model & Fine-Tuning](#-model--fine-tuning)  
- [💡 Challenges & Solutions](#-challenges--solutions)  
- [🚀 Installation & Setup](#-installation--setup)  
- [🎨 Interactive Streamlit UI](#-interactive-streamlit-ui)  
- [🤖 Usage](#-usage)  
- [🔗 Links](#-links)  
- [📢 Contributing](#-contributing)  
- [📜 License](#-license)  

---

## 🧠 **Introduction**  

Math memes go viral every day, but some of them contain **incorrect calculations** that mislead people. FixerX is built to **detect and correct math mistakes** in memes using **AI-powered natural language processing (NLP)**.  

**🔍 Example:**  
❌ Incorrect: `8 ÷ 2(2+2) = 1`  
✅ FixerX Correction: `8 ÷ 2(2+2) = 16`  

FixerX uses **DeepSeek-Math 7B RL**, a specialized LLM for mathematical reasoning, and fine-tunes it with **LoRA (Low-Rank Adaptation)** to improve its understanding of viral math errors.  

---

## 🎯 **Features**  
✅ **AI-Powered Math Correction:** Detects & fixes incorrect math statements  
✅ **DeepSeek-Math Model:** Fine-tuned for enhanced accuracy  
✅ **LoRA Fine-Tuning:** Efficient model adaptation on a limited dataset  
✅ **Interactive UI:** Streamlit interface for easy meme correction  
✅ **Hyperparameter Tuning:** Adjustable settings for experimentation  
✅ **Fun "Error Rating" System:** Adds an element of engagement 🎭  

---

## ⚙️ **Tech Stack**  
- **Model:** DeepSeek-Math 7B RL  
- **Fine-Tuning:** LoRA, Hugging Face, PyTorch  
- **Dataset Handling:** Hugging Face Datasets, Pandas  
- **UI:** Streamlit  
- **Training & Deployment:** Google Colab, Kaggle  

---

## 📂 **Dataset**  

FixerX was fine-tuned on a **curated dataset of incorrect viral math memes**. The dataset contains:  
- **Incorrect Math Statements** (e.g., `3/6 = 3/2`)  
- **Corrected Versions** (e.g., `3/6 = 1/2`)  

Example Data Format:  
```json
[
    {"incorrect": "8 ÷ 2(2+2) = 1", "correct": "8 ÷ 2(2+2) = 16"},
    {"incorrect": "5² = 10", "correct": "5² = 25"}
]
```

---

## 📌 **Model & Fine-Tuning**  

### **Why DeepSeek-Math 7B RL?**  
🔹 **Optimized for Math Reasoning**  
🔹 **Better Symbolic Understanding**  
🔹 **Pre-trained on High-Quality Math Data**  

### **Fine-Tuning with LoRA**  
LoRA (Low-Rank Adaptation) was used to fine-tune the model efficiently:  
```python
model = AutoModelForCausalLM.from_pretrained(base_model_name)
model = PeftModel.from_pretrained(model, adapter_model_name)
model = model.merge_and_unload()
model.save_pretrained("merged_adapters")
```

---

## 💡 **Challenges & Solutions**  

### 🛑 **1. Tokenizer Padding Issues**  
**Problem:** Tokenizer was not padding inputs correctly, leading to shape mismatches.  
✅ **Solution:** Used `padding=True, truncation=True` to standardize inputs.  

### 🛑 **2. Model Loading Issues**  
**Problem:** Model files (`config.json`, `pytorch_model.bin`) weren’t saved properly.  
✅ **Solution:** Used `.merge_and_unload()` before saving.  

---

## 🚀 **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/buzzgrewal/FixerX.git
cd FixerX
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Download Model**  
Download the fine-tuned model and place it in `./FixerX_deepseekmath-r1`.  

---

## 🎨 **Interactive Streamlit UI**  

The **FixerX UI** lets users input incorrect math memes and adjust hyperparameters for better predictions.  

Run the Streamlit App:  
```bash
streamlit run app.py
```


### **💻 UI Features:**  
✔️ Input incorrect math statements  
✔️ Generate AI-powered corrections  
✔️ Adjust temperature, max length, and top-p sampling  
✔️ Get a **fun "Error Rating"**! 🎭  

![250307_19h57m23s_screenshot](https://github.com/user-attachments/assets/93d47115-73ef-431d-bc3c-86bcbd7b2180)


---

## 🤖 **Usage**  

### **Testing with Predefined Cases**  
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "./FixerX_deepseekmath-r1"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

test_cases = [
    "8 ÷ 2(2+2) = 1",
    "5² = 10",
    "3/6 = 3/2"
]

def correct_math_meme(math_statement):
    prompt = f"Incorrect: {math_statement}\nCorrect:"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100, temperature=0.7, do_sample=True)

    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("Correct:")[-1].strip()

for case in test_cases:
    print(f"❌ Incorrect: {case}\n✅ Model's Correction: {correct_math_meme(case)}\n")
```

---

## 🎭 **Fun Feature: Error Rating System**  

FixerX doesn't just correct mistakes—it also **rates them based on sassiness!** 😆  
```python
import random

def error_rating():
    sass = random.randint(50, 100)
    patience = 100 - sass
    return f"{sass}% sass, {patience}% patience!"

print(error_rating()) 
```

---

## 🔗 **Links**  
- **📂 GitHub Repo:** [FixerX on GitHub](https://github.com/buzzgrewal/FixerX)  
- **📊 Kaggle Notebook:** [FixerX on Kaggle](https://www.kaggle.com/models/buzzgrewal/fixerx)  
- **📝 Blog Post:** [FixerX on Medium](https://buzzgrewal.medium.com/fixerx-the-ai-that-turns-math-mishaps-into-masterpieces-5f635f7d2408)  

---

## 📢 **Contributing**  
Want to improve FixerX? Feel free to fork the repo, open PRs, and share ideas! 💡  

---

## 📜 **License**  
This project is licensed under the **MIT License**.  

---

🌟 **If you found FixerX useful, don’t forget to star ⭐ the repo!** Let’s fix math memes together! 🎯
