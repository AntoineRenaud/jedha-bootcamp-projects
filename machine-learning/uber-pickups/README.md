# Uber pickups

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Uber_logo_2018.svg/320px-Uber_logo_2018.svg.png)

This project aims to **optimize Uber's operations** by identifying "**hot zones**" — areas where drivers should be located to maximize **pickup efficiency** and customer satisfaction. The use of historical data will help to develop an algorithm that detects clusters of high-demand locations.

## Project Overview

Uber faces challenges in efficiently matching drivers with riders, leading to longer wait times for customers. This project seeks to address this issue by identifying optimal locations (hot zones) where drivers should be positioned based on historical pickup patterns. 

- Develop an **unsupervised machine learning** algorithm to **detect clusters** of high-demand areas.
- **Visualize** these clusters on an **interactive map** using tools like Plotly.
     
      
## Dataset Description

The dataset contains information about pickup times and locations in New York City. The features include:  

- **Date/Time:** The timestamp of the record.
- **Lat & Long:** Geographic coordinates representing pickup locations (latitude and longitude).
- **Base:** An identifier for the driver’s operational hub.

## Approach 

- **Clustering Algorithms:** Utilize KMeans and DBScan to group pickup locations into clusters representing hot zones.
- **Visualization:** Use Plotly to create interactive maps that display the identified hot zones, showing how they change throughout the day and week.


## How to Run This Project

1. Install the required dependencies:

```python
pip install -r requirements.txt
```
2. Run the jupyter notebook