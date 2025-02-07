pc = {
    "grafica": "nvidia",
    "cpu": "i5",
    "ram": "8",
}

print(pc['grafica'])
grafica = pc['grafica']
print(grafica)

pc['pc_componentes'] = 'componentes'
print(pc['cpu'])

del pc['pc_componentes']
print(pc)

