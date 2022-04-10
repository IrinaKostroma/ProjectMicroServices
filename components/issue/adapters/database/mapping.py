from sqlalchemy.orm import registry

from issue.adapters.database import tables
from issue.application import dataclasses

mapper = registry()

mapper.map_imperatively(dataclasses.Issue, tables.issues)
