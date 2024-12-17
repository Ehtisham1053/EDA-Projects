import numpy as np

# 1. numpy.random.rand
# Generates an array of random values from a uniform distribution over [0, 1).
rand_array = np.random.rand(2, 3)  # 2x3 array
print("Random Array (Uniform [0,1)):\n", rand_array)

# 2. numpy.random.randn
# Generates an array of random values from a standard normal distribution (mean=0, std=1).
randn_array = np.random.randn(2, 3)  # 2x3 array
print("Random Array (Normal Mean=0, Std=1):\n", randn_array)

# 3. numpy.random.randint
# Generates random integers between 1 (inclusive) and 10 (exclusive).
randint_array = np.random.randint(1, 10, size=(2, 3))  # 2x3 array
print("Random Integer Array:\n", randint_array)

# 4. numpy.random.random_sample
# Generates random floats in the range [0.0, 1.0).
random_sample_array = np.random.random_sample((2, 3))  # 2x3 array
print("Random Sample Array:\n", random_sample_array)

# 5. numpy.random.choice
# Selects random elements from a given 1D array with probabilities.
choice_array = np.random.choice([10, 20, 30, 40], size=5, replace=True, p=[0.1, 0.2, 0.3, 0.4])
print("Random Choice Array:\n", choice_array)

# 6. numpy.random.uniform
# Generates random floats from a uniform distribution over [5, 10).
uniform_array = np.random.uniform(5, 10, size=(2, 3))  # 2x3 array
print("Uniform Random Array:\n", uniform_array)

# 7. numpy.random.normal
# Generates random floats from a normal distribution (mean=5, std=2).
normal_array = np.random.normal(5, 2, size=(2, 3))  # 2x3 array
print("Normal Random Array (Mean=5, Std=2):\n", normal_array)

# 8. numpy.random.binomial
# Generates random integers from a binomial distribution (10 trials, p=0.5 success probability).
binomial_array = np.random.binomial(10, 0.5, size=(2, 3))  # 2x3 array
print("Binomial Random Array:\n", binomial_array)

# 9. numpy.random.poisson
# Generates random integers from a Poisson distribution (expected events = 3).
poisson_array = np.random.poisson(3, size=(2, 3))  # 2x3 array
print("Poisson Random Array:\n", poisson_array)

# 10. numpy.random.seed
# Sets a seed for reproducibility of random numbers.
np.random.seed(42)
consistent_array = np.random.rand(2, 3)  # Always produces the same output for the same seed
print("Consistent Random Array:\n", consistent_array)

# 11. numpy.random.shuffle
# Randomly shuffles an array in place.
array = np.array([1, 2, 3, 4, 5])
np.random.shuffle(array)
print("Shuffled Array:\n", array)

# 12. numpy.random.permutation
# Randomly permutes the elements of an array (returns a new array).
permuted_array = np.random.permutation([1, 2, 3, 4, 5])
print("Permuted Array:\n", permuted_array)

# 13. numpy.random.beta
# Generates samples from a Beta distribution (shape parameters a=2, b=5).
beta_array = np.random.beta(2, 5, size=(2, 3))  # 2x3 array
print("Beta Distribution Array:\n", beta_array)

# 14. numpy.random.exponential
# Generates samples from an Exponential distribution (scale=1.5).
exponential_array = np.random.exponential(1.5, size=(2, 3))  # 2x3 array
print("Exponential Random Array:\n", exponential_array)

# 15. numpy.random.multivariate_normal
# Generates samples from a multivariate normal distribution (mean vector and covariance matrix).
mean = [0, 0]
cov = [[1, 0.5], [0.5, 1]]  # Covariance matrix
multi_normal_array = np.random.multivariate_normal(mean, cov, size=5)  # 5 samples
print("Multivariate Normal Array:\n", multi_normal_array)
