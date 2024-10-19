class PaymentStrategy:

    def pay(self):
        pass


class CreditCardPayment(PaymentStrategy):

    def pay(self):
        print('Для оплаты картой, приложите её к терминалу:')
        card = input('Приложить карту (да/нет): ')
        if 'да' in card or 'Да' in card or 'ДА' in card:
            print('Оплата прошла успешно!')
        elif 'нет' in card or 'Нет' in card or 'НЕТ' in card:
            print('До новых встреч!')
        else:
            print('Транзакция отклонена.')


class EWalletPayment(PaymentStrategy):

    def pay(self):
        print('Для оплаты электронным кошельком, введите его реквизиты:')
        card = int(input('Ввести реквизиты (8 чисел): '))
        division1 = card // 10000000
        division2 = card // 100000000
        if division1 > 0 and division2 == 0:
            print('Оплата прошла успешно!')
        else:
            print('Введено неверное количество чисел.')


class CashPayment(PaymentStrategy):

    def pay(self):
        print('Для оплаты наличными, внесите купюры:')
        card = input('Внести купюры (да/нет): ')
        if 'да' in card or 'Да' in card or 'ДА' in card:
            bill1 = int(input('Внесите по 1 купюре 5 раз (напечатайте 1):\n'))
            bill2 = int(input())
            bill3 = int(input())
            bill4 = int(input())
            bill5 = int(input())
            if (2 > bill1 > 0) and (2 > bill2 > 0) and (2 > bill3 > 0) and\
                    (2 > bill4 > 0) and (2 > bill5 > 0):
                print('Оплата прошла успешно!')
            else:
                print('Введено неверное количество купюр. Возврат средств...')
        elif 'нет' in card or 'Нет' in card or 'НЕТ' in card:
            print('До новых встреч!')
        else:
            print('Транзакция отклонена.')


class PaymentContext:

    def __init__(self, payment_strategy_value: PaymentStrategy):
        self.payment_strategy = payment_strategy_value

    def payment(self):
        self.payment_strategy.pay()


credit_card_payment = CreditCardPayment()
payment_context = PaymentContext(credit_card_payment)
payment_context.payment()

e_wallet_payment = EWalletPayment()
payment_context = PaymentContext(e_wallet_payment)
payment_context.payment()

cash_payment = CashPayment()
payment_context = PaymentContext(cash_payment)
payment_context.payment()
