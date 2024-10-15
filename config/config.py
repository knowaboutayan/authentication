import os,dotenv

dotenv.load_dotenv()

DB_HOSTNAME = os.getenv("filess_hostname")
DB_USERNAME = os.getenv("filess_username")
DB_PASSWORD =os.getenv("filess_password")
DB_DATABASE =os.getenv("filess_database")
DB_PORT = os.getenv("filess_port")
JWT_SECRET_KEY = os.getenv("jwt_secret_key")
JWT_ALGORITHM = os.getenv("jwt_algorithm")
