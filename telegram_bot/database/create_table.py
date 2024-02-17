# import asyncio
from sqlalchemy import Column, CHAR, BigInteger, Date, REAL, create_engine, ForeignKey
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from create_connection import settings

Base = declarative_base()

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)
sync_session_factory = sessionmaker(sync_engine)


# async_engine = create_async_engine(
#    url=settings.DATABASE_URL_asyncpg,
#    echo=True,
# )

# async_session_factory = async_sessionmaker(async_engine)


class User(Base):
    __tablename__ = 'user'
    tg_id = Column(BigInteger, primary_key=True)


class Role(Base):
    __tablename__ = 'role'
    id = Column(BigInteger, ForeignKey('user.tg_id'), primary_key=True)
    role = Column(CHAR(30))


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(BigInteger, primary_key=True)
    tg_id = Column(BigInteger)
    date = Column(Date)
    dollar_amount = Column(REAL)
    dollar_price = Column(REAL)
    rubles_amount = Column(REAL)


class Balance(Base):
    __tablename__ = 'balance'
    id = Column(BigInteger, primary_key=True)
    balance = Column(REAL)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'))


class UserWeekStat(Base):
    __tablename__ = 'user_week_stat'
    id = Column(BigInteger, primary_key=True)
    date = Column(Date)
    tg_id = Column(BigInteger, ForeignKey('operation.id'))
    balance = Column(REAL)
    overall_profit = Column(REAL)
    overall_profit_percent = Column(REAL)
    week_profit = Column(REAL)
    week_profit_percent = Column(REAL)


class WeekStatOverall(Base):
    __tablename__ = 'week_stat_overall'
    id = Column(BigInteger, primary_key=True)
    overall_profit = Column(REAL)
    overall_profit_percent = Column(REAL)
    week_profit = Column(REAL)
    week_profit_percent = Column(REAL)


class Deposit(Base):
    __tablename__ = 'deposit'
    operation_id = Column(BigInteger, ForeignKey('operation.id'), primary_key=True)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'))


class Withdraw(Base):
    __tablename__ = 'withdraw'
    operation_id = Column(BigInteger, ForeignKey('operation.id'), primary_key=True)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'))


def create_tables():
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


create_tables()
