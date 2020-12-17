from .dal import exec_get_user


def user_get(query_schema):
    u_id = query_schema.get('u_id')
    return exec_get_user(u_id)
