from itsdangerous import URLSafeTimedSerializer

SECRET_KEY = "sfasdf"
SECURITY_PASSWORD_SALT = "fasdf"

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer('SECRET_KEY')
    return serializer.dumps(email, salt='SECURITY_PASSWORD_SALT')


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer('SECRET_KEY')
    try:
        email = serializer.loads(
            token,
            salt='SECURITY_PASSWORD_SALT',
            max_age=expiration
        )
    except:
        return False
    return email