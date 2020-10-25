# -*- coding: utf-8 -*-

# pandas library
import pandas as pd

# gallery local library
from Gallery import meses as m 
from Gallery import graph as gh

def gen_json(data):
    df = pd.DataFrame(data)

    #group by UDIS
    udis = df[df['divisa']=='UDIS']
    month_group_udis = udis.groupby('mes')

    #group by USD
    usd = df[df['divisa']=='USD']
    month_group_usd = usd.groupby('mes')

    e_keys = month_group_udis.groups.keys()
    r_keys = month_group_usd.groups.keys()

    _agrega_datos(e_keys,month_group_udis,'UDIS')
    _agrega_datos(r_keys, month_group_usd,'USD')

    return 'ok'

def _agrega_datos(g_keys, group, tipo):

    for k in g_keys:
        data_series = {}
        drilldown_serie ={'data':[]}
        
        nombre_mes = m.meses[k]['nombre']
        pesos = group.get_group(k)['pesos'].sum()
        dias_list = group.get_group(k)['dia'].tolist()

        pesos_list = group.get_group(k)['pesos'].tolist()
        
        data_series['name'] = nombre_mes
        data_series['y'] = pesos

        if tipo == 'UDIS':
            data_series['drilldown'] = nombre_mes + '_udis' 
            data_series['color'] = "#625AA4"
            drilldown_serie['id']= nombre_mes + '_udis'
            drilldown_serie['name'] = 'UDIS'
        else:
            data_series['drilldown'] = nombre_mes + '_usd' 
            drilldown_serie['id']= nombre_mes + '_usd'
            data_series['color'] = "#72B5A8"
            drilldown_serie['name'] = nombre_mes
            drilldown_serie['name'] = 'USD'
        
        
        #drilldown_serie['name'] = nombre_mes
        
    
        dias_list.sort()
    
        for i in range(len(dias_list)):
            data_list =[str(dias_list[i]),pesos_list[i]]
            drilldown_serie['data'].append(data_list)
    
        if tipo == 'UDIS':
            gh.grafico['series'][0]['data'].append(data_series)
        else:
            gh.grafico['series'][1]['data'].append(data_series)

        gh.grafico['drilldown']['series'].append(drilldown_serie)




