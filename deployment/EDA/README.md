# Getaround Delay Analysis

## Overview
This notebook analyzes Getaround's check-in/check-out data to study vehicle return delays and evaluate the impact of implementing a minimum buffer time between consecutive rentals. The goal is to address late checkout issues while balancing potential revenue loss for owners.

## Objectives
- Study historical vehicle return delays.
- Assess the trade-off between mitigating late returns and minimizing revenue impact.
- Provide actionable insights for setting:
  - **Threshold**: Optimal duration for the minimum delay between rentals.
  - **Scope**: Whether to apply the feature to all cars or only "Connect" cars.

## Key Findings

### Dataset Insights
1. **Delay Distribution**
   - Total valid delays recorded: **16,346 rentals**.
   - Average delay: **60 minutes**, but skewed by extreme values (-22k to +71k minutes).
   - Median delay: **9 minutes** → Half of returns occur within 9 minutes or less.

### Impact of Buffer Thresholds
The analysis evaluated the number of affected rentals at different thresholds:
- **30-minute buffer**: 
  - Total impacted: **279 rentals**
  - Breakdown: **148 mobile**, **131 Connect**.
- **60-minute buffer**: 
  - Total impacted: **401 rentals**
  - Breakdown: **220 mobile**, **181 Connect**.
- **180-minute buffer**:
  - Total impacted: **870 rentals**
  - Breakdown: **498 mobile**, **372 Connect**.

### Scope of Implementation
- Apply to **all cars** (maximize problem resolution but higher revenue impact) vs.  
- Only **Connect cars** (targeted solution with lower financial risk).