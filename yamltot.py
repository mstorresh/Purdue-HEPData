#code create by: Manuel Sebastián Torres Hernández


import yaml
import os

# ------ reading the list of yaml files --------------- 1.
fileyamllist = 'texlist.txt'

in_fileyamllist = open(fileyamllist, 'r')

lines = in_fileyamllist.readlines()


# -------- reading the figure list ------------

fileplot = 'plotlist.txt'

in_fileplot = open(fileplot, 'r')

linesplot = in_fileplot.readlines()


# -----------------  reading the yaml files -----------------------------------------------


linesyaml = lines[0].strip()  #yaml list

print(str(linesyaml[:-5]))
print(len(lines))


linesn = linesplot[0].strip()
print(str(linesn[len(linesn)-3:]))
print(linesplot[0])
print(len(linesplot))

archivo = open('submission.txt', "w")

header1 = []
quali2 = []
header2 = []
for nume in range(len(lines)):
    linesyaml = str(lines[nume].strip())
    with open(linesyaml, 'r') as file:

        documents = yaml.load(file)
        archivo.write(f'name: "{linesyaml[:-5]}"    \n')
        for item, doc in documents.items():
            #print( doc[0]['header'])
            #print(documents.items())
            #print( doc[0].keys())
            for i in doc[0].keys():
                if i == 'qualifiers':
                    word = str(doc[0]['qualifiers']).replace(':', '')
                    word = word.replace('None', '').replace("'",'')
                    quali2.append(word)
            header1.append(str(doc[0]['header']))
        for i in range(len(header1)):
            if header1[i][-3] == '$' :
                #print(header1[i][10:-2])
                he = header1[i][10:-2].replace(':', '')
                he = he.replace("'",'')
                header2.append(he)
            else:
                #print(header1[i][9:-1])
                he2 = header1[i][9:-1].replace(':', '')
                he2 = he2.replace("'",'')
                header2.append(he2)


        #print(quali2[0][3:-2])
        print(linesyaml)
        archivo.write(f"location: Data from Figure {linesyaml[3:5]}    \n")
        archivo.write(f"description: {quali2[0][2:-2]} , " + f"{header2[0]} , " + f"{header2[1]}  \n")
        archivo.write(f"keywords:   \n")
        archivo.write("- { name:" + f"  { header1[0]}" + " }  \n")
        archivo.write("- { name:" + f"  { header1[1]}" + " }  \n")

        archivo.write(f"data_file:  {linesyaml} \n")
        archivo.write("additional_resources: \n")

        for k in range(len(linesplot)):
            linesn = linesplot[k].strip()
            if linesyaml[0:6] == linesn[0:6] and linesn[-2] == 'd':
                archivo.write("- {description: Image file , location: " + f"{linesn}" + "} \n" )
            else:
                pass
        header1.clear()
        header2.clear()
        quali2.clear()
        archivo.write("\n")


os.rename('submission.txt', 'submission.yaml')
