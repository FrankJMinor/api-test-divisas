# -*- coding: utf-8 -*-

def init_graph():
    grafico['series'][0]['data'] = []
    grafico['series'][1]['data'] = []
    grafico['drilldown']['series'] = []

grafico = {
    'labels': {
            'items' : [{
              'html' : 'El valor en pesos puede sobreponerse, sobreponga el cursos en la columna para visualizar el dato',
            'style' : {
                'left' : '1px',
              'top' : '273px',
             'color' : '#fffff',
              'fontWeight' : '100'
            }
          }]
     },
    'chart': {
        'type': 'column'
    },
    'title': {
        'text': 'Divisas'
    },
    'subtitle': {
        'text': 'Mostrará tiempo en meses o días según corresponda el periodo seleccionado'
    },
    'accessibility': {
        'announceNewData': {
    'enabled': True
        }
    },
    'xAxis': {
        'type': 'category'
    },
    'yAxis': {
        'title': {
    'text': 'Monto'
        }

    },
    'legend': {
        'enabled': True
    },
    'plotOptions': {
        'series': {
    'borderWidth': 0,
    'dataLabels': {
        'enabled': True,
        'format': '${point.y:,.1f}'
    }
        }
    },

    'tooltip': {
        'headerFormat': '<span style="font-size:11px">{series.name}</span><br>',
        'pointFormat': '<span style="color:{point.color}">{point.name}</span>: <b>${point.y:,.2f}</b>'
    },

    'series': [
        {
    'name': "UDIS",
    'colorByPoint': False,
    "color" : "#625AA4",
    'data': []
        },

        {
    'name': "USD",
    'colorByPoint': False,
    "color" : "#72B5A8",
    'data': []
        }

    ],
    'drilldown': {
        'series': [
    
             
        ]
    }
}



