from typing import Union, Tuple

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    IS_DEV_MODE: bool = False
    ALLOW_ORIGINS: Union[str, Tuple[str, ...]] = Field(default_factory=tuple)

    LOGGING_LEVEL: str = 'INFO'

    @property
    def LOGGING_CONFIG(self):
        return {
            'loggers': {
                'gunicorn': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }
