
success = {200: {'status': 200, 'text': 'Successful'}}
created = {201: {'status': 201, 'text': 'Created'}}
accepted = {202: {'status': 202, 'text': 'Accepted'}}
no_content = {204: {'status': 204, 'text': 'No Content'}}

bad_request = {400: {'status': 400, 'text': 'Bad Request'}}
unauthorized = {401: {'status': 401, 'text': 'Unauthorized'}}
forbidden = {403: {'status': 403, 'text': 'Forbidden'}}
not_found = {404: {'status': 404, 'text': 'Not Found'}}
method_not_allowed = {405: {'status': 405, 'text': 'Method Not Allowed'}}
conflict = {409: { "status": 409,"text": "User already exists"}}
session_expired = {419:{"status":419,"text":"Session Expired"}}
unprocessable_entity = {422: {'status': 422, 'text': 'Unprocessable Entity'}}

internal_server_error = {500: {'status': 500, 'text': 'Internal Server Error'}}
not_implemented = {501: {'status': 501, 'text': 'Not Implemented'}}
service_unavailable = {503: {'status': 503, 'text': 'Service Unavailable'}}

# A combined dictionary for easier access
http_statuses = {
    **success,
    **created,
    **accepted,
    **no_content,
    **bad_request,
    **session_expired,
    **unauthorized,
    **forbidden,
    **not_found,
    **method_not_allowed,
    **conflict,
    **unprocessable_entity,
    **internal_server_error,
    **not_implemented,
    **service_unavailable,
}
