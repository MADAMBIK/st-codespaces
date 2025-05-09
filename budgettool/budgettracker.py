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
                font-size: 70px;
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

    # Render custom title
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown(
        '<div class="centered-title">'
        '<span class="budget-green">Budget</span> '
        '<span class="tracker-black">Buddy</span>'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("INCOME")
    salary_actual = st.number_input("Salary", key="salary_a")
    grant_actual = st.number_input("Child Support/Grant", key="grant_a")
    other_income_actual = st.number_input("Other Income", key="other_a")

    income_actual = salary_actual + grant_actual + other_income_actual
    st.markdown(f"**Total Income: R {income_actual:,.2f}**")

    st.divider()

    st.subheader("FIXED COSTS")
    fixed_items = [
        "Rent / House Bond", "Vehicle Finance", "Short-term Insurance", "Medical Aid / Hospital Plan",
        "School / Crèche Fees", "Retail Store Accounts", "Cellphone Contract", "Internet Contract",
        "Magazine/Newspaper Subscriptions", "DStv", "Savings / Emergency Fund / Investments", "Gym",
        "Money for Family"
    ]

    fixed_actual = 0
    for item in fixed_items:
        fixed_actual += st.number_input(f"{item}", key=f"{item}_a")

    st.markdown(f"**Total Fixed Costs: R {fixed_actual:,.2f}**")

    st.divider()

    st.subheader("CHANGING COSTS")
    changing_items = [
        "Transport (e.g. Petrol / Taxi Fare)", "Utilities (Water and Lights)",
        "Groceries / Take-away Food", "Clothing / Clothing Accounts", "Entertainment",
        "Medication", "Cellphone Airtime (Pay-as-you-go)"
    ]

    changing_actual = 0
    for item in changing_items:
        changing_actual += st.number_input(f"{item}", key=f"{item}_a")

    st.markdown(f"**Total Changing Costs: R {changing_actual:,.2f}**")

    st.divider()

    st.subheader("OTHER EXPENSES")
    other_items = [
        "Contribution to Events (e.g. Gifts)", "Vehicle Repairs", "Haircut / Salon / Beauty Treatment",
        "Books / Newspapers / Magazines", "TV Licence Fee", "Vehicle Licence Renewal"
    ]

    other_actual = 0
    for item in other_items:
        other_actual += st.number_input(f"{item}", key=f"{item}_a")

    st.markdown(f"**Total Other Expenses: R {other_actual:,.2f}**")

    st.divider()

    # Summary
    total_expenses_actual = fixed_actual + changing_actual + other_actual
    balance = income_actual - total_expenses_actual

    st.subheader("Summary")
    st.markdown(f"**Total Income: R {income_actual:,.2f}**")
    st.markdown(f"**Total Expenses: R {total_expenses_actual:,.2f}**")
    st.markdown(f"**Surplus / Deficit: R {balance:,.2f}**")

    if balance > 0:
        st.success("✅ Great! You can save, invest, or build your emergency fund.")
    else:
        st.warning("⚠️ You're overspending. Consider reducing some expenses.")
    
    if balance > 2000:
        # excess income after budgeting to 
        
        recommended_invest = balance*0.2
        recommended_savingtowardskids = balance*0.3
        recommended_travelsaving = balance*0.5
      
       
        st.subheader("**Excess income suggestions**")
        st.markdown(f"- **Invest(35%):** R{recommended_invest:,.2f}")
        st.markdown(f"- **Saving towards kids(15%):** R{recommended_savingtowardskids:,.2f}")
        st.markdown(f"- **Travel Savings(50%):** R{recommended_travelsaving:,.2f}")
       