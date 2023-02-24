import math
import matplotlib.pyplot as plt
import numpy as np

# Propriedades do material usando Aramid como exemplo
E11 = 76  # GPa
E22 = 5.5  # GPa
G12 = 2.1  # GPa
nu12 = 0.34
nu21 = (E22 / E11) * nu12

# Ângulo em graus (Lembre-se de definir os ángulos)
theta = 30
theta_rad = math.radians(theta)

# Tensões aplicadas (Não esqueça de definir isso também)
sigma_xx = 100  # MPa
sigma_yy = -50  # MPa
tau_xy = 20  # MPa

# Cálculo das deformações
eps_xx = (1/E11) * (sigma_xx - nu12*sigma_yy)
eps_yy = (1/E22) * (sigma_yy - nu21*sigma_xx)
gamma_xy = (1/G12) * tau_xy

# Cálculo dos componentes de deformação
eps_11 = eps_xx * math.cos(theta_rad)**2 + eps_yy * math.sin(theta_rad)**2 + 2 * gamma_xy * math.sin(theta_rad) * math.cos(theta_rad)
eps_22 = eps_xx * math.sin(theta_rad)**2 + eps_yy * math.cos(theta_rad)**2 - 2 * gamma_xy * math.sin(theta_rad) * math.cos(theta_rad)
gamma_12 = (eps_xx - eps_yy) * math.sin(theta_rad) * math.cos(theta_rad) + gamma_xy * (math.cos(theta_rad)**2 - math.sin(theta_rad)**2)

# resultados
print("Estado de deformação (εxx, εyy, γxy):")
print((eps_xx, eps_yy, gamma_xy))
print("Componentes de deformação (ε11, ε22, γ12) em θ =", theta, "graus:")
print((eps_11, eps_22, gamma_12))

# Função para calcular as deformações para cada ângulo
def calc_deformation(theta, sigma_xx, sigma_yy, tau_xy):
    # Cálculo das deformações
    eps_xx = (1/E11) * (sigma_xx - nu12*sigma_yy)
    eps_yy = (1/E22) * (sigma_yy - nu21*sigma_xx)
    gamma_xy = (1/G12) * tau_xy

    # Cálculo dos componentes de deformação
    eps_11 = eps_xx * math.cos(theta)**2 + eps_yy * math.sin(theta)**2 + 2 * gamma_xy * math.sin(theta) * math.cos(theta)
    eps_22 = eps_xx * math.sin(theta)**2 + eps_yy * math.cos(theta)**2 - 2 * gamma_xy * math.sin(theta) * math.cos(theta)
    gamma_12 = (eps_xx - eps_yy) * math.sin(theta) * math.cos(theta) + gamma_xy * (math.cos(theta)**2 - math.sin(theta)**2)

    return eps_11, eps_22, gamma_12

# Função para calcular as tensões para cada ângulo
def calc_stress(theta, sigma_xx, sigma_yy, tau_xy):
    c = math.cos(theta)
    s = math.sin(theta)
    T = np.array([[c**2, s**2, 0], [s**2, c**2, 0], [0, 0, 2*c*s]])
    S = np.array([[1/E11, -nu12/E11, 0], [-nu21/E22, 1/E22, 0], [0, 0, 1/G12]])
    sigma = np.dot(np.dot(S, T), np.array([sigma_xx, sigma_yy, tau_xy]))
    return sigma[0], sigma[1], sigma[2]


# Lista de ângulos theta
theta_list = [i for i in range(0, 91, 5)]

# Listas para armazenar os valores de tensão
sigma11_list = []
sigma22_list = []
tau12_list = []

# Loop para calcular os valores de tensão para cada ângulo
for theta in theta_list:
    sigma11, sigma22, tau12 = calc_stress(math.radians(theta), sigma_xx, sigma_yy, tau_xy)
    sigma11_list.append(sigma11)
    sigma22_list.append(sigma22)
    tau12_list.append(tau12)

# Plot dos gráficos
plt.plot(theta_list, sigma11_list, label='σ11')
plt.plot(theta_list, sigma22_list, label='σ22')
plt.plot(theta_list, tau12_list, label='τ12')
plt.legend()
plt.title('Tensões em função do ângulo')
plt.xlabel('Ângulo (graus)')
plt.ylabel('Tensão (MPa)')
plt.show()