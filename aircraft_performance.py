import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# AIRCRAFT PARAMETERS
# ==========================================

mass = 1200          # Aircraft mass, kg
S = 16               # Wing area, m^2
AR = 8               # Aspect ratio
e = 0.8              # Oswald efficiency factor
CD0 = 0.025          # Zero-lift drag coefficient
CL_max = 1.5         # Maximum lift coefficient

rho = 1.225          # Air density, kg/m^3
g = 9.81             # Gravitational acceleration, m/s^2

# ==========================================
# BASIC CALCULATIONS
# ==========================================

# Aircraft weight
W = mass * g

# Induced drag factor
K = 1 / (np.pi * e * AR)

# ==========================================
# DISPLAY RESULTS
# ==========================================

print("==========================================")
print("     AIRCRAFT PERFORMANCE ANALYSIS")
print("==========================================")

print(f"Aircraft Mass              : {mass} kg")
print(f"Wing Area                  : {S} m^2")
print(f"Aspect Ratio               : {AR}")
print(f"Oswald Efficiency          : {e}")
print(f"Zero-Lift Drag Coefficient : {CD0}")
print(f"Maximum Lift Coefficient   : {CL_max}")
print(f"Aircraft Weight            : {W:.2f} N")
print(f"Induced Drag Factor (K)    : {K:.4f}")
# ==========================================
# PERFORMANCE CALCULATION
# ==========================================

# Stall speed
V_stall = np.sqrt((2 * W) / (rho * S * CL_max))

# Velocity range
V = np.linspace(28.3, 200, 500)

# Dynamic pressure
q = 0.5 * rho * V**2

# Lift coefficient for steady level flight
CL = W / (q * S)

# Drag coefficient
CD = CD0 + K * CL**2

# Lift
L = q * S * CL

# Drag
D = q * S * CD

# Lift-to-drag ratio
L_D = L / D

# ==========================================
# DISPLAY SOME RESULTS
# ==========================================

print("\nPerformance at selected speeds:")

for speed in [30, 50, 70, 90, 110, 130]:
    
    q_speed = 0.5 * rho * speed**2
    CL_speed = W / (q_speed * S)
    CD_speed = CD0 + K * CL_speed**2
    D_speed = q_speed * S * CD_speed
    
    print(f"\nVelocity = {speed} m/s")
    print(f"CL       = {CL_speed:.3f}")
    print(f"CD       = {CD_speed:.3f}")
    print(f"Drag     = {D_speed:.2f} N")
    # ==========================================
# PERFORMANCE PLOTS
# ==========================================

# 1. Drag vs Velocity
plt.figure()
plt.plot(V, D)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.title("Drag vs Velocity")
plt.grid(True)
plt.show()


# 2. Lift Coefficient vs Velocity
plt.figure()
plt.plot(V, CL)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lift Coefficient (CL)")
plt.title("Lift Coefficient vs Velocity")
plt.grid(True)
plt.show()


# 3. Drag Coefficient vs Velocity
plt.figure()
plt.plot(V, CD)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("Drag Coefficient vs Velocity")
plt.grid(True)
plt.show()


# 4. Lift-to-Drag Ratio vs Velocity
plt.figure()
plt.plot(V, L_D)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lift-to-Drag Ratio (L/D)")
plt.title("Lift-to-Drag Ratio vs Velocity")
plt.grid(True)
plt.show()
# ==========================================
# KEY PERFORMANCE PARAMETERS
# ==========================================



# CL corresponding to maximum L/D
CL_LD_max = np.sqrt(CD0 / K)

# Velocity corresponding to maximum L/D
V_LD_max = np.sqrt((2 * W) / (rho * S * CL_LD_max))

# Maximum L/D
CD_LD_max = CD0 + K * CL_LD_max**2
LD_max = CL_LD_max / CD_LD_max

# ==========================================
# DISPLAY KEY RESULTS
# ==========================================

print("\n==========================================")
print("        KEY PERFORMANCE PARAMETERS")
print("==========================================")

print(f"Stall Speed              : {V_stall:.2f} m/s")
print(f"Stall Speed              : {V_stall * 3.6:.2f} km/h")

print(f"CL at Maximum L/D        : {CL_LD_max:.3f}")
print(f"Velocity at Maximum L/D  : {V_LD_max:.2f} m/s")
print(f"Velocity at Maximum L/D  : {V_LD_max * 3.6:.2f} km/h")
print(f"Maximum L/D              : {LD_max:.2f}")
# ==========================================
# THRUST AND POWER REQUIRED
# ==========================================

# In steady level flight:
# Thrust required = Drag

# ==========================================
# THRUST REQUIRED
# ==========================================

T_required = D

# ==========================================
# THRUST AVAILABLE
# ==========================================

T_available = 4000       # N

# ==========================================
# THRUST DIAGNOSTIC
# ==========================================

print("\n--- THRUST DIAGNOSTIC ---")
print(f"Minimum Thrust Required : {np.min(T_required):.2f} N")
print(f"Maximum Thrust Required : {np.max(T_required):.2f} N")
print(f"Thrust Available        : {T_available:.2f} N")
print(f"Velocity Minimum        : {V[0]:.2f} m/s")
print(f"Velocity Maximum        : {V[-1]:.2f} m/s")

# Power required
P_required = T_required * V

# Convert power to kW
P_required_kW = P_required / 1000
# ==========================================
# MINIMUM THRUST AND POWER REQUIRED
# ==========================================

min_thrust_index = np.argmin(T_required)
min_power_index = np.argmin(P_required)

V_min_thrust = V[min_thrust_index]
T_min = T_required[min_thrust_index]

V_min_power = V[min_power_index]
P_min = P_required[min_power_index]

print("\n==========================================")
print("       THRUST & POWER PERFORMANCE")
print("==========================================")

print(f"Minimum Thrust Required : {T_min:.2f} N")
print(f"Speed at Minimum Thrust : {V_min_thrust:.2f} m/s")

print(f"Minimum Power Required  : {P_min/1000:.2f} kW")
print(f"Speed at Minimum Power  : {V_min_power:.2f} m/s")
# ==========================================
# THRUST REQUIRED VS VELOCITY
# ==========================================

plt.figure()
plt.plot(V, T_required)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Thrust Required (N)")
plt.title("Thrust Required vs Velocity")
plt.grid(True)
plt.show()


# ==========================================
# POWER REQUIRED VS VELOCITY
# ==========================================

plt.figure()
plt.plot(V, P_required_kW)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Power Required (kW)")
plt.title("Power Required vs Velocity")
plt.grid(True)
plt.show()
# ==========================================
# THRUST AVAILABLE
# ==========================================


# Excess thrust
T_excess = T_available - T_required
# ==========================================
# MAXIMUM EXCESS THRUST
# ==========================================

max_excess_index = np.argmax(T_excess)

V_max_excess = V[max_excess_index]
T_excess_max = T_excess[max_excess_index]

print("\n==========================================")
print("          THRUST PERFORMANCE")
print("==========================================")

print(f"Thrust Available       : {T_available:.2f} N")
print(f"Maximum Excess Thrust   : {T_excess_max:.2f} N")
print(f"Speed at Max Excess     : {V_max_excess:.2f} m/s")

# ==========================================
# POWER PERFORMANCE
# ==========================================

# Power Required
P_required = T_required * V

# Power Available
P_available = T_available * V

# Maximum excess power
excess_power = P_available - P_required

# Maximum rate of climb
max_ROC = np.max(excess_power) / W

# Speed for maximum rate of climb
V_max_ROC = V[np.argmax(excess_power)]

print("\n==========================================")
print("          POWER PERFORMANCE")
print("==========================================")

print(f"Maximum Power Available : {np.max(P_available)/1000:.2f} kW")
print(f"Maximum Power Required  : {np.max(P_required)/1000:.2f} kW")

print(f"Maximum Excess Power    : {np.max(excess_power)/1000:.2f} kW")
print(f"Speed for Maximum ROC   : {V_max_ROC:.2f} m/s")
print(f"Maximum Rate of Climb   : {max_ROC:.2f} m/s")

# ==========================================
# POWER REQUIRED VS POWER AVAILABLE GRAPH
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    V,
    P_required / 1000,
    linewidth=2,
    label="Power Required"
)

plt.plot(
    V,
    P_available / 1000,
    linewidth=2,
    label="Power Available"
)

plt.scatter(
    V_max_ROC,
    P_available[np.argmax(excess_power)] / 1000,
    s=100,
    zorder=5,
    label=f"Maximum ROC = {max_ROC:.2f} m/s"
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Power (kW)")
plt.title("Power Required vs Power Available")

plt.grid(True)
plt.legend()

plt.show()

# ==========================================
# RATE OF CLIMB VS VELOCITY
# ==========================================

rate_of_climb = excess_power / W

max_roc_index = np.argmax(rate_of_climb)

plt.figure(figsize=(10, 6))

plt.plot(
    V,
    rate_of_climb,
    linewidth=2,
    label="Rate of Climb"
)

plt.scatter(
    V[max_roc_index],
    rate_of_climb[max_roc_index],
    s=100,
    zorder=5,
    label=f"Maximum ROC = {rate_of_climb[max_roc_index]:.2f} m/s"
)

plt.axvline(
    V[max_roc_index],
    linestyle="--",
    linewidth=1,
    label=f"Speed = {V[max_roc_index]:.2f} m/s"
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Rate of Climb (m/s)")
plt.title("Rate of Climb vs Velocity")

plt.xlim(V_stall, 140)

plt.grid(True)
plt.legend()

plt.show()
# ==========================================
# POWER REQUIRED VS POWER AVAILABLE GRAPH
# ==========================================

plt.figure(figsize=(10, 6))

# Power Required
plt.plot(
    V,
    P_required / 1000,
    linewidth=2,
    label="Power Required"
)

# Power Available
plt.plot(
    V,
    P_available / 1000,
    linewidth=2,
    label="Power Available"
)

# Maximum excess power / maximum ROC point
idx_max_ROC = np.argmax(excess_power)

plt.scatter(
    V_max_ROC,
    P_required[idx_max_ROC] / 1000,
    s=100,
    zorder=5,
    label=f"Maximum ROC = {max_ROC:.2f} m/s"
)

# Vertical line at maximum ROC speed
plt.axvline(
    V_max_ROC,
    linestyle="--",
    linewidth=1
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Power (kW)")
plt.title("Power Required vs Power Available")

plt.xlim(V_stall, 140)
plt.ylim(0, 500)

plt.grid(True)
plt.legend()

plt.show()

# ==========================================
# CL VS VELOCITY
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    V,
    CL,
    linewidth=2,
    label="Lift Coefficient (CL)"
)

plt.axhline(
    CL_max,
    linestyle="--",
    linewidth=1,
    label=f"CL max = {CL_max:.2f}"
)

plt.axvline(
    V_stall,
    linestyle="--",
    linewidth=1,
    label=f"Stall Speed = {V_stall:.2f} m/s"
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Lift Coefficient (CL)")
plt.title("Lift Coefficient vs Velocity")

plt.xlim(V_stall, 140)

plt.grid(True)
plt.legend()

plt.show()

# ==========================================
# CD VS VELOCITY
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    V,
    CD,
    linewidth=2,
    label="Drag Coefficient (CD)"
)

plt.axhline(
    CD0,
    linestyle="--",
    linewidth=1,
    label=f"CD₀ = {CD0:.3f}"
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("Drag Coefficient vs Velocity")

plt.xlim(V_stall, 140)

plt.grid(True)
plt.legend()

plt.show()

# ==========================================
# DRAG VS VELOCITY
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    V,
    T_required,
    linewidth=2,
    label="Drag / Thrust Required"
)

# Minimum drag point
min_drag_index = np.argmin(T_required)

plt.scatter(
    V[min_drag_index],
    T_required[min_drag_index],
    s=100,
    zorder=5,
    label=f"Minimum Drag = {T_required[min_drag_index]:.2f} N"
)

plt.axvline(
    V[min_drag_index],
    linestyle="--",
    linewidth=1,
    label=f"Minimum Drag Speed = {V[min_drag_index]:.2f} m/s"
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.title("Drag vs Velocity")

plt.xlim(V_stall, 140)

plt.grid(True)
plt.legend()

plt.show()
# ==========================================
# RATE OF CLIMB
# ==========================================

P_available = T_available * V

P_excess = P_available - P_required

ROC = P_excess / W

# Maximum rate of climb
max_ROC_index = np.argmax(ROC)

V_max_ROC = V[max_ROC_index]
max_ROC = ROC[max_ROC_index]

print("\n==========================================")
print("             CLIMB PERFORMANCE")
print("==========================================")

print(f"Maximum Rate of Climb : {max_ROC:.2f} m/s")
print(f"Speed for Maximum ROC : {V_max_ROC:.2f} m/s")

# ==========================================
# RATE OF CLIMB VS VELOCITY
# ==========================================

plt.figure()

plt.plot(V, ROC)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Rate of Climb (m/s)")
plt.title("Rate of Climb vs Velocity")
plt.grid(True)

plt.show()
# ==========================================
# LEVEL FLIGHT INTERSECTIONS
# ==========================================

# Difference between thrust available and thrust required
thrust_difference = T_available - T_required

# Find locations where the sign changes
crossing_indices = np.where(
    np.diff(np.sign(thrust_difference)) != 0
)[0]

# Calculate the two intersection speeds using interpolation
V_intersections = []

for i in crossing_indices:
    V1 = V[i]
    V2 = V[i + 1]

    T1 = thrust_difference[i]
    T2 = thrust_difference[i + 1]

    # Linear interpolation
    V_cross = V1 - T1 * (V2 - V1) / (T2 - T1)

    V_intersections.append(V_cross)

print("\n==========================================")
print("       LEVEL FLIGHT INTERSECTIONS")
print("==========================================")

for i, V_cross in enumerate(V_intersections):

    print(f"Intersection {i + 1} : {V_cross:.2f} m/s")
    print(f"Intersection {i + 1} : {V_cross * 3.6:.2f} km/h")

# Maximum level-flight speed
V_max_level = V_intersections[-1]

# ==========================================
# THRUST REQUIRED VS THRUST AVAILABLE
# ==========================================

plt.figure(figsize=(10, 6))

# Thrust required curve
plt.plot(
    V,
    T_required,
    linewidth=2,
    label="Thrust Required"
)

# Thrust available
plt.axhline(
    y=T_available,
    linewidth=2,
    label="Thrust Available = 4000 N"
)

# Mark intersection
for V_cross in V_intersections:

    plt.scatter(
        V_cross,
        T_available,
        s=100,
        zorder=5,
        label=f"Intersection = {V_cross:.2f} m/s"
    )

# Zoom into the useful region
plt.xlim(28, 140)
plt.ylim(0, 5000)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Thrust (N)")
plt.title("Thrust Required vs Thrust Available")

plt.legend()
plt.grid(True)

plt.show()

# ==========================================
# FINAL AIRCRAFT PERFORMANCE SUMMARY
# ==========================================

print("\n")
print("=" * 50)
print("       FINAL AIRCRAFT PERFORMANCE SUMMARY")
print("=" * 50)

print(f"Aircraft Mass              : {mass:.2f} kg")
print(f"Wing Area                  : {S:.2f} m^2")
print(f"Aspect Ratio               : {AR:.2f}")
print(f"Oswald Efficiency          : {e:.2f}")
print(f"Zero-Lift Drag Coefficient : {CD0:.3f}")
print(f"Maximum Lift Coefficient   : {CL_max:.2f}")

print("\n--- AERODYNAMIC PERFORMANCE ---")

print(f"Stall Speed                : {V_stall:.2f} m/s")
print(f"Stall Speed                : {V_stall * 3.6:.2f} km/h")
print("Maximum L/D                : 14.18")
print("Speed at Maximum L/D       : 41.16 m/s")
print("Speed at Maximum L/D       : 148.18 km/h")

print("\n--- THRUST PERFORMANCE ---")

print(f"Thrust Available            : {T_available:.2f} N")
print(f"Minimum Thrust Required     : {np.min(T_required):.2f} N")
print(f"Maximum Level-Flight Speed  : {V_max_level:.2f} m/s")
print(f"Maximum Level-Flight Speed  : {V_max_level * 3.6:.2f} km/h")

print("\n--- POWER & CLIMB PERFORMANCE ---")

print(f"Maximum Excess Power        : {excess_power[max_excess_index] / 1000:.2f} kW")
print(f"Speed for Maximum ROC       : {V_max_ROC:.2f} m/s")
print(f"Maximum Rate of Climb       : {max_ROC:.2f} m/s")

print("\n" + "=" * 50)
print("              ANALYSIS COMPLETE")
print("=" * 50)