import numpy as np
import tensorflow as tf

print('TF version:', tf.__version__)

print("Coffee Roasting: learn Temp, Time => predict(probability that coffee beans are well-roasted).")

print("Set up the model...")

print("Using 3 nodes in hidden layer -> 1 node learns one 'bad region', where NOT to roast coffee. There 3 such 'bad' regions, so we use 3 nodes.")

tf.random.set_seed(1234)  # applied to achieve consistent results
model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(2,)),
        tf.keras.layers.Dense(3, activation='sigmoid', name = 'layer1'),
        tf.keras.layers.Dense(1, activation='sigmoid', name = 'layer2')
     ]
)
print(model.summary())

x = np.array([[200.0, 17.0],
              [120.0, 5.0],
              [425, 20],
              [212, 18]              
              ])

y = np.array([1,0,0,1])

# TODO
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01),
)

# normalize the data, to speed up back-propogation (fitting weights to the data)
norm_l = tf.keras.layers.Normalization(axis=-1)
norm_l.adapt(x)  # learns mean, variance

print("")
print("=== Training (learning weights) ===")
# Train: - needs data!
# model.fit(
#     Xt,Yt,
#     epochs=10,
# )

# hard-coded, previously trained weights:
W1 = np.array([
    [-8.94,  0.29, 12.89],
    [-0.17, -7.34, 10.79]] )
b1 = np.array([-9.87, -9.28,  1.01])
W2 = np.array([
    [-31.38],
    [-27.86],
    [-32.79]])
b2 = np.array([15.54])
model.get_layer("layer1").set_weights([W1,b1])
model.get_layer("layer2").set_weights([W2,b2])

print("After training, the weights have been adjusted:")
W1, b1 = model.get_layer("layer1").get_weights()
W2, b2 = model.get_layer("layer2").get_weights()
print("W1:\n", W1, "\nb1:", b1)
print("W2:\n", W2, "\nb2:", b2)

print("")
print("=== Inference (prediction) ===")
# model.predict(x_new)

# input data
X_test = np.array([
    [200,13.9],  # postive example
    [200,17]])   # negative example
print("input (temp Celsius, Duration minutes)")
print(X_test)
X_testn = norm_l(X_test)
predictions = model.predict(X_testn)
print("predictions = \n", predictions)

# To convert the probabilities to a decision, we apply a threshold of 0.5:
yhat = (predictions >= 0.5).astype(int)
print(f"decisions = \n{yhat}")
