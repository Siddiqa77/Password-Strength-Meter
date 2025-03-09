import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Criteria checks
    length = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*]", password))
    
    # Strength calculation
    if length:
        strength += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")
    
    if has_upper:
        strength += 1
    else:
        feedback.append("🔴 Add at least one uppercase letter.")
    
    if has_lower:
        strength += 1
    else:
        feedback.append("🔴 Add at least one lowercase letter.")
    
    if has_digit:
        strength += 1
    else:
        feedback.append("🔴 Include at least one number (0-9).")
    
    if has_special:
        strength += 1
    else:
        feedback.append("🔴 Use at least one special character (!@#$%^&*).")
    
    # Strength label
    if strength <= 2:
        return "Weak", feedback
    elif strength == 3 or strength == 4:
        return "Moderate", feedback
    else:
        return "Strong", feedback

# Streamlit UI with enhanced styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 400px;
            padding: 20px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .stTextInput, .stButton {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🔐 Password Strength Meter</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your credentials to continue.</p>", unsafe_allow_html=True)

# Login Form with emojis
username = st.text_input("👤 Enter Username")
password = st.text_input("🔑 Enter Password", type="password")
login_button = st.button("🚀 Login Securely", use_container_width=True)

if login_button:
    if username and password:
        strength, feedback = check_password_strength(password)
        
        if strength == "Weak":
            st.error(f"❌ Password Strength: {strength}")
        elif strength == "Moderate":
            st.warning(f"⚠️ Password Strength: {strength}")
        else:
            st.success(f"✅ Welcome, {username}! Your password is strong.")
        
        if feedback:
            st.markdown("**🛡️ Suggestions to improve your password:**")
            for tip in feedback:
                st.markdown(f"- {tip}")
    else:
        st.warning("⚠️ Please enter both username and password.")

st.markdown("</div>", unsafe_allow_html=True)
