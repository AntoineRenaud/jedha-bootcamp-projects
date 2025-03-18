import streamlit as st

# Page Title
st.title("Getaround Analysis Dashboard 🚗")

# Overview Section
st.header("Overview")
st.write("""
**Context**  
Getaround is a peer-to-peer car rental platform, where users can rent cars for short periods. To ensure smooth rental experiences, drivers must complete a checkin and checkout flow to assess car condition, fuel levels, and mileage. Rentals occur through three methods: mobile agreements, Connect (keyless), and paper contracts (minimal).

**Project Goal 🎯**  
The objective is to analyze rental delays caused by late checkouts, which can lead to dissatisfaction for subsequent users. To mitigate this, a delay buffer between rentals is being considered, but it may impact revenue. The Product Manager must determine:

- **Threshold**: How long should the minimum delay between rentals be?
- **Scope**: Should it apply to all cars or only Connect cars?

Key analysis points include:

- Impact on owner revenue based on delay thresholds.
- Number of affected rentals.
- Frequency of late checkouts and their effect on the next driver.
- Problematic cases solved by the delay feature.
""")

# Deliverables Section
st.header("Deliverables")
st.write("""
- A **dashboard** to provide insights for decision-making.
- A **/predict API endpoint** for price optimization using machine learning.
- A **documentation page** detailing API endpoints.
""")
