# AT&T Spam Detector 🕵️‍♀️ 
![AT&T Logo](https://upload.wikimedia.org/wikipedia/fr/4/43/Logo_AT%26T.svg)

## Overview
**AT&T** Inc., a US global telecommunications leader, seeks an **automated solution to combat SPAM messages** for its users. **This project** addresses this pain point by **developing a deep learning model** capable of detecting spam SMS based solely on message content.

## Project Goals
Build an **automated SPAM detector** that:  
- Processes SMS text content in real-time  
- Flags messages as "spam" or "ham" with high accuracy  

## Dataset
The dataset used for this project is located in the `src/` directory:
- `spam.csv`: Contains labeled SMS messages classified as "spam" or "ham".

## Approach
### 1. Exploratory Data Analysis (EDA)
- Analyze the dataset to understand the distribution of spam and ham messages.

### 2. Data Preprocessing
- Normalize text data by converting to lowercase and tokenizing.
- Encode labels and split the dataset into training and testing sets.

### 3. Model Development
- **Baseline Model**: Implement a Recurrent Neural Network (RNN) for sequence analysis.
- **Improved Model**: Develop an LSTM-based network to capture long-term dependencies and improve performance.

### 4. Model Evaluation
- Evaluate models and compare the performance of the baseline and improved models.

## Setup & Installation

Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
Run the Jupyter notebook:
   ```sh
   jupyter notebook spam-detector.ipynb
   ```
