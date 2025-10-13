def session_user(request):
    return {
        'session_user_id': request.session.get('user_id'),
        'session_username': request.session.get('username'),
    }
