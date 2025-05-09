import streamlit as st

def app():
    # Custom page styling
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
    st.markdown('</div>', unsafe_allow_html=True)

    # Quote
    st.markdown('<p class="quote">“A budget is telling your money where to go instead of asking where it went.”<br>— Dave Ramsey</p>', unsafe_allow_html=True)

    # Content sections
    st.markdown('<div class="section-title">Why Budget?</div>', unsafe_allow_html=True)
    st.markdown("""
    Setting financial goals helps you decide what you want to achieve — whether it’s:
    - Short-term (e.g., paying off debt or saving for a car), or  
    - Long-term (e.g., paying off a bond or saving for retirement).  

    Because life doesn’t always go as planned, staying flexible and reviewing your goals regularly is essential.
    """)

    st.markdown('<div class="section-title">Benefits of Keeping a Budget</div>', unsafe_allow_html=True)
    st.markdown("""
    - Make long- and short-term financial plans  
    - Get the most value from your money  
    - Prepare for major life or financial changes  
    - Enjoy peace of mind by reaching your goals
    """)

    st.markdown('<div class="section-title">How to Track Your Spending</div>', unsafe_allow_html=True)
    st.markdown("""
    - Carry a notebook or use a phone app to **record every purchase** — even small ones  
    - Transfer notes to a spreadsheet like **Excel** regularly  
    - **Save receipts** to ensure you capture minor expenses  
    - Don’t rely only on bank statements — they can hide fees or vague descriptions
    """)

    st.markdown('<div class="section-title">Budgeting Tips</div>', unsafe_allow_html=True)
    st.markdown("""
    1. **Control Your Spending**  
       If you didn’t plan the purchase, wait 24 hours. Ask: *Do I need it or just want it?*

    2. **Track Every Purchase**  
       Small items add up. Keep receipts, and account for card fees and interest too.

    3. **Update Often**  
       Daily or weekly tracking helps you stay aligned with your goals.
    """)

    st.markdown('<div class="section-title">Did You Know?</div>', unsafe_allow_html=True)
    st.markdown("""
    South Africans are known for **spending more than saving**.  
    This app is designed to help shift that mindset by teaching you to **manage your income wisely** and **live within your means**.
    """)

    st.markdown('<div class="section-title">This Guide Is for You If You...</div>', unsafe_allow_html=True)
    st.markdown("""
    - Have an income  
    - First time earner
    - Use formal or informal financial services  
    - Want to **spend less than you earn**  
    - Aim to **grow your savings and financial stability**
    """)

    st.markdown('<div class="section-title">What You’ll Learn with Budget Buddy</div>', unsafe_allow_html=True)
    st.markdown("""
    - Building good financial habits and setting goals  
    - Understanding how interest affects you  
    - Understanding financial planning  
    - Exploring banking and investment products  
    - Learning about insurance and retirement planning  
    - Drawing up a will (future-update)  
    - Knowing your investor rights (future-update)  
    - Filing a financial complaint (future-update)
    """)
