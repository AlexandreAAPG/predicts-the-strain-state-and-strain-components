import math

# Propriedades do material usando Aramid como exemplo
E11 = 76  # GPa
E22 = 5.5  # GPa
G12 = 2.1  # GPa
nu12 = 0.34
nu21 = (E22 / E11) * nu12

# Ângulo em graus (Lembre-se de definir os ángulos)
theta = 30
theta_rad = math.radians(theta)

# Tensões aplicadas (Não esqueça de definir isso támbem)
sigma_xx = 100  # MPa
sigma_yy = -50  # MPa
tau_xy = 20  # MPa

# Cálculo das deformações
eps_xx = (1/E11) * (sigma_xx - nu12*sigma_yy)
eps_yy = (1/E22) * (sigma_yy - nu21*sigma_xx)
gamma_xy = (1/G12) * tau_xy