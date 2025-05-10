# Example new input (change as needed)
new_input = np.array([[75, 0, 1, 20, 582, 0, 1, 130, 1, 4, 1]])  # Use appropriate format
new_input_scaled = scaler.transform(new_input)

prediction = model.predict(new_input_scaled)
print("Predicted Death Event (1 = Yes, 0 = No):", prediction[0])
