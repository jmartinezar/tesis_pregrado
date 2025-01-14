import numpy as np
import matplotlib.pyplot as plt

# Define the range for φ
phi = np.linspace(-2, 2, 500)

# Define the potentials
V1 = 0.5 * phi**4  # λ > 0, μ^2 > 0
V2 = -0.5 * phi**2 + 0.25 * phi**4  # λ > 0, μ^2 < 0

# Define font size for axis labels
label_font_size = 15

# Create the first plot
plt.figure(figsize=(6, 4))
plt.plot(phi, V1, 'k')  # Black line
plt.axhline(0, color='black', linewidth=1.0)  # Solid horizontal axis
plt.axvline(0, color='black', linewidth=1.0)  # Solid vertical axis
plt.title(r"$\lambda > 0$ y $\mu^2 > 0$", fontsize=label_font_size)
plt.xlabel(r"$\phi$", fontsize=label_font_size)
plt.ylabel(r"$V(\phi)$", fontsize=label_font_size)
plt.xticks([])  # Remove x-axis numbering
plt.yticks([])  # Remove y-axis numbering
plt.grid(alpha=0.3)  # Restore the grid
plt.tight_layout()
plt.savefig("figures/pot_1.pdf")
plt.close()

# Create the second plot
plt.figure(figsize=(6, 4))
plt.plot(phi, V2, 'k')  # Black line
plt.axhline(0, color='black', linewidth=1.0)  # Solid horizontal axis
plt.axvline(0, color='black', linewidth=1.0)  # Solid vertical axis
plt.title(r"$\lambda > 0$ y $\mu^2 < 0$", fontsize=label_font_size)
plt.xlabel(r"$\phi$", fontsize=label_font_size)
plt.ylabel(r"$V(\phi)$", fontsize=label_font_size)
plt.xticks([])  # Remove x-axis numbering
plt.yticks([])  # Remove y-axis numbering
plt.grid(alpha=0.3)  # Restore the grid
plt.tight_layout()
plt.savefig("figures/pot_2.pdf")
plt.close()

print("The corrected plots have been saved as 'potential_positive_mu_fixed.pdf' and 'potential_negative_mu_fixed.pdf'.")