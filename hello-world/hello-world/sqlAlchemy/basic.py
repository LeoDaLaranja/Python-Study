from sqlalchemy import *

'''
This example creates a PostgreSQL engine to communicate with an instance running locally on port 5432. It also defines that it will use usr and pass as the credentials to inreact with the sqlachemy database.

'''
#engine = create_engine()
meta = MetaData()
'''
Relationship Patterns
'''
#One to many
class Article(base):
    __tablename__ = 'arcticles'
    id = Column(Integer,primary_key = True)
    comments= relationship("Comment")

class Coments(base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key= True) 
    article_id = Column(Integer, ForeignKey('articles.id'))


#Many to one

class Tire(base):
    __tablename__ = 'tires'
    id = Column(Integer, primary_key= True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship("Car")

class car(base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)


#One to one 

class Person():
    __tablename__ = "people"
    id = Column(Integer, primary_key= True)
    mobile_phone = relationship("MobilePhone", uselist= False, back_populates = "person")

class MobilePhones():
    __tablename__ = "mobile_phone"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship("Person", back_popuplates = "mobile_phone")

'''

We pass two parameters to the relationship function. 
The first one, uselist=False, makes SQLAlchemy understand that mobile_phone will hold only a single instance and not 
an array (multiple) of instanes.
The second one, back_populates, instructs SQLAlchemy to populate the other side of the mapping
'''

#Many to many 


students_classes_association = Table('students_classes', base.metadata,
        Column('student_id',Integer,ForeignKey('students.id')),
        Column('class_id',Integer,ForeignKey('classes.id'))

)
class Student(Base):
    __tablename = 'students'
    id = Column(Integer,primary_key=True)
    classes = relationship("Class", secondary = students_classes_association)

class Class(base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
'''

In this case, we had to create a helper table to presist the association between instances of Student and instances
of Class, as this wouldn't be possible without an extra table. 

'''