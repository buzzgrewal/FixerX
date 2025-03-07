import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import random


MODEL_PATH = "./FixerX_deepseekmath-r1" 
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH).to("cuda" if torch.cuda.is_available() else "cpu")


def error_rating():
    sass = random.randint(50, 100)
    patience = 100 - sass
    return f"🧐 Error Rating: {sass}% sass, {patience}% patience!"


st.set_page_config(page_title="FixerX - Math Meme Debugger", page_icon="⚡", layout="centered")

st.title("⚡ FixerX: Math Meme Debugger")
st.subheader("Turning Math Mishaps into Math Masterpieces! 🎯✨")

st.write("Enter an incorrect math meme, and let FixerX correct it! 🔢")


user_input = st.text_area("❌ Incorrect Math Statement:", placeholder="e.g., 8 ÷ 2(2+2) = 1")


st.sidebar.header("⚙️ Hyperparameter Settings")
temperature = st.sidebar.slider("Temperature (0 = deterministic, 1 = creative)", 0.0, 1.5, 0.7, 0.1)
max_length = st.sidebar.slider("Max Output Length", 50, 200, 100, 10)
top_p = st.sidebar.slider("Top-p (sampling diversity)", 0.0, 1.0, 0.9, 0.05)


def correct_math_meme(math_statement):
    prompt = f"Incorrect: {math_statement}\nCorrect:"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            do_sample=True
        )

    corrected_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_output.split("Correct:")[-1].strip()


if st.button("🔍 Fix Math Meme"):
    if user_input.strip():
        with st.spinner("Analyzing & fixing the math... 🔢"):
            corrected_text = correct_math_meme(user_input)
            st.success("✅ Fixed Math Statement:")
            st.write(f"**{corrected_text}**")
            
            st.info(error_rating())
    else:
        st.warning("⚠️ Please enter a math statement to correct.")


st.markdown("---")
st.caption("⚡ **FixerX** - Debugging Math, One Meme at a Time! 🚀")
