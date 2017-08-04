# import datetime
# from sqlalchemy import schema, types

# metadata = schema.MetaData()

# def now():
#     return datetime.datetime.now()

# page_table = schema.Table('page', metadata,
#     schema.Column('id', types.Integer,
#         schema.Sequence('page_seq_id', optional=True), primary_key=True),
#     schema.Column('content', types.Text(), nullable=False),
#     schema.Column('posted', types.DateTime(), default=now),
#     schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
#     schema.Column('heading', types.Unicode(255)),
# )

# comment_table = schema.Table('comment', metadata,
#     schema.Column('id', types.Integer,
#         schema.Sequence('comment_seq_id', optional=True), primary_key=True),
#     schema.Column('pageid', types.Integer,
#         schema.ForeignKey('page.id'), nullable=False),
#     schema.Column('content', types.Text(), default=u''),
#     schema.Column('name', types.Unicode(255)),
#     schema.Column('email', types.Unicode(255), nullable=False),
#     schema.Column('created', types.TIMESTAMP(), default=now),
# )

# pagetag_table = schema.Table('pagetag', metadata,
#     schema.Column('id', types.Integer,
#         schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
#     schema.Column('pageid', types.Integer, schema.ForeignKey('page.id')),
#     schema.Column('tagid', types.Integer, schema.ForeignKey('tag.id')),
# )

# tag_table = schema.Table('tag', metadata,
#     schema.Column('id', types.Integer,
#        schema.Sequence('tag_seq_id', optional=True), primary_key=True),
#     schema.Column('name', types.Unicode(20), nullable=False, unique=True),
# )

# class Page(object):
#     pass

# class Comment(object):
#     pass

# class Tag(object):
#     pass

# from sqlalchemy import orm

# orm.mapper(Page, page_table, properties={
#     'comments':orm.relation(Comment, backref='page'),
#     'tags':orm.relation(Tag, secondary=pagetag_table)
#     })

# orm.mapper(Comment, comment_table)
# orm.mapper(Tag, tag_table)

import datetime
from sqlalchemy import schema, types, orm

metadata = schema.MetaData()

def now():
    return datetime.datetime.now()

from sqlalchemy.ext.declarative import declarative_base

# Assign the same metadata object we created earlier.
Base = declarative_base(metadata=metadata)

# We still need the pagetag table because we don't want to explicitly define a
# Pagetag class but still
# need to specify the table in the relation between pages and tags.
pagetag_table = schema.Table('pagetag', metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer, schema.ForeignKey('page.id')),
    schema.Column('tagid', types.Integer, schema.ForeignKey('tag.id')),
)

class Page(Base):
    __tablename__ = 'page'

    id = schema.Column(types.Integer,
        schema.Sequence('page_seq_id', optional=True), primary_key=True)
    content = schema.Column(types.Text(), nullable=False)
    posted = schema.Column(types.DateTime(), default=now)
    title = schema.Column(types.Unicode(255), default=u'Untitled Page')
    heading = schema.Column(types.Unicode(255))
    comments = orm.relation("Comment", backref="page")
    tags = orm.relation("Tag", secondary=pagetag_table)

class Comment(Base):
    __tablename__ = 'comment'

    id = schema.Column(types.Integer,
        schema.Sequence('comment_seq_id', optional=True), primary_key=True)
    pageid = schema.Column(types.Integer,
        schema.ForeignKey('page.id'), nullable=False)
    content = schema.Column(types.Text(), default=u'')
    name = schema.Column(types.Unicode(255))
    email = schema.Column(types.Unicode(255), nullable=False)
    created = schema.Column(types.TIMESTAMP(), default=now())

class Tag(Base):
    __tablename__ = 'tag'

    id = schema.Column(types.Integer,
       schema.Sequence('tag_seq_id', optional=True), primary_key=True)
    name = schema.Column(types.Unicode(20), nullable=False, unique=True)

page_table = Page.__table__