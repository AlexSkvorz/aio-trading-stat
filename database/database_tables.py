from sqlalchemy import Column, CHAR, BigInteger, Date, REAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    tg_id = Column(BigInteger, primary_key=True, unique=True, nullable=False)


class Role(Base):
    __tablename__ = 'role'
    id = Column(BigInteger, ForeignKey('user.tg_id'), primary_key=True)
    role = Column(CHAR(20), nullable=False)


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    tg_id = Column(BigInteger, nullable=False)
    date = Column(Date, nullable=False)
    dollar_amount = Column(REAL, nullable=False)
    dollar_price = Column(REAL, nullable=False)
    rubles_amount = Column(REAL, nullable=False)


class Balance(Base):
    __tablename__ = 'balance'
    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    balance = Column(REAL, nullable=False)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'), nullable=False)


class UserWeekStat(Base):
    __tablename__ = 'user_week_stat'
    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    date = Column(Date)
    tg_id = Column(BigInteger, ForeignKey('operation.id'))
    balance = Column(REAL, nullable=False)
    overall_profit = Column(REAL, nullable=False)
    overall_profit_percent = Column(REAL, nullable=False)
    week_profit = Column(REAL, nullable=False)
    week_profit_percent = Column(REAL, nullable=False)


class WeekStatOverall(Base):
    __tablename__ = 'week_stat_overall'
    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    overall_profit = Column(REAL, nullable=False)
    overall_profit_percent = Column(REAL, nullable=False)
    week_profit = Column(REAL, nullable=False)
    week_profit_percent = Column(REAL, nullable=False)


class Deposit(Base):
    __tablename__ = 'deposit'
    operation_id = Column(BigInteger, ForeignKey('operation.id'), primary_key=True)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'))


class Withdraw(Base):
    __tablename__ = 'withdraw'
    operation_id = Column(BigInteger, ForeignKey('operation.id'), primary_key=True)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'))
