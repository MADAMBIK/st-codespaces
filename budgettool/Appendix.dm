## Appendix

import streamlit as st

st.markdown("## Appendix B: Budget-Buddy Proposal")

st.markdown("""
### **Introduction**

South Africa is among the most developed countries on the African continent and continues to experience rapid growth in the financial technology (fintech) sector. There is a wide range of fintech solutions currently active in banking, financial markets, and insurance (e.g., Naked Insurance). However, despite the expansion of such platforms, many South Africans still struggle with fundamental financial literacy. As a result, a significant portion of the population lacks knowledge in essential areas such as financial planning, budgeting, and basic investment strategies.

This gap in financial understanding has led to widespread issues, including high levels of personal debt, low credit scores, and reduced access to credit. Consequently, many individuals miss opportunities for financial growth and capital expansion. The lack of financial literacy also contributes to underinvestment in financial markets, limited retirement savings, and increased dependency on government support. Alarmingly, these challenges affect not only older generations but also the youth—many of whom enter the workforce unprepared to make sound financial decisions.

---

### **Proposed Solution: Budget-Buddy**

Given the widespread use of smartphones, computers, and tablets in South Africa, coupled with easy access to Wi-Fi in public spaces such as cafes, universities, workplaces, and malls, a digital solution can address these challenges effectively. **Budget-Buddy** is proposed as a lightweight, secure, and accessible web-based application designed to promote financial literacy, assist in personal budgeting, and introduce users to basic investing principles.

The application is intended to empower users—especially graduates and young professionals—with the knowledge and tools needed to manage their finances effectively and plan for the future. It will not require the submission of personal identifying information, ensuring privacy and data security.

---

### **Key Features**

- **Interactive Budgeting Tool:** Helps users manage income and expenses, set financial goals, and build savings.
    
- **Real-Time Investment Guidance:** Provides up-to-date information and personalized suggestions on how to allocate surplus funds.
    
- **Investment Education:** Includes beginner-friendly explanations of basic investment concepts, terminology, and strategies.
    
- **Financial Planning Module:** Offers templates and guidelines for short- and long-term financial planning.
    
- **Terminology Library:** Covers essential financial and accounting terms to enhance users' understanding.
    
- **User Segmentation:** Tailored content and tools for different user groups, including singles, married individuals, students, graduates, working professionals, retirees, and learners.
    
- **Low Data Usage:** Designed to function with minimal data requirements; some features may be made available offline.
    
- **Security and Privacy:** No collection of sensitive personal information, ensuring user privacy and data safety.
""")

st.markdown("""
### 1. Financial Literacy in South Africa

**The Hidden Crisis: How Financial Illiteracy is Crippling South Africa's Economy**  
*By: Harry Scherzer*  
- A survey by FSCA and HSRC found that only 51% of South Africans are financially literate.  
- The country had a household debt-to-income ratio of 62.4% in 2023.  
- South Africa has one of the lowest savings rates globally, estimated at 0.13% of GDP in 2022.  
- Financial illiteracy leads to poor financial decisions and reduced revenue efficiency for businesses.

---

### 2. Understanding Financial Literacy and the Two-Pot System

**Understanding Financial Literacy in South Africa: The Impact of the New Two-Pot System**  
*Staff Reporter*  
- 40% of South Africans earning above R15 000 do not know the difference between gross and net income.  
- Vulnerable groups (women, black South Africans, those without matric, youth) exhibit lower financial literacy.  
- 70% of South Africans lack a household budget.  
- 75% are unaware of the high cost of credit cards, and 65% lack long-term financial goals.

---

### 3. Youth Financial Literacy and Mismanagement

**More Than 50% of South African Youth Struggle with Financial Management**  
*Youth Generational Wealth Survey by 1Life Insurance*  
- Fewer than 30% of youth have a solid monthly budget.  
- 45% get financial information from social media.  
- Only 18% have disability cover, and 13% have critical illness cover.  
- 70% of disposable income is spent on entertainment, fashion, and dining out.

---

### 4. Debt and Credit Challenges

**Debt Crisis Deepens: South Africans Using Up to 75% of Income to Repay Debt**  
*DebtBusters’ Debt Index, Q4 2024*  
- 82% of new debt counselling applicants have personal loans; 52% have payday loans.  
- High earners (R35 000+) spend 74% of income on debt; low earners (R5 000 or less) spend 75%.  
- Unsecured debt for high earners has increased by 60% since 2016.
""")

**A. File Descriptions:**

- `budgettracker.py`: Contains logic for calculating investment, savings, and travel recommendations and it is mainly budgeting especially for an individual with a monthly income.
- `homepage.py`: it is a welcome page, contains explanations of the whole web app.
- `Student.py`: Handles student-specific budgeting logic, for those that have no idea on how to go around on their monthly expenses based on their incomes.
- `budgetpage.py` : it is more like a navigation on the budget tools that are in the app.
- `Descriptions.py` : it explains the whole idea of budgeting, saving and investing.
- `educationtool.py` : it contains markdowns of most financial content in SA that are essential to strive.
- `Investment101.py` : it contains low-high risk investment products and their explanations, mostly are banking investment products which are good to start with.
- `main.py` : it mostly for the navigation around the app, with the use of streamlit option-menu.

**B. Sample Input:**
-it is mostly incomes and expenses values.

**C. Output Screenshot:**
![screenshot](budgetkit.png)
![screenshot](educationallessons.png)
![screenshot](starterkit.png)



**D. Dependencies:**
- Python 3.10+
- Streamlit 1.x
