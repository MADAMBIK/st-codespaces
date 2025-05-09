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
    st.markdown('<div class="centered-subtitle">Plan your monthly student budget smartly</div><br>', unsafe_allow_html=True)

  
    st.info("Please use the navigation bar on the left to switch to other budgeting tools.")


    income = st.number_input("💰 **Enter your expected monthly income (Rands):**", min_value=0)


    RENT_CAP = 7000
    FOOD_CAP = 2500
    TRANSPORT_COST = 2000
    PRIME_INTEREST_RATE = 0.11  # Annual
    CAR_TERM_MONTHS = 72
    MAX_CAR_VALUE = 300000
    INSURANCE_COST = 1000

    if income > 0:
        # Budget Allocations
        recommended_rent = min(income * 0.3, RENT_CAP)
        recommended_food = min(income * 0.2, FOOD_CAP)
        transport_cost = TRANSPORT_COST
        savings = income * 0.2
        wants = income * 0.1
        essentials_total = recommended_rent + recommended_food + transport_cost
        total_outflow = essentials_total + savings + wants
        remaining = income - total_outflow

        st.subheader("**Budget Allocation**")
        st.markdown(f"- **Rent (30%, capped at R7,000):** R{recommended_rent:,.2f}")
        st.markdown(f"- **Food (20%, capped at R2,500):** R{recommended_food:,.2f}")
        st.markdown(f"- **Transport (Fixed):** R{transport_cost:,.2f}")
        st.markdown(f"- **Savings (20%):** R{savings:,.2f}")
        st.markdown(f"- **Wants (10%):** R{wants:,.2f}")
        st.markdown(f"**Remaining Funds:** R{remaining:,.2f}")

       
        st.subheader("🚗 **Car Affordability**")
        if remaining >= 3000:
            r = PRIME_INTEREST_RATE / 12
            n = CAR_TERM_MONTHS
            max_payment = remaining * 0.6
            car_value = max_payment * ((1 - (1 + r) ** -n) / r)
            car_value = min(car_value, MAX_CAR_VALUE)
            monthly_payment = car_value * (r / (1 - (1 + r) ** -n))
            total_monthly_car_cost = monthly_payment + INSURANCE_COST
            leftover = remaining - total_monthly_car_cost

            st.markdown(f"- ✅ Affordable Car Value: **R{car_value:,.2f}**")
            st.markdown(f"- Estimated Monthly Payment: **R{monthly_payment:,.2f}**")
            st.markdown(f"- Insurance: **R{INSURANCE_COST:,.2f}**")
            st.markdown(f"- Left for Investment: **R{leftover:,.2f}**")
        else:
            leftover = remaining
            st.warning("⚠️ Not enough remaining funds to afford a car.")

     
        st.subheader("📈 Suggested Investment")
        if leftover > 0:
            st.markdown(f"- Consider investing **R{leftover:,.2f}** for your future goals.")
        else:
            st.markdown("- No leftover funds to invest at this stage.")




