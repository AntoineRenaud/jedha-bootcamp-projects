# Getaround Analysis 🚗

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Getaround_%28Europe%29.png/800px-Getaround_%28Europe%29.png)

Getaround is a peer-to-peer car rental platform, where users can rent cars for short periods. To ensure smooth rental experiences, drivers must complete a checkin and checkout flow to assess car condition, fuel levels, and mileage.  
The challenge was to address issues caused by late checkouts, which disrupt subsequent rentals.

#  Project Overview

The problem revolves around optimizing the scheduling process to **prevent conflicts due to late returns**. The solution involves **creating a dashboard**, **developing an API endpoint** with machine learning capabilities, and **providing comprehensive documentation** for ease of use.


# Approach

The objective is to analyze rental delays caused by late checkouts, which can lead to dissatisfaction for subsequent users. To mitigate this, a delay buffer between rentals is being considered, but it may impact revenue.

- **Data Analysis:** This involved identifying patterns of late returns and their effects on user satisfaction and revenue. Key metrics included the frequency of late checkouts, their duration, and subsequent impacts on car availability. 
    

- **Dashboard Development:** Create an interactive dashboard using Streamlit to visualize how different minimum delay thresholds affected various metrics such as the number of affected rentals, potential revenue loss, and user satisfaction scores.
    

- **Machine Learning Model:** To optimize pricing dynamically based on demand and availability, a machine learning model was developed. The model used historical data to predict optimal prices, factoring in time, location, and car type. An API endpoint was created to provide these predictions in real-time. 
    

- **Documentation & Hosting:** Comprehensive documentation for the API was crafted, explaining endpoints, their inputs, and outputs. This ensured that users could easily integrate the API into other systems. The application was then hosted online using Heroku, ensuring it was accessible and scalable. 
     

# Setup Instructions: 

To run this project locally: 
     

## Installation Steps 

- **Install dependencies:** 

```python
pip install -r requirements.txt
```

# URLs

* **Dashboard** : https://get-around-dashboard-b46bbe2723e8.herokuapp.com/
* **API** : https://get-around-api-7c81f90e1f50.herokuapp.com/
* **MLFLow server** : https://mlflow-server-1f00c9913525.herokuapp.com/