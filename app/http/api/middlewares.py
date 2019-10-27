from functools import wraps
from flask import request, g, abort
from jwt import decode, exceptions
import json

# flask provides a module called 'g' which is a global context shared
# across the request life cycle.
# This middleware is checking whether or not the request is valid,
# if so, the middleware will extract the authenticated user details
# and persist them in the global context.
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
      authorization = request.headers.get("authorization", None)
      if not authorization:
          return json.dumps({'error': 'no authorization token provied'}), 403, {'Content-type': 'application/json'}
      
      try:
          token = authorization.split(' ')[1]
          resp = decode(token, None, verify=False, algorithms=['HS256'])
          g.user = resp['sub']
      except exceptions.DecodeError as identifier:
          return json.dumps({'error': 'invalid authorization token'}), 403, {'Content-type': 'application/json'}
      
      return f(*args, **kwargs)

  return wrap