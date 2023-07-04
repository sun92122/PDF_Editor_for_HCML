from flask import render_template, request
from app.PDFEditor import PDFMaker


def hello_world():
    return """
<h2 style='justify-content: center;display: flex;'>
    <a href='/'>Hello!</a>
</h2>
"""


user = {
    'username': 'Sun',
    'age': 18
}

MUTI_TEMPLATES = {
    'item': {
        'name': '', # should be other than switch[:2]|''
        'value': '',
        'type': 'text'
    },
    'price': {
        'name': '單價',
        'value': '',
        'type': 'number'
    },
    'quantity': {
        'name': '數量',
        'value': '',
        'type': 'number'
    },
    'unit': {
        'name': '單位',
        'value': '',
        'type': 'text'
    },
    'total': {
        'name': '總價',
        'value': '',
        'type': 'number'
    }
}

datas = {
    'eventName': {
        'name': '活動名稱',
        'value': '',
        'type': 'text'
    },
    'groupName': {
        'name': '活動股別',
        'value': '',
        'type': 'text'
    },
    'switch': {
        'name': '活動類型',
        'value': '',
        'type': 'radio',
        'options': {
            'purpose': '單一用途',
            'item': '單一項目'
        }
    },
    'single': {
        'name': '', # should be same as switch[:2]|''
        'value': '',
        'type': 'text'
    },
    'multiple': [
        {
            'item': {
                'name': '', # should be other than switch[:2]|''
                'value': '',
                'type': 'text'
            },
            'price': {
                'name': '單價',
                'value': '',
                'type': 'number'
            },
            'quantity': {
                'name': '數量',
                'value': '',
                'type': 'number'
            },
            'unit': {
                'name': '單位',
                'value': '',
                'type': 'text'
            },
            'total': {
                'name': '總價',
                'value': '',
                'type': 'number'
            }
        }
    ]
}


def index():
    if request.method == 'POST':
        user['username'] = request.form['username']
        user['age'] = request.form['age']
        # PDFMaker()
    return render_template('index.html', datas=datas)
