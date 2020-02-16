import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    
    def add_record(self, Record):
        self.records.append(Record)
    
    def get_today_stats(self):
        now = dt.datetime.now().date()
        self.total = 0
        for day in self.records:
            if day.date == now:
                self.total += day.amount
        return self.total
    
    def get_week_stats(self):
        total_week = 0
        now = dt.datetime.now().date()
        last_week = dt.timedelta(days=7)
        period = now - last_week
        for day in self.records:
            if period <= day.date <= now:
                total_week += day.amount
        return total_week

        
class Record:
    def __init__(self, amount, comment, date = dt.datetime.now().strftime('%d.%m.%Y')):
        self.amount = amount
        self.comment = comment
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        
    def get_calories_remained(self):
        totals = self.get_today_stats()
        if self.limit > totals:
            remains = self.limit - totals
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remains} кКал')
        else:
            return ('Хватит есть!')

class CashCalculator(Calculator):
    USD_RATE = 60.5
    EURO_RATE = 65.5
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        total_maney = self.get_today_stats()
        remains = self.limit - total_maney
        eur_money = float(remains) / self.EURO_RATE
        eur_money_r = round(eur_money, 2)
        usd_money = float(remains) / self.USD_RATE
        usd_money_r = round(usd_money, 2)
        rub_maney = float(remains)
        rub_maney_r = round(rub_maney, 2)
        if remains > 0:
            if currency == 'eur':
                return (f'На сегодня осталось {eur_money_r} Euro')
            elif currency == 'usd':
                return (f'На сегодня осталось {usd_money_r} USD')
            elif currency == 'rub':
                return (f'На сегодня осталось {rub_maney_r} руб')
        elif remains == 0:
                return ('Денег нет, держись')
        elif remains < 0:
            if currency == 'eur':
                return (f'Денег нет, держись: твой долг - {-eur_money_r} Euro')
            elif currency == 'usd':
                return (f'Денег нет, держись: твой долг - {-usd_money_r} USD')
            elif currency == 'rub':
                return (f'Денег нет, держись: твой долг - {-rub_maney_r} руб')


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
print(cash_calculator.get_today_cash_remained("rub"))