
import math 

input_strain = float(input("Enter the strain: "))

# strain and stress coordinates
A = (0.01, 43)
C = (0.06, 43.5)
D = (0.18, 60)
E = (0.27, 51)

# linear elastic region
if input_strain >= 0 and input_strain <= 0.01:
    Y = 43/0.01
    stress = Y * input_strain
    print("The stress is approximately", round(stress, 1))

# plastic region
elif input_strain > 0.01 and input_strain <= 0.06:
    slope = (C[1] - A[1])/(C[0] - A[0])
    stress = (slope * (input_strain - A[0])) + A[1]
    print("The stress is approximately", round(stress, 1))

# strain hardening region
elif input_strain > 0.06 and input_strain <= 0.18:
    slope = (D[1] - C[1])/(D[0] - C[0])
    stress = (slope * (input_strain - C[0])) + C[1]
    print("The stress is approximately", round(stress, 1))

# necking region
elif input_strain > 0.18 and input_strain <= 0.27:
    slope = (E[1] - D[1])/(E[0] - D[0])
    stress = (slope * (input_strain - E[0])) + E[1]
    print("The stress is approximately", round(stress, 1))

# for edge cases
else:
    print("Strain is undefined in that region")

