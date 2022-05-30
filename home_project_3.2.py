HEIGHT = 3000
WIRE_WEIGHT = {3: 0.056, 4: 0.099, 5: 0.154, 2: 0.0247, 1: 0.0062}
length = input("Enter length")
if length.isdigit() or lentgh.endswith('mm'):
 multiplier = 1
elif length.endswith('mm'):
 multiplier = 10
else:
 multiplier = 1000
mesh_edge = input("Enter mesh cell size")
if length.endswith('mm'):
 multiplier = 10
else:
 multiplier = 1
length_mm = int(length.strip('cm'))*multiplier
mesh_edge_mm = int(mesh_edge.strip('cm'))*multiplier
wire_diametr = int(input('Enter wire diametr'))
wire_length = 2 * length_mm / mesh_edge_mm * HEIGHT * 2 / 3 ** 0.5
wire_length_m = wire_length / 1000
print (
f'You need {wire_length_m * WIRE_WEIGHT[wire_diametr]} kg of '
f'wire {wire_diametr} mm in diametr'
)