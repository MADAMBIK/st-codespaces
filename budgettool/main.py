# main.py
import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar navigation bar
with st.sidebar:
    selected = option_menu(
        "Budget Buddy",
        ["Homepage", "Description", "Budget Tools", "Starter Kit", "Budget Kit", "Financial Lessons", "Investment 101"],
        icons=["house", "file-text", "calculator", "book", "briefcase", "mortarboard", "graph-up"],
        menu_icon="cast",
        default_index=0
    )

# Dynamically import and run selected page
if selected == "Homepage":
    import homepage
    homepage.app()

elif selected == "Description":
    import Description
    Description.app()

elif selected == "Budget Tools":
    import budgetpage
    budgetpage.app()

elif selected == "Starter Kit":
    import Student
    Student.app()

elif selected == "Budget Kit":
    import budgettracker
    budgettracker.app()

elif selected == "Financial Lessons":
    import educationtool
    educationtool.app()

elif selected == "Investment 101":
    import Investment101
    Investment101.app()

