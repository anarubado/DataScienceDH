def make_car(manufacturer, model, **info):
    result = {'manufacturer': manufacturer,
              'model': model}
    for key in info.keys():
        result[key] = info[key] # Agregamos los pares clave-valor que están en el diccionario info al diccionario result
    return result