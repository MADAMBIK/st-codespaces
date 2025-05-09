import streamlit as st
import base64

def app():
    st.markdown("""
        <style>
            .main {
                background-color: #90EE90;
                padding: 20px;
                border-radius: 10px;
            }
            .centered-title {
                text-align: center;
                font-size: 70px;
                font-weight: bold;
            }
            .budget-green {
                color: #006400;
            }
            .tracker-black {
                color: #000000;
            }
            .section-title {
                font-size: 26px;
                color: #336699;
                margin-top: 30px;
                font-weight: bold;
            }
            .quote {
                font-style: italic;
                font-size: 18px;
                text-align: center;
                color: #333;
            }
            .bullet {
                margin-left: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Render title
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown(
        '<div class="centered-title">'
        '<span class="budget-green">Budget</span> '
        '<span class="tracker-black">Buddy</span>'
        '</div>',
        unsafe_allow_html=True
    )
    
    st.markdown("""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
        <style>
            .centered-title {
                text-align: center;
                font-size: 60px;
                font-weight: bold;
            }
            .centered-subtitle {
                text-align: center;
                font-size: 20px;
            }
            .info-box {
                padding: 15px;
                border-radius: 10px;
                border: 1px solid #ccc;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)


    st.title("Budget Tools")
    st.markdown("**Choose a category using the navigation bar on the side.**")

    # Info columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="info-box">
                <i class="bi bi-mortarboard"></i>
                <strong> Student Starter Kit</strong>
                <p>Tool tailored for new young professions.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="info-box">
                <i class="bi bi-briefcase"></i>
                <strong> Employee Kit</strong>
                <p>For tools and budgeting tailored to working professionals.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="info-box">
                <i class="bi bi-book"></i>
                <strong> Financial Education</strong>
                <p>Learn about budgeting, saving, and debt.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="info-box">
                <i class="bi bi-graph-up"></i>
                <strong> Investment 101</strong>
                <p>Get started with investing and growing wealth.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("ℹ️ Use the **navigation bar on the left** to move between pages.")

