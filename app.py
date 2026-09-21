import streamlit as st
import joblib

st.set_page_config(
    page_title="Warehouse Robot RL",
    page_icon="🤖"
)

st.title("🤖 Smart Warehouse Robot")
st.write("Q-Learning based Reinforcement Learning Application")

Q = joblib.load("warehouse_robot_q_table.pkl")

actions = {
    0: "LEFT",
    1: "RIGHT",
    2: "UP",
    3: "DOWN"
}

state = st.selectbox(
    "Select the robot's current State:",
    list(range(16))
)

st.write(f"### Current State: {state}")

if st.button("Find Best Action"):

    best_action_number = int(Q[state].argmax())

    best_action = actions[best_action_number]

    st.subheader("Q-Values")

    st.write(f"LEFT   : {Q[state][0]:.2f}")
    st.write(f"RIGHT  : {Q[state][1]:.2f}")
    st.write(f"UP     : {Q[state][2]:.2f}")
    st.write(f"DOWN   : {Q[state][3]:.2f}")

    st.subheader("Best Action")

    st.success(f"Best Action: {best_action}")

    st.info(f"The robot should move {best_action}.")
