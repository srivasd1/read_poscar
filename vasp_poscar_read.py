def read_poscar(filename):
  with open(filename, 'r') as f:
   lines = f.readlines()
#First line is comment .strip() removes white leading or trailing spaces of the line
   comment = lines[0].strip()
#Scaling Parameter
   SP = float(lines[1].strip())
#lattice Vectors
  lattice_vectors = []
  for i in range(2,5):
     vector = list(map(float,lines[i].strip().split())) #map() is used to apply a given function to each item of an iterable 
#(like a list or a tuple) and returns a map object, which can be converted to a list, tuple,
     lattice_vectors.append(vector)
#Elements Kind
  elements = lines[5].strip().split()
#No. of elements of each kind
  elements_counts=list(map(int, lines[6].strip().split()))
#Check Selective dynamics
  if lines[7].strip().startswith('s'):
    number = 8
  elif lines[7].strip().startswith('S'):
    number = 8
  else:
    number = 7
    print(number) 
# The next line to read  coordinates: direct or cartesian
  coordinate_type = lines[number].strip()
# Read atomic positions
  atomic_positions = []
  for i in range(number+1, sum(elements_counts)+number):
      position = list(map(float,lines[i].strip().split()))
      atomic_positions.append(position)
  return{"comment": comment,
        "scaling_factor": SP,
        "lattice_vectors": lattice_vectors,
	"coordinate_type": coordinate_type,
        "element_counts": elements_counts,
        "atomic_positions": atomic_positions
}
  

# Example usage
poscar_data = read_poscar("POSCAR")
print("Lattice Vectors:", poscar_data['lattice_vectors'])
print(poscar_data['coordinate_type'])
print("Atomic Positions:", poscar_data['atomic_positions'])
#x=poscar_data['lattice_vectors']
#print(x[1][1])
