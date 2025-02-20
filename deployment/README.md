# block5-deployment

## Getaround Analysis Dashboard
###  Overview

### Context
Getaround is a peer-to-peer car rental platform, where users can rent cars for short periods. To ensure smooth rental experiences, drivers must complete a checkin and checkout flow to assess car condition, fuel levels, and mileage. Rentals occur through three methods: mobile agreements, Connect (keyless), and paper contracts (minimal).

### Project Goal
The objective is to analyze rental delays caused by late checkouts, which can lead to dissatisfaction for subsequent users. To mitigate this, a delay buffer between rentals is being considered, but it may impact revenue. The Product Manager must determine:

Threshold: How long should the minimum delay between rentals be?
Scope: Should it apply to all cars or only Connect cars?

Key analysis points include:

Impact on owner revenue based on delay thresholds.
Number of affected rentals.
Frequency of late checkouts and their effect on the next driver.
Problematic cases solved by the delay feature.

### URLs

* **Dashboard** : https://get-around-dashboard-b46bbe2723e8.herokuapp.com/
* **API** : https://get-around-api-7c81f90e1f50.herokuapp.com/
* **MLFLow server** : https://mlflow-server-1f00c9913525.herokuapp.com/