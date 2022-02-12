from sqlalchemy import DATETIME, FLOAT, TEXT, VARCHAR, Column, column
from .base_model import Base


class TestResult(Base):
    __tablename__ = "test_result"
    
    id = Column(VARCHAR(36), primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    result = Column(VARCHAR(20), nullable=False)
    date_created = Column(DATETIME, nullable=False)
    type = Column(VARCHAR(12), nullable=False)
    duration = Column(FLOAT)
    log = Column(TEXT)
    std_error = Column(TEXT)
    std_out = Column(TEXT)
