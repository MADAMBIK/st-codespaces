import streamlit as st
import base64

def app():
    # Convert image to base64
    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    img_generated = get_base64_image("image1.jpg")

    st.markdown(
        f"""
        <div style='margin-top:30px; width:100%; height:300px;
                    background-image: url("data:image/jpg;base64,{img_generated}");
                    background-size: contain;
                    background-repeat: no-repeat;
                    background-position: center;
                    opacity: 0.4;'>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
        <style>
            .main {
                background-color: #90EE90;
                padding: 20px;
                border-radius: 10px;
            }
            .centered-title {
                text-align: center;
                font-size: 100px;
                font-weight: bold;
            }
            .budget-green {
                color: #006400;
            }
            .buddy-black {
                color: #000000;
            }
            .centered-subtitle {
                text-align: center;
                color: #336699;
                font-size: 24px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown(
        '<div class="centered-title">'
        '<span class="budget-green">Budget</span> '
        '<span class="buddy-black">Buddy</span>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="centered-subtitle">Your Companion for Smarter Budgeting and Investing</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size: 18px; padding: 10px 30px;'>
    Welcome to <strong>Budget Buddy</strong>, a streamlined personal finance platform designed to help individuals and families take control of their financial lives. Whether you're managing your first salary, navigating family expenses, or planning to invest or for retirement, Budget Buddy equips you with financial educational tools and reliable guidance.
    </div>
    """, unsafe_allow_html=True)


