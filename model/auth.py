import datetime
import random
from model.mail.smtp.email import send_email
def sign_up(*,cursor, name, email, password, role):
    # Generate a unique user_id
    user_id = f"{name.lower()[:2]}{random.randint(1000, 9999)}{datetime.datetime.now().microsecond}"
    email = str(email).lower()
    password = str(password)  # Consider hashing this for security
    role = str(role)

    try:
        query = f"INSERT INTO userdata (user_id, name, email, password, role) VALUES ('{user_id}','{name}','{email}','{password}','{role}');"
        # Use parameterized queries to avoid SQL injection
        cursor.execute(query)
        cursor.execute('commit;')
        print("User registered successfully!")
        with open('html/successful_reg.html','r') as file:
                body = file.read()
                

        # Replace the placeholders with dynamic values
        body = body.replace("{{user_id}}", user_id) \
                        .replace("{{name}}", name) \
                        .replace("{{email}}", email) \
                        .replace("{{role}}", role)
            
        send_email(recipient_email=email,subject='Registration successful',body=body,body_type='html')

        return True
    except Exception as e:
        # Handle any exceptions that occur during the execution
        print("!!!ERR!!! signup::", e)
        # Roll back in case of error
        return False

def log_in(*,cursor,email,password):
    try:
        query = f"SELECT user_id, name, email, role FROM userdata WHERE email = '{str(email)}' AND password = '{str(password)}';"
        cursor.execute(query)
        fetchedData = cursor.fetchone()
 
  
        if fetchedData is not None:
                
            userData = {
                "userId":fetchedData[0],
                "name":fetchedData[1],
                "email":fetchedData[2],
                "role":fetchedData[-1]    
            }
            
            
            return userData
        print("No user found")
        return None
        
    except Exception as err:
        print('!!!ERR!!! log_in::',err)
