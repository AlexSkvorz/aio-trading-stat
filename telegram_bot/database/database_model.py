from sqlalchemy import Column, CHAR, BigInteger, Date, REAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_real_column():
    return Column(REAL, nullable=False)


class User(Base):
    __tablename__ = 'user'
    tg_id = Column(BigInteger, primary_key=True)


class Role(Base):
    __tablename__ = 'role'
    id = Column(BigInteger, ForeignKey('user.tg_id'), primary_key=True)
    role = Column(CHAR(20), nullable=False)


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(BigInteger, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    date = Column(Date, nullable=False)
    dollar_amount = create_real_column()
    dollar_price = create_real_column()
    rubles_amount = create_real_column()


class Balance(Base):
    __tablename__ = 'balance'
    id = Column(BigInteger, primary_key=True)
    balance = create_real_column()
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'), nullable=False)


class UserWeekStat(Base):
    __tablename__ = 'user_week_stat'
    id = Column(BigInteger, primary_key=True)
    date = Column(Date)
    tg_id = Column(BigInteger, ForeignKey('operation.id'))
    balance = create_real_column()
    overall_profit = create_real_column()
    overall_profit_percent = create_real_column()
    week_profit = create_real_column()
    week_profit_percent = create_real_column()


class WeekStatOverall(Base):
    __tablename__ = 'week_stat_overall'
    id = Column(BigInteger, primary_key=True)
    overall_profit = create_real_column()
    overall_profit_percent = create_real_column()
    week_profit = create_real_column()
    week_profit_percent = create_real_column()


class Deposit(Base):
    __tablename__ = 'deposit'
    operation_id = Column(BigInteger, ForeignKey('operation.id'), primary_key=True)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'))


class Withdraw(Base):
    __tablename__ = 'withdraw'
    operation_id = Column(BigInteger, ForeignKey('operation.id'), primary_key=True)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_id'))
