import streamlit as st
import random

st.set_page_config(page_title="Fighting Fantasy Character Sheet", layout="centered")

st.title("🗡️ Fighting Fantasy Character Sheet")

# Utility functions
def roll_d6(n):
    return sorted([random.randint(1, 6) for _ in range(n)])

def generate_stats(char_class):
    # Skill: median of 3d6 + 4 (Wizard) or +6 (Warrior)
    skill_roll = roll_d6(3)
    skill = skill_roll[1] + (4 if char_class == "Wizard" else 6)
    
    # Stamina: median two of 4d6 + 12
    stamina_roll = roll_d6(4)
    stamina = sum(stamina_roll[1:3]) + 12

    # Luck: median of 3d6 + 6
    luck_roll = roll_d6(3)
    luck = luck_roll[1] + 6

    return skill, stamina, luck

# --- Initialize session state ---
if "name" not in st.session_state:
    st.session_state.update({
        "name": "",
        "quest": "",
        "char_class": "Wizard",  # Renamed from "class"
        "skill_init": 0,
        "skill_curr": 0,
        "stamina_init": 0,
        "stamina_curr": 0,
        "luck_init": 0,
        "luck_curr": 0,
        "libra_call": True,
        "provisions": 0,
        "gold": 0,
        "weapon": "",
        "items": "",
        "lost_used": "",
    })

# --- Reset and Generate function ---
def reset_and_generate():
    st.session_state.name = ""
    st.session_state.quest = ""
    st.session_state.weapon = ""
    st.session_state.items = ""
    st.session_state.lost_used = ""
    st.session_state.libra_call = True
    st.session_state.provisions = 0
    st.session_state.gold = 0

    skill, stamina, luck = generate_stats(st.session_state.char_class)
    st.session_state.skill_init = skill
    st.session_state.skill_curr = skill
    st.session_state.stamina_init = stamina
    st.session_state.stamina_curr = stamina
    st.session_state.luck_init = luck
    st.session_state.luck_curr = luck

# --- UI Layout ---

st.text_input("Name", key="name")
st.text_input("Quest", key="quest")

st.selectbox("Class", ["Wizard", "Warrior"], key="char_class")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("SKILL")
    st.number_input("Initial", key="skill_init", min_value=0)
    st.number_input("Current", key="skill_curr", min_value=0)
with col2:
    st.subheader("STAMINA")
    st.number_input("Initial ", key="stamina_init", min_value=0)
    st.number_input("Current ", key="stamina_curr", min_value=0)
with col3:
    st.subheader("LUCK")
    st.number_input("Initial  ", key="luck_init", min_value=0)
    st.number_input("Current  ", key="luck_curr", min_value=0)

st.checkbox("LIBRA CALL", value=True, key="libra_call")

col4, col5 = st.columns(2)
with col4:
    st.number_input("PROVISIONS", min_value=0, step=1, key="provisions")
with col5:
    st.number_input("GOLD", min_value=0, step=1, key="gold")

st.text_input("WEAPON", key="weapon")

st.text_area("ITEMS", height=100, key="items")
st.text_area("LOST/USED", height=100, key="lost_used")

st.button("🎲 Generate New", on_click=reset_and_generate)
