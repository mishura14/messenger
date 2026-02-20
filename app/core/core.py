from app.database.postgres.postgres import db_connect
from app.database.redis.redis import redis_connect
from app.utils.smtp.smtp_server import create_smtp_server

# подключение к бд
db = db_connect()
# подключение к редис серверу
rd = redis_connect()
# подключение к почтовому серверу
server = create_smtp_server()
