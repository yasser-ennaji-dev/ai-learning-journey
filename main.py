import numpy as np 
from sklearn.linear_model import LinearRegression

# Training data: [distance_km, traffic_level]
X = np.array([
    [2, 3],
    [5, 4],
    [3, 8],
    [8, 2],
    [10, 9],
    [4, 5]
])

# Target: delivery time in minutes
y = np.array([15, 25, 32, 30, 55, 24])

# Get user input with error handling
while True:
    try:
        distance_km = int(input("Enter the distance in km: "))
        traffic_level = int(input("Enter the traffic level (1-10): "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Train the model
model = LinearRegression()
model.fit(X, y)

# Make prediction
delivery_input = np.array([[distance_km, traffic_level]])
predicted_time = model.predict(delivery_input)

# Display results
print(f"\nThe AI model predicts that with {distance_km} km and traffic level {traffic_level},")
print(f"the delivery will take approximately {predicted_time[0]:.1f} minutes.")