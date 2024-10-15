def all_user_data(*,cursor,user_id = None):
    query = f"SELECT user_id,name,email,role FROM userdata;"
    cursor.execute(query)
    data = cursor.fetchall()
    user_data = []
    if data is  None or len(data) == 0:
        return None
    else:
        for user in data:
            user_data.append({
                'user_id':user[0],
                'name':user[1],
                'email':user[2],
                'role':user[-1]
            })
    return user_data
