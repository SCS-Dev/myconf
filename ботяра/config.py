settings = {
    
    'info': {
        'TOKEN': '58dd6979c6a78ed66bae5d41299c50b8d54cc624bd43c9e8c4a554077195532a7ac553b0a9bcec1ce4d24', # https://vkhost.github.io (VK ADMIN)
        'ID': 331413425, # Ваш ID (https://regvk.com/id/)
        'DEBUG': True, # Режим разработчика (большее количество логов)
    },


    # Автоматическая выдача работы
    'job_slaves': {
        'ENABLED': True, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'JOBS': ['Майнит биток мне', 'Любимчик', 'котик',], # Случайная работа
    },


    # Автоматическая цепь
    'fet_slaves': {
        'ENABLED': False, #л/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'MAX_PROFIT': False, # Сажать на цепь, только при максимальной профите (1000р)
    },


    # Таргетированое ворование рабов
    'steal_target': {
        'TARGETS': [], # цели для кражи рабов (ID's) (https://regvk.com/id/)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'MIN_PRICE': 0, # Минмальная цена для покупки
        'MAX_PRICE': 90000, # Максимальная цена для покупки
        'AUTO_FET': True, # Автоматически кидать цепь после покупки
    },


    # Ворование рабов у топ-игроков
    'steal_top': {
        'ENABLED': True, # Вкл/Выкл (True/False)
        'MULTI-THREAD': True, # Мультипоточность (💀💀)
        'MIN_PRICE': 0, # Минмальная цена для покупки
        'MAX_PRICE': 90000, # Максимальная цена для покупки
        'AUTO_FET': True # Автоматически кидать цепь после покупки
    },


    # Перепродажа рабов для большей выгоды
    'abuse_slaves': {
        'ENABLED': True, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀💀💀)
        'MIN_BALANCE': 1, # Минимальная цена для абуза
        'AUTO_FET': False, # Автоматически кидать цепь после абуза
        'LIMIT': 19500, # Лимит по цене продажи раба 
    },


    # Покупка минусовых ID
    'abuse_unknowns': {
        'ENABLED': False, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'MIN_PRICE': 0, # Минимальная цена для покупки
        'MAX_PRICE': 100000, # Максимальная цена для покупки
        'AUTO_FET': False, # Автоматически кидать цепь после покупки
    },
    
}
