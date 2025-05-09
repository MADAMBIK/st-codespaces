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
    st.title("Investment Options in South Africa")
    
    st.markdown("## Risk-Free Investment Options")

    st.markdown("""
### 1. Tax Free Savings Account

| Category | Details |
|---------|---------|
| **Benefits** | No tax is payable on the interest, dividends or capital gains earned on these investments. Immediate access to capital and income. Your money grows faster. Encourages long-term investment and tax-free wealth creation. |
| **Who can help** | Your bank, an investment company or an independent financial planner. |
| **Investment Amount** | You may invest up to R30 000 per year (maximum R500 000 over your lifetime). Any amount above the annual or lifetime limit will be taxed at 40% by SARS. |
| **Risk Factor** | Very safe |
| **Tax Implications** | No tax payable unless limits are exceeded. |

---

### 2. Call Accounts

| Category | Details |
|---------|---------|
| **Benefits** | You can deposit or withdraw funds at any time without penalties. Interest is earned daily and paid monthly. Higher interest is earned the higher the balance. Compound interest is earned (interest is paid on interest). |
| **Who can help** | Speak to someone at your bank. |
| **Investment Amount** | Usually, a minimum deposit is required. |
| **Risk Factor** | Very low risk. |
| **Tax Implications** | Interest earned is taxable and must be declared to SARS. |

---

### 3. Fixed-Term Deposits

| Category | Details |
|---------|---------|
| **Benefits** | You invest a fixed amount of money for a fixed period of time. You are guaranteed a fixed return on your investment. You know in advance what your investment will be worth at the end of the period. |
| **Who can help** | Speak to someone at your bank. |
| **Investment Amount** | Usually, a minimum deposit is required. You cannot add more funds to your investment. |
| **Risk Factor** | Low risk, but poor protection against inflation. Penalties for early withdrawals. |
| **Tax Implications** | Interest earned is taxable and must be declared to SARS. |

---

### 4. Notice Deposits

| Category | Details |
|---------|---------|
| **Benefits** | Interest is earned daily and paid monthly. Tiered interest rates. The higher your balance, the more interest you earn. Interest is reinvested, earning compound interest. To access funds, a 7 to 32-day notice is required. |
| **Who can help** | Speak to someone at your bank. |
| **Investment Amount** | Usually, a minimum deposit is required. Additional deposits may be made. |
| **Risk Factor** | Low risk. |
| **Tax Implications** | Interest earned is taxable and must be declared to SARS. |

---

### 5. Money Market Funds

| Category | Details |
|---------|---------|
| **Benefits** | Pooled fund professionally managed to provide interest income and capital protection. Earn a higher return than with a bank savings account. Funds are available within 24 hours of withdrawal request. |
| **Who can help** | Unit trust companies, financial advisors, banks, online investment platforms. |
| **Investment Amount** | Minimum lump sum investment or debit-order contribution required. |
| **Risk Factor** | Low risk. |
| **Tax Implications** | Interest earned is taxable and must be declared to SARS. |
""")

    st.markdown("## Medium to High Risk Investments")

    st.markdown("""
### 1. Stocks / Shares

Represent part ownership in a company listed on the JSE. As a shareholder, you may receive dividends and benefit from a rising share price. The value of your investment may decrease depending on the company’s performance and overall stock market conditions. Suitable for investors with a high risk appetite and long-term goals.

---

### 2. Exchange-Traded Funds (ETFs)

Listed investment products that track the performance of a group of shares (index), such as the FTSE/JSE Top 40. You are investing in a diversified basket of shares, which reduces risk compared to individual stocks. ETFs can be traded on the JSE like shares. Costs are lower than actively managed funds.

---

### 3. Bonds

Issued by government or corporations to raise funds. When you buy a bond, you are lending money in exchange for interest payments over a fixed term. Government bonds are low risk. Corporate bonds carry higher risk, but potentially higher returns. Bonds are suitable for income-seeking investors.

---

### 4. Collective Investment Schemes (CIS)

Pooled investments managed by professionals. Funds are spread across a variety of assets such as stocks, bonds, and property. Investors benefit from diversification and professional management. Examples: unit trusts, mutual funds. Risk varies based on fund allocation.

---

### 5. Participation Mortgage Bond Scheme

Investors pool funds to lend to property developers. The mortgage bond is registered over the property as security. Investors earn interest on the loan. Risk depends on property market conditions and borrower repayment ability.

---

### 6. Derivatives

Contracts whose value is derived from an underlying asset (e.g. shares, indices, currencies, commodities). Examples include options, futures, CFDs. Used for hedging or speculative purposes. High risk due to leverage and complexity. Suitable for advanced investors.
""")

