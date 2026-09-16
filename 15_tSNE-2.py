# ---------------------------------------------------------
# T-SNE EXAMPLE
# 3. Fashion-MNIST
# Fashion-MNIST consists of 70,000 $28 \times 28$ grayscale images across 10 clothing categories, organized as a drop-in replacement for standard MNIST.
# ---------------------------------------------------------

# Import required libraries
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
# ---------------------------------------------------------
# 1. Download dataset (returns X as 70,000 x 784, y as strings)
# ---------------------------------------------------------
fmnist = fetch_openml('Fashion-MNIST', version=1, as_frame=False, parser='auto')
X = fmnist.data
y = fmnist.target.astype(int)

print("Dataset shape:", X.shape)
print("Number of features:", X.shape[1])


# # ---------------------------------------------------------
# # STEP 2: Standardize the data
# # ---------------------------------------------------------

# # Standardization puts features on a similar scale
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# # # ---------------------------------------------------------
# # # STEP 3: Apply t-SNE
# # # ---------------------------------------------------------

# # # Create the t-SNE model
model = TSNE(
    n_components=2,       # Convert data into 2 dimensions
    perplexity=30,        # Number related to neighborhood size
    random_state=42       # Gives reproducible results
)

# # # Transform 64-dimensional data into 2 dimensions
X_tsne = model.fit_transform(X_scaled)

print("t-SNE output shape:", X_tsne.shape)


# # # ---------------------------------------------------------
# # # STEP 4: Visualize the result
# # # ---------------------------------------------------------

plt.figure(figsize=(10, 7))

# Create a scatter plot
# c=y means points are colored according to their digit
scatter = plt.scatter(
    X_tsne[:, 0], #Take all rows and the first column of X_tsne.
    X_tsne[:, 1], #Take all rows and the second column of X_tsne.
    c=y, #Color each point according to which digit it represents.
    cmap="tab10", #tab10 provides a set of different colors suitable for categorical values such as:
    s=15 #s means size of each point.
)

# Add color bar to show digit numbers
plt.colorbar(scatter, label="cloths")

# Add title and labels
plt.title("t-SNE Visualization of Fashion MNIST")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
# Display the graph
plt.show()