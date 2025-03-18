import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_excel('src/get_around_delay_analysis.xlsx')


# Streamlit app title
st.title('Get Around Analysis')

# Display the dataset summary
st.subheader('Dataset Summary')
st.write(df.describe(include='all'))

# Display missing value percentages
st.subheader('Missing Value Percentage')
missing_percentage = df.isnull().sum() / len(df) * 100
st.write(missing_percentage)

st.markdown('Feature description : \n\
- **rental_id**: Unique identifier for each rental.\n \
- **car_id**: Identifier for the car being rented.\n\
- **checkin_type**: Either "mobile" or "connect", referring to how the check-in process was handled.\n\
- **state**: The state of the rental (e.g., "ended", "canceled").\n\
- **delay_at_checkout_in_minutes**: The delay in minutes at checkout (how late the car was returned).\n\
- **previous_ended_rental_id**: The rental ID of the previous rental for that car.\n\
- **time_delta_with_previous_rental_in_minutes**: The time difference between the end of the previous rental and the start of the current one (in minutes).\n')

# Calculate and display the percentage of late users
st.subheader('Late Users Statistics')
late_users = len(df.loc[df['delay_at_checkout_in_minutes'] > 0])
total_users = len(df)
late_user_ratio = late_users / total_users * 100
st.write(f'Total users: {total_users}')
st.write(f'Late users: {late_users}')

st.write('On 21 310 users,  **9404** where **late**.\n \
It represents an amount of **44,1%** of total users.')

# Calculate and display delay at checkout information
st.subheader('Delay at Checkout Statistics')
st.write(df['delay_at_checkout_in_minutes'].describe())

st.write('Out of the dataset, there are 16,346 rentals with a valid delay time (not NaN).')
st.write('But some of them are **negative**, so we can assume that those values correspond \
         to people who **returned their vehicles earlier** than expected.')
st.write('The average delay is about **60** minutes, but this statistic is **skewed** by **extreme values** \
    (with a minimum delay of -22,433 minutes and a maximum of 71,084 minutes).')
st.write('The median delay is only **9** minutes, meaning half of the rentals are delayed by 9 minutes or less.')

# Check-in type and state distribution plot
st.subheader('Check-in Type and State Distribution')

# Group the data for plotting
checkin_type_and_state = df.groupby(['checkin_type', 'state']).size()

# Create subplots for Connect and Mobile users
fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=('Connect users', 'Mobile users'))

fig.add_trace(go.Bar(
    x=df['state'].unique(),
    y=checkin_type_and_state['connect'],
    name='Connect',
    text=checkin_type_and_state['connect'],
    textposition='auto',
), row=1, col=1)

fig.add_trace(go.Bar(
    x=df['state'].unique(),
    y=checkin_type_and_state['mobile'],
    name='Mobile',
    text=checkin_type_and_state['mobile'],
    textposition='auto'
), row=1, col=2)

fig.update_layout(height=800, width=800, title_text='Check-in Type and State Distribution')
st.plotly_chart(fig)


connect_users = df[df['checkin_type'] == 'connect']
connect_users_ratio = len(connect_users)/total_users*100
st.write(f"Connect users represents {connect_users_ratio:0.1f} % of the total users")



# Threshold analysis
st.subheader('Threshold Impact on Rentals')
thresholds = [x for x in range(0, 750, 30)]

# Perform threshold impact analysis
results = []
for threshold in thresholds:
    impacted_rentals = df[(df['time_delta_with_previous_rental_in_minutes'] < threshold) &
                          (df['time_delta_with_previous_rental_in_minutes'].notna())]
    mobile_affected = impacted_rentals[impacted_rentals['checkin_type'] == 'mobile'].shape[0]
    connect_affected = impacted_rentals[impacted_rentals['checkin_type'] == 'connect'].shape[0]
    results.append({
        'Threshold (minutes)': threshold,
        'Total Affected Rentals': impacted_rentals.shape[0],
        'Mobile Affected Rentals': mobile_affected,
        'Connect Affected Rentals': connect_affected
    })

df_results = pd.DataFrame(results)

# Display the threshold analysis table
st.write('Threshold Impact Table')
st.write(df_results)

# Plot the threshold impact on rentals
st.subheader('Threshold Impact on Rentals Plot')
line_trace = go.Scatter(
    x=thresholds, 
    y=df_results['Total Affected Rentals'], 
    mode='lines+markers', 
    name='Total Affected Rentals',
    line=dict(color='blue', width=2)
)

bar_mobile = go.Bar(
    x=thresholds, 
    y=df_results['Mobile Affected Rentals'], 
    name='Mobile Affected Rentals',
    marker_color='orange',
    width=12
)

bar_connect = go.Bar(
    x=thresholds, 
    y=df_results['Connect Affected Rentals'], 
    name='Connect Affected Rentals',
    marker_color='green',
    width=12
)

# Combine traces into one figure
fig = go.Figure()
fig.add_trace(line_trace)
fig.add_trace(bar_mobile)
fig.add_trace(bar_connect)

fig.update_layout(
    barmode='group',
    title='Threshold Impact on Rentals',
    xaxis_title='Threshold (minutes)',
    yaxis_title='Affected Rentals',
    legend=dict(x=0.1, y=1.1, orientation='h'),
    height=600,
    width=900
)

# Display the plot in Streamlit
st.plotly_chart(fig)

st.write('- At **30** minutes, **279** **rentals** would be affected, with **148** **mobile** rentals and **131** **connect** rentals. \n\
- At **60** minutes, **401** **rentals** would be impacted, with **220** **mobile** and **181** **connect** rentals. \n\
- At **180** minutes, **870** **rentals** would be impacted, with **498** **mobile** and **372** **connect** rentals.\n \
This plot can help guide decisions on setting the buffer threshold and whether it should apply to all cars or only "connect" cars.')
