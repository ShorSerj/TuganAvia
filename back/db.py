import config
import time
import sqlite3
from loguru import logger
from contextlib import closing

logger.add(
    config.os.path.join(config.basedir, "log", "database.log"),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}\n", rotation="00:00", retention="7 days", enqueue=True
)


def connection_for_sqlite_with_attempts(func):
    """
    Decorator to connect the DB
    """

    def func_wraper(*arguments, **kwargs):
        attempts = 5
        while attempts:
            try:
                with sqlite3.connect(config.DATABASE_PATH) as connection:
                    with closing(connection.cursor()) as cursor:
                        return func(cursor, *arguments, **kwargs)
            except sqlite3.Error as e:
                attempts -= 1
                logger.error(f"Attempts left {attempts}, error: {e}")
                time.sleep(30)

        else:
            logger.error("0 attempts left, connection failed")

    return func_wraper


def connection_for_sqlite(func):
    """
    Decorator to connect the DB
    """

    def func_wraper(*arguments, **kwargs):

        # try:
        with sqlite3.connect(config.DATABASE_PATH) as connection:
            with closing(connection.cursor()) as cursor:
                return func(cursor, *arguments, **kwargs)

        # except sqlite3.Error as e:
        #     logger.error(f"Error: {e}")

    return func_wraper