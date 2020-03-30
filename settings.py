SERVER_NAME = "lloyd-pearson.co.uk"
DOMAIN = {'widgets': {
        'allow_unknown': True,
      #  'additional_lookup' : {
      #      'url': 'regex(".+")',
      #      'field': 'instanceId'
      #      },
        'schema': {
                'instanceId': {'type': 'integer'},
            }
    }, 

    'data': {
            'allow_unknown': True,
            #'additional_lookup': {
             #   'url':'regex(".+")',
             #   'field': 'dataId'
             #   },
        'schema': {
            }
        }
    }

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'nuclear'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


ALLOW_UNKNOWN = True

PAGINATION = False
