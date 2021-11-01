from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = 'Employee'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, Sequence('Employee_id_seq'))
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return "<Employee(name='%s', fullname='%s', nickname='%s')>" % (
                             self.name, self.fullname, self.nickname)

    reLemployer = relationship("Employer", back_populates="reLemployee")


class Employer(Base):
    __tablename__ = 'Employer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    employee_id = Column(Integer, ForeignKey("Employee.id"))
    
    reLemployee = relationship("Employee", back_populates="reLemployer")

