class Dollar():
    def __init__(self):
        pass
    def dollarsize(self, money):
        self.money = money
        m_round = round(money, 2)
        m_list = '.'.split(m_round)

        money = -123456.78901
        m_round = round(money, 2)
        m_list = str(m_round).split('.')
        f_list = list(m_list[0])
        minus = True
        if f_list[0] == '-':
            minus = False
            del f_list[0]

        for i in (range(len(f_list),0, -3)):  
            f_list.insert(i,',')

        del f_list[-1]

        str_list = ''.join(f_list) + '.' + str(m_list[1])

        if minus == False:
            print('-$' + str_list)
        else:
            print('$' + str_list)
