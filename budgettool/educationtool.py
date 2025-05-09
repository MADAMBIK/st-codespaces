import streamlit as st

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
                font-size: 64px;
                font-weight: bold;
            }
            .budget-green {
                color: #006400;
            }
            .tracker-black {
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
        '<span class="tracker-black">Buddy</span>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown("**This guide will help you understand money and finance in South Africa in a simple way.**")

    # BUDGETING
    with st.expander("**BUDGETING**"):
        st.subheader("What is budgeting and why is it important?")
        st.write("""
        Budgeting is like planning how you will spend your pocket money.
        If you get R100 a week, you decide how much goes to snacks, transport, savings, etc.
        
        **Why it's important:**
        - You don’t run out of money before month-end
        - You can plan for future things like clothes or a birthday
        """)
        st.markdown("**Example**")
        st.code("""
Income: R1,000
Needs (60%) = R600
Wants (30%) = R300
Savings (10%) = R100
        """)

    # SAVING
    with st.expander("**SAVING**"):
        st.subheader("What is the importance of saving?")
        st.write("""
        Saving is like putting money in a jar for when you really need it — like when your phone breaks or for school shoes.

        **Why save?**
        - Emergency needs
        - To reach goals (like a laptop)
        - Peace of mind
        """)
        st.markdown("**Tip**: Start small. Even R10 a week helps!")

    # CREDIT SCORE
    with st.expander("**CREDIT SCORE**"):
        st.subheader("Learn more on Credit Score")
        st.markdown("""
A credit score is a three-digit number used by lenders to determine whether you qualify for credit, such as a loan or credit card.

### Who calculates your credit score?
In South Africa, credit bureaus include:
- **Experian**
- **TransUnion**
- **Compuscan**
- **XDS**

### Experian Score Bands

| Credit Score | Band         | Description              |
|--------------|--------------|--------------------------|
| 0 - 599      | Very Poor    | Let’s start climbing     |
| 599 - 615    | Poor         | On the up                |
| 616 - 633    | Fair         | On good ground           |
| 634 - 657    | Good         | Looking bright           |
| 658 - 740    | Excellent    | Soaring high             |

### What affects your credit score?

| Factor                          | Explanation                                  |
|---------------------------------|----------------------------------------------|
| Missed payments                 | Indicates you may miss future payments       |
| Judgments, bankruptcy           | Shows poor financial management              |
| Too many credit applications    | Looks risky to lenders                       |
| Unused high credit limits       | Potential to accumulate debt                 |
| Frequent address changes        | May signal instability                       |
| Report errors                   | Can reduce your score – fix mistakes         |

**To improve your score:** Pay on time, keep debt low, check your report.

**High score =** lower risk, better loan terms.  
**Low score =** higher risk, costly loans.
        """)

    # INTEREST RATES
    with st.expander("**INTEREST RATES**"):
        st.subheader("2 Types of Interest Rates")
        st.markdown("""
### What is an Interest Rate?

Interest is money **you earn** when saving or **pay** when borrowing.

- Expressed as a **% per year**
- Can be **fixed** or **variable**

---

### Simple Interest vs Compound Interest

| Type             | Description                                  | Example                                                    |
|------------------|----------------------------------------------|------------------------------------------------------------|
| Simple Interest  | Earn on original amount only                 | Year 1: R1000 × 10% = R100 → R1100                         |
|                  |                                              | Year 2: R1000 × 10% = R100 → R1200                         |
| Compound Interest| Earn interest on interest too               | Year 1: R1000 × 10% = R100 → R1100                         |
|                  |                                              | Year 2: R1100 × 10% = R110 → R1210                         |
|                  |                                              | Year 3: R1210 × 10% = R121 → R1331                         |

---

### Compound Interest Tips:
- Start early
- Reinvest gains
- Stay invested
        """)

    # BANK ACCOUNTS
    with st.expander("**BANK ACCOUNTS**"):
        st.subheader("2 Types of Bank Accounts")
        st.markdown("""
Most people use a **cheque** or **savings** account.

### Comparison:

| Feature                  | Cheque Account                            | Savings Account                         |
|--------------------------|-------------------------------------------|------------------------------------------|
| Purpose                  | Daily use                                 | Saving                                   |
| Interest Rate            | Low                                       | Higher                                   |
| Requirements             | Minimum balance/income                    | Open to all                              |
| Monthly Fees             | Usually has monthly fees                  | Charges per transaction                  |
| Features                 | Free swipes, SMS alerts, online banking   | Few extra features                       |
| Best Use                 | Regular payments                          | Growing money                            |

**Tip:** Use cheque accounts to spend, savings accounts to grow.
        """)

    # LOANS
    with st.expander("**TYPES OF LOANS & RISKS**"):
        st.subheader("Borrowing Money You’ll Pay Back With Extra")
        st.markdown("""
### Types of Loans:

- **Personal loan** – for anything like emergencies (high interest)
- **Car loan** – for buying a car (medium interest)
- **Home loan** – for property (low interest, long-term)
- **Student loan** – for university studies

### Risks:

| Risk                      | Why It Matters                          |
|---------------------------|------------------------------------------|
| High interest             | Makes loans expensive                    |
| Missed payments           | Hurts credit score                       |
| Debt trap                 | Borrowing more to repay old debt         |
| Asset repossession        | Car or house may be taken away           |

**Tip:** Only borrow what you need and can afford to repay.
        """)

    with st.expander("**INSURANCE**"):
        st.subheader("What is insurance and why do we need it?")
        st.write("Insurance is a way of protecting yourself financially against unexpected events. You pay a small amount regularly (a premium) and the insurance company helps cover large costs when something goes wrong.")
        st.write("Types of insurance:")
        st.write("- Car insurance – covers damage or theft of your vehicle")
        st.write("- Health insurance/Medical aid – helps cover doctor or hospital bills")
        st.write("- Life insurance – pays your family money if you pass away")
        st.write("Why is insurance important?")
        st.write("It prevents financial stress by helping you pay for big, unexpected expenses.")

    with st.expander("**TAX, VAT & SARS**"):
        st.subheader("What is tax?")
        st.write("Tax is money that people and businesses must pay to the government. This money is used by the government to build infrastructure like roads and schools, pay salaries of government workers like teachers and police, and support social grants.")
        st.subheader("What is VAT?")
        st.write("VAT stands for Value Added Tax. It is a tax added to most goods and services you buy. In South Africa, the standard VAT rate is 15%. Some items like basic food (e.g. bread, milk) are VAT-free to help poor households.")
        st.subheader("What is SARS?")
        st.write("SARS stands for the South African Revenue Service. This is the government agency that collects taxes in South Africa. They make sure people and businesses pay the right amount of tax.")

        

    st.markdown("</div>", unsafe_allow_html=True)

