from flask import Flask, request, jsonify

app = Flask(__name__)

# Create some test data
transformers = [
    {'id': 0,
     'name': 'Optimus Prime',
     'type': 'Autobots',
    },
    {'id': 1,
     'name': 'Bumblebee',
     'type': 'Autobots',
    },
    {'id': 2,
     'name': 'Cliffjumper',
     'type': 'Autobots',
    },    
    {'id': 3,
     'name': 'Megatron',
     'type': 'Decepticons',
    },
    {'id': 4,
     'name': 'Soundwave',
     'type': 'Decepticons',
    },
    {'id': 5,
     'name': 'Starscream',
     'type': 'Decepticons',
    },
]

@app.route('/')
def home():
    return "<h1>Oh hi</h1><p>Greetings, Human</p>"


@app.route('/api/transformers/all', methods=['GET'])
def api_all():
    return jsonify(transformers)