from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from ...singleton import Singleton
from ...config import Config


class BaseRepository(Singleton):
    def __init__(self) -> None:
        self.__config = Config()
        self.__engine = create_engine(
            f"{self.__config.database.driver_name}://"
            f"{self.__config.database.user}:{self.__config.database.password}@"
            f"{self.__config.database.host}:{self.__config.database.port}/{self.__config.database.name}"
        )
        self._session: Session = sessionmaker(self.__engine)()
