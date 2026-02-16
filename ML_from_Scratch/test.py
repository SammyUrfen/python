# import numpy as np
# from network import Network, Layer, RMSProp


# # Create network
# network = Network([
#     Layer(128, 784, activation='relu'),  # Input: 784 features (MNIST)
#     Layer(64, 128, activation='relu'),
#     Layer(10, 64, activation='sigmoid') # Output: 10 classes
# ])

# # Load MNIST data
# train_set = np.loadtxt('mnist_train.csv', delimiter=',')
# X_train, y_train = train_set[:, 1:], train_set[:, 0]
# X_train = X_train / 255.0  # Normalize

# # One-hot encode labels
# y_train_one_hot = np.zeros((y_train.size, y_train.max().astype(int) + 1))
# y_train_one_hot[np.arange(y_train.size), y_train.astype(int)] = 1

# # Train
# optimizer = RMSProp(learning_rate=0.001)
# loss_history = network.train(X_train, y_train_one_hot, optimizer, 
#                             epochs=100, batch_size=128)


# # Load MNIST Test data
# train_set = np.loadtxt('mnist_test.csv', delimiter=',')
# X_train, y_train = train_set[:, 1:], train_set[:, 0]
# X_train = X_train / 255.0  # Normalize

# # One-hot encode labels
# y_train_one_hot = np.zeros((y_train.size, y_train.max().astype(int) + 1))
# y_train_one_hot[np.arange(y_train.size), y_train.astype(int)] = 1

# accuracy = network.test(X_train, y_train_one_hot)
# print(f"Test Accuracy: {accuracy:.2f}%")

# # Save model
# # network.save('mnist_model.pkl')

# # # Load model
# # loaded_net = Network.load('mnist_model.pkl')


import pandas as pd

# Replace 'your_file.csv' with your actual CSV file name
df = pd.read_csv('train.csv')

# Calculate missing values percentage and get data types
missing_data = pd.DataFrame({
    'Column': df.columns,
    'Data Type': df.dtypes,
    'Missing Values (%)': (df.isnull().sum() / len(df)) * 100
})

# Round the percentage to 2 decimal places
missing_data['Missing Values (%)'] = missing_data['Missing Values (%)'].round(2)

# Save the results to a CSV file
missing_data.to_csv('missing_values_analysis.csv', index=False)

# Display the results
print(missing_data)