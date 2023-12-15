from Api_orm.db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.column(db.integer, primary_key=True)
    title = db.column(db.string(80), nullable=False, unique=True)
    pages = db.column(db.Float(precision=2), nullable=False)


    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f'BookModel(title={self.title}, pages={self.pages})'

    def json(self):
        return {'title': self.title, 'pages': self.pages}

    @classmethod
    def find_by_title(cls, title):#->"BookModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, id):#->"BookModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):# -> None:
        db.session.delete(self)
        db.session.commit()
