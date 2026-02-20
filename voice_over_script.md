Floods are among the most frequent and devastating natural disasters, causing massive loss of life and property every year. Predicting them accurately and well in advance is crucial for disaster management and saving lives.

Welcome to the demonstration of our 'Smart Flood Prediction System'. This project leverages Machine Learning to predict the probability of floods based on various weather and climate parameters.

Traditional methods of flood forecasting often struggle with the complexity of changing weather patterns. Our solution aims to bridge this gap by analyzing historical data to identify patterns that lead to flooding.

We have built a robust web application that allows users to input real-time weather data and instantly get a prediction on whether a flood involves a risk.

Let's dive into the technical details. We started with a comprehensive dataset containing historical records of weather conditions.

The key features used for prediction include: Temperature and Humidity, Cloud Cover, Annual Rainfall, And seasonal rainfall data across different months like January-February, March-May, and the Monsoon season.

For the core logic, we utilized Python and the Scikit-Learn library. We implemented multiple Machine Learning algorithms, including Logistic Regression, K-Nearest Neighbors, Decision Trees, and Random Forest.

After training and testing, the model with the highest accuracy was selected and saved to power our application.

To make this model accessible, we developed a user-friendly web interface using the Flask framework.

Here on the home page, the user can navigate to the prediction section.

The user enters the required parameters such as the current Temperature, Humidity, Cloud Cover, and Rainfall statistics for the region.

Once the data is submitted, the backend processes the input, scales it to match our training data, and passes it through the trained model.

And there we have it! The system analyzes the inputs and immediately alerts the user if there is a high chance of flooding...

...or confirms if the situation is safe.

In conclusion, this Flood Prediction System demonstrates how Machine Learning can be effectively applied to real-world problems. By providing timely alerts, it empowers authorities and individuals to take necessary precautions.

Thank you for watching.
