import os
from pathlib import Path


print("file name:   ")
file1 = input()
#x = pd.read_csv(input, sep="\t")
#print(x)

in_file = open(file1, 'r')

lines = in_file.readlines()
valor1 = lines[2].strip().split('\t')
print(len(valor1))


archivo = open(file1 + 'yaml', "w")

archivo.write("dependent_variables: \n")
archivo.write("- header: {name: ' $ \ frac{1}{N}_{trig} \ frac{d N}{d \Delta \phi} $'}  \n")
archivo.write("  qualifiers: \n")
archivo.write(f"  - { {lines[0][2:-1]} } \n")
archivo.write("  values: \n")

for i in range(2, len(lines)):
    valor = lines[i].strip().split('\t')
    archivo.write(f"  - value: {valor[1]} \n")
    if len(valor)==3:
        archivo.write("    errors: \n")
        archivo.write(f"    - symerror: {valor[2]} \n")
        archivo.write( "      label: stat \n")
    if len(valor)==4:
        archivo.write("    errors: \n")
        archivo.write("    - asymerror: \n")
        archivo.write(f"       plus: {valor[2]}  \n")
        archivo.write(f"       minus: {valor[3]}  \n")
        archivo.write( "      label: stat \n")
    if len(valor)==5:
        archivo.write("    errors: \n")
        archivo.write(f"    - symerror: {valor[2]} \n")
        archivo.write( "    - asymerror: \n")
        archivo.write(f"       plus: {valor[3]}  \n")
        archivo.write(f"       minus: {valor[4]}  \n")
        archivo.write( "      label: stat \n")
    else:
        pass

archivo.write("independent_variables: \n")
archivo.write("- header: {name: '$ \Delta \phi = \phi - \phi_{t} $', units: 'rad'     } \n")
archivo.write("  values: \n")

for j in range(2, len(lines)):
    valor = lines[j].strip().split('\t')
    archivo.write(f"  - value: {valor[0]} \n")

archivo.close()

print(file1 + 'yaml')
filename = Path(file1 + 'yaml')
out_file = filename.with_suffix('.yaml')
print(out_file)
oldname = file1 + 'yaml'

os.rename(oldname,out_file)
