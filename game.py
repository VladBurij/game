# импортируемые модули
import PySide6.QtWidgets as psw 
import PySide6.QtCore as psc
import PySide6.QtGui as psg # модули PySide6 для интерфейса
import random # библиотека random для создания элемента случайности
from dataclasses import dataclass # для более лёгкого создания классов

# Классы внутриигровых объектов
# Класс оружия
@dataclass
class Weapon:
    name: str # название
    physic_attack: int
    termo_attack: int
    chemical_attack: int
    electro_attack: int
    radiation_attack: int
    psyonical_attack: int
    cold_attack: int
    EMI_attack: int # характеристики
    about: str = """Оружие""" # описание
    icon: str = "img\icons\weapon\Стандартная_иконка.png" # ссылка на изображение
# Класс брони
@dataclass
class Armor: 
    name: str # название
    physic_protect: int
    termo_protect: int
    chemical_protect: int
    electro_protect: int
    radiation_protect: int
    psyonical_protect: int
    cold_protect: int
    EMI_protect: int # харакетристики
    about: str = """Броня""" # описание
    icon: str = "img\icons\\armor\Стандартная_иконка.png" # ссылка на изображение
# Класс существа. Это основной класс, который будет наследоваться последующими.
@dataclass
class Creature:
    name: str # имя
    health: int # текущее здоровье
    max_health: int # максимальное здоровье
    physic_attack: int
    termo_attack: int
    chemical_attack: int
    electro_attack: int
    radiation_attack: int
    psyonical_attack: int
    cold_attack: int
    EMI_attack: int # параметры естественной атаки 
    physic_protect: int
    termo_protect: int
    chemical_protect: int
    electro_protect: int
    radiation_protect: int
    psyonical_protect: int
    cold_protect: int
    EMI_protect: int # параметры естественной защиты
    weapon: Weapon = None # используемое оружие
    armor: Armor = None # одетая броня
    krit_chance = 1 # параметр шанса крит.урона
    def attack(self, enemy): # функция атаки противника
        accident = random.randint(1, 20) # шанс случайности промаха.
        if accident == 13: # шанс промаха составляет 5%
            return f"{self.name} промахнулся и не нанёс урон"
        else:
            physic_protect = enemy.physic_protect + enemy.armor.physic_protect
            if physic_protect > 100:
                physic_protect = 100
            termo_protect = enemy.termo_protect + enemy.armor.termo_protect
            if termo_protect > 100:
                termo_protect = 100
            chemical_protect = enemy.chemical_protect + enemy.armor.chemical_protect
            if chemical_protect > 100:
                chemical_protect = 100
            electro_protect = enemy.electro_protect + enemy.armor.electro_protect
            if electro_protect > 100:
                electro_protect = 100
            radiation_protect = enemy.radiation_protect + enemy.armor.radiation_protect
            if radiation_protect > 100:
                radiation_protect = 100
            psyonical_protect = enemy.psyonical_protect + enemy.armor.psyonical_protect
            if psyonical_protect > 100:
                psyonical_protect = 100
            cold_protect = enemy.cold_protect + enemy.armor.cold_protect
            if cold_protect > 100:
                cold_protect = 100
            EMI_protect = enemy.EMI_protect + enemy.armor.EMI_protect
            if EMI_protect > 100:
                EMI_protect = 100
            # здесь вычисляется защита противника - сумма его естественной и броневой защиты, которая может быть не больше 100
            accident = random.randint(1, 15) # шанс нанести крит.урон
            if self.weapon == None: # если нету оружия
                damage = int((self.physic_attack * (100 - physic_protect)/100) + (self.termo_attack * (100 - termo_protect)/100) + (self.chemical_attack * (100 - chemical_protect)/100) + (self.electro_attack * (100 - electro_protect)/100) + (self.radiation_attack * (100 - radiation_protect)/100) + (self.psyonical_attack * (100 - psyonical_protect)/100) + (self.cold_attack * (100 - cold_protect)/100) + (self.EMI_attack * (100 - EMI_protect)/100))
                # общий урон вычисляется по формуле атака игрока * (100 - защита врага/100)
                if accident in range(0, self.krit_chance): # шанс составляет 6,6%, но может быть увеличен
                    enemy.health -= damage * 2 # если выпал крит урон удваивается
                    return f"{enemy.name} получил {damage * 2} критического урона!"
                else:
                    enemy.health -= damage # иначе наносится обычный урон
                    return f"{enemy.name} получил {damage} урона"
            else: # при наличии оружия
                damage = int(self.weapon.physic_attack * (100 - physic_protect)/100) + (self.weapon.termo_attack * (100 - termo_protect)/100) + (self.weapon.chemical_attack * (100 - chemical_protect)/100) + (self.weapon.electro_attack * (100 - electro_protect)/100) + (self.weapon.radiation_attack * (100 - radiation_protect)/100) + (self.weapon.psyonical_attack * (100 - psyonical_protect)/100) + (self.weapon.cold_attack * (100 - cold_protect)/100) + (self.weapon.EMI_attack * (100 - EMI_protect)/100)
                if accident in range(0, self.krit_chance):
                    enemy.health -= damage * 2
                    return f"{enemy.name} получил {damage * 2} критического урона!"
                else:
                    enemy.health -= damage
                    return f"{enemy.name} получил {damage} урона"
    def health_control(self): # функция проверки, что персонаж жив
        if self.health <= 0:
            return False
        else:
            return True
    def get_weapon(self, weapon): # изменение используемого оружия
        self.weapon = weapon
    def get_armor(self, armor): # изменение одетой брони
        self.armor = armor
# Дочерний класс человека
@dataclass
class Human(Creature):
    health: int = 100
    max_health: int = 100
    physic_attack: int = 5
    termo_attack: int = 0
    chemical_attack: int = 0
    electro_attack: int = 0
    radiation_attack: int = 0
    psyonical_attack: int = 0
    cold_attack: int = 0
    EMI_attack: int = 0
    physic_protect: int = 5
    termo_protect: int = 5
    chemical_protect: int = 5
    electro_protect: int = 5
    radiation_protect: int = 5
    psyonical_protect: int = 5
    cold_protect: int = 5
    EMI_protect: int = 100
    about: str = """Обычный человек. Обычный стандартный человек, не отличающийся от нас с вами.
Имеет малую защиту от внешних воздействий и удары кулаков в качестве атаки."""
# Дочерний класс мутанта
@dataclass
class Mutant(Creature):
    health: int = 85
    max_health: int = 85
    physic_attack: int = 5
    termo_attack: int = 0
    chemical_attack: int = 5
    electro_attack: int = 0
    radiation_attack: int = 5
    psyonical_attack: int = 0
    cold_attack: int = 0
    EMI_attack: int = 0
    physic_protect: int = 2
    termo_protect: int = 2
    chemical_protect: int = 70
    electro_protect: int = 2
    radiation_protect: int = 95
    psyonical_protect: int = 5
    cold_protect: int = 5
    EMI_protect: int = 100
    about: str = """Мутировавший организм. По сравнению с обычным человеком у него меньше здоровья 
и защиты от некоторых факторов, но он более устойчив к химии и радиации"""
# Дочерний класс робота
@dataclass
class Robot(Creature):
    health: int = 100
    max_health: int = 100
    physic_attack: int = 15
    termo_attack: int = 0
    chemical_attack: int = 0
    electro_attack: int = 0
    radiation_attack: int = 0
    psyonical_attack: int = 0
    cold_attack: int = 0
    EMI_attack: int = 0
    physic_protect: int = 20
    termo_protect: int = 20
    chemical_protect: int = 100
    electro_protect: int = 5
    radiation_protect: int = 30
    psyonical_protect: int = 100
    cold_protect: int = 40
    EMI_protect: int = 0
    about: str = """Человекоподобный робот. Металлическое тело даёт большую защиту от внешних факторов,
невосприимчив к химии и пси-атакам, однако плохо переносит ЭМИ и электричество"""
# Класс локации
@dataclass
class Location:
    name: str # название
    loc_type: str # тип локации
    enemy: any = None # враг на локации

# Постоянные внутриигровые объекты
# Оружие
knife = Weapon("Армейский нож", 20, 0, 0, 0, 0, 0, 0, 0, """Армейский нож, используемый для
выживания и боя, наносит небольшой физ.урон""", "img\icons\weapon\Нож.png")
termo_knife = Weapon("Энергетический нож", 0, 20, 0, 0, 0, 0, 0, 0, """Энергетический нож, спец.инструмент и оружие
ближнего боя, наносит небольшой термо урон""", "img\icons\weapon\Энерго_нож.png")
electro_dubina = Weapon("Электрическая дубинка", 15, 2, 0, 10, 0, 0, 0, 0, """Электрическая дубинка, предназначена для
ближнего боя, наносит небольшой физический и
электрический урон""", "img\icons\weapon\Электро_дубинка.png")
pistol = Weapon("Пистолет кал .50", 50, 0, 0, 0, 0, 0, 0, 0, """Пистолет с крупным калибром .50
с невероятной мощью, наносит средний физ.урон""", "img\icons\weapon\Пистолет.png")
laser_gun = Weapon("АЛ-94", 0, 50, 0, 0, 0, 0, 0, 0, """Автомат лазерный - основное оружие
военных сил, наносит средний термоурон""", "img\icons\weapon\Лаз_автомат.png")
EMI_gun = Weapon("ЭМВ", 0, 0, 0, 30, 0, 0, 0, 60, """ЭМИ-винтовка, используемая для
уничтожения роботов, наносит урон ЭМИ и электричеством""", "img\icons\weapon\ЭМИ-пушка.png")
rad_gun = Weapon("РадВЛ-14", 0, 0, 0, 0, 60, 0, 0, 0, """Рад-винтовка, наводящая сильную
радиацию на противника, наносит большой рад.урон""", "img\icons\weapon\рад-пушка.png")
# словарь всего вооружения в игре
weapons = {
    "Армейский нож": knife,
    "Энергетический нож": termo_knife,
    "Электрическая дубинка": electro_dubina,
    "Пистолет кал .50": pistol,
    "АЛ-94": laser_gun,
    "ЭМВ": EMI_gun,
    "РадВЛ-14": rad_gun,
}
# Броня
leather_armor = Armor("Кожаная броня", 10, 10, 5, 15, 2, 0, 15, 0, """Кожаная броня, состоящая из плотных
кожанных пластин, хоть как-то защищает""", "img\icons\\armor\Кожаная_броня.png")
metal_armor = Armor("Металлическая броня", 30, 15, 5, 0, 30, 5, 5, 30, """Металлическая броня, состоящая из пластин
стальных сплавов, добротно защищает""", "img\icons\\armor\Металлическая_броня.png")
policy_armor = Armor("Полицейская броня", 25, 20, 10, 40, 15, 5, 15, 10, """Полицейская броня, использовалась спецназом
и полицией, имеет сбалансированную защиту""", "img\icons\\armor\Полицейская_броня.png")
chemical_armor = Armor("Костюм хим.защиты", 15, 30, 90, 50, 90, 30, 55, 45, """Костюм хим.защиты, спец.снаряжения против
радиации и химии, не очень в бою""", "img\icons\\armor\Костюм_хим.защиты.png")
energy_armor = Armor("Энергетическая броня", 20, 60, 15, 70, 40, 90, 10, 90, """Энергетическая броня, сложное устройство из
блоков энегополей, защищает от пси-атак и энергии""", "img\icons\\armor\Энергетическая_броня.png")
military_armor = Armor("Военная броня", 70, 45, 15, 40, 35, 30, 25, 30, """Военная броня, основное снаряжение
военных сил, имеет хорошую боевую защиту""", "img\icons\\armor\Военная_броня.png")
# Словарь всей брони в игре
armors = {
    "Кожаная броня": leather_armor,
    "Металлическая броня": metal_armor,
    "Полицейская броня": policy_armor,
    "Костюм хим.защиты": chemical_armor,
    "Энергетическая броня": energy_armor,
    "Военная броня": military_armor
}
# Боссы, у них будет увеличенное здоровье и шанс критического урона по сравнению с другими противниками
stoormtroper = Human("Штурмовик", 125, 125, weapon = laser_gun, armor = military_armor, about = "Штурмовик, солдат эскадронов смерти, облачённый в мощную броню с автоматом на перевес.")
stoormtroper.krit_chance = 4
killer = Robot("Убийца", 125, 125, weapon = pistol, armor = energy_armor, about = "Робот-убийца, восставший против своих бывших хозяев. Использует энерго-броню и пистолет")
killer.krit_chance = 4
sentinel = Mutant("Страж", 110, 110, weapon = rad_gun, armor = policy_armor, about = "Страж - мутировавший полицейский, до сих пор сторожащий улицы в своей униформе и с рад-винтовкой")
stoormtroper.krit_chance = 4
# Словарь боссов
enemys = {
    "Штурмовик": stoormtroper,
    "Убийца": killer,
    "Страж": sentinel
}

# Особые переменные исключительно для игрока
Player = Human("Игрок", weapon = knife, armor = leather_armor) # сам игрок
inventory_weapon = {} # словарь оружия игрока
inventory_armor = {} # словарь брони игрока
heals = 3 # кол-во аптечек игрока
exp = 0 # опыт игрока
level = 1 # уровень игрока
level_up = 50 # кол-во опыта для перехода на следующий уровень

# Классы окон интерфейса
# Класс окна начального меню
class MenuWindow(psw.QWidget):
    def __init__(self):
        super(MenuWindow, self).__init__()
        self.setWindowTitle("Меню") # название окна
        self.setFixedSize(psc.QSize(200, 100)) # его размеры
        # верхняя надпись
        self.label = psw.QLabel("Меню игры")
        self.label.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование надписи
        # кнопка "Начать играть"
        self.btn1 = psw.QPushButton("Начать играть")
        self.btn1.clicked.connect(self.beginning) # подключение функции "beginning"
        # кнопка "Выход"
        self.btn2 = psw.QPushButton("Выход")
        self.btn2.clicked.connect(self.close) # подключение функции закрытия окна и соотвественно программы
        # вертикальный контейнер
        self.v_layout = psw.QVBoxLayout()
        self.v_layout.addWidget(self.label) # добавление надписи
        self.v_layout.addWidget(self.btn1) # добавление первой кнопки
        self.v_layout.addWidget(self.btn2) # добавление второй кнопки
        self.setLayout(self.v_layout) # установить контейнер основным
    def beginning(self): #функция перехода в меню создания персонажа
        create_player.show()
        self.close()
# Класс окна создания персонажа
class CreatePlayer(psw.QMainWindow):
    def __init__(self):
        super(CreatePlayer, self).__init__()
        self.player_type = random.choice(["Человек", "Мутант", "Робот"]) # случайный начальный тип персонажа
        self.player_weapon = random.choice(list(weapons.keys())) # случайный выбор оружия
        self.player_armor = random.choice(list(armors.keys())) # случайный выбор брони
        self.setWindowTitle("Меню создания персонажа") # название окна
        # верхняя надпись
        self.title1 = psw.QLabel("Создание персонажа") 
        self.title1.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование
        # редактируемая строка имени игрока
        self.person_name = psw.QLineEdit("Игрок")
        # название выбранного типа персонажа
        self.type_person_title = psw.QLabel(self.player_type)
        # описание типа персонажа
        self.about_person = psw.QLabel("Описание")
        # первоначальное описание формируется в зависимости от начального типа
        if self.player_type == "Человек":
            self.about_person.setText(Human.about)
        elif self.player_type == "Мутант":
            self.about_person.setText(Mutant.about)
        elif self.player_type == "Робот":
            self.about_person.setText(Robot.about)
        # выпадающий список выбора типа персонажа
        self.type_person = psw.QComboBox()
        self.type_person.addItems(["Человек", "Мутант", "Робот"]) # добавление вариантов
        self.type_person.currentTextChanged.connect(self.type_changed) # подключение функции изменния описания персонажа
        # вертикальный контейнер создания персонажа
        self.creation_person = psw.QVBoxLayout()
        self.creation_person.addWidget(self.title1) # добавление верхней надписм
        self.creation_person.addWidget(self.person_name) # добавление строки имени персонажа
        self.creation_person.addWidget(self.type_person_title) # добавление название типа персонажа
        self.creation_person.addWidget(self.about_person) # добавление описания типа персонажа
        self.creation_person.addWidget(psw.QLabel("Вы можете поменять тип персонажа ниже:")) # добавление выпадающего списка типа персонажа
        self.creation_person.addWidget(self.type_person) # добавление выпадающего списка типа персонажа
        # верхняя надпись в блоке оружия
        self.title2 = psw.QLabel("Ваше оружие")
        self.title2.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование
        # иконка оружия
        self.icon_weapon = psw.QLabel()
        self.icon_weapon.setPixmap(psg.QPixmap(weapons[self.player_weapon].icon)) # иконка случайного оружия
        # название оружия
        self.name_weapon = psw.QLabel(weapons[self.player_weapon].name)
        # описание оружия
        self.about_weapon = psw.QLabel(weapons[self.player_weapon].about)
        # вертикальный контейнер про оружие
        self.choice_weapon = psw.QVBoxLayout()
        self.choice_weapon.addWidget(self.title2) # добавление верхней надписи
        self.choice_weapon.addWidget(self.icon_weapon) # добавление иконки
        self.choice_weapon.addWidget(self.name_weapon) # добавление названия
        self.choice_weapon.addWidget(self.about_weapon) # добавление описания
        # верхняя надпись в блоке оружия
        self.title3 = psw.QLabel("Ваша броня")
        self.title3.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование
        # иконка брони
        self.icon_armor = psw.QLabel()
        self.icon_armor.setPixmap(psg.QPixmap(armors[self.player_armor].icon)) # иконка случайной брони
        # название брони
        self.name_armor = psw.QLabel(armors[self.player_armor].name)
        # описание брони
        self.about_armor = psw.QLabel(armors[self.player_armor].about)
        # вертикальный контейнер про броню
        self.choice_armor = psw.QVBoxLayout()
        self.choice_armor.addWidget(self.title3) # добавление верхней надписи
        self.choice_armor.addWidget(self.icon_armor) # добавление иконки
        self.choice_armor.addWidget(self.name_armor) # добавление названия
        self.choice_armor.addWidget(self.about_armor) # добавление описания
        # горизонтальный блок снаряжения
        self.chocing_inventory = psw.QHBoxLayout()
        self.chocing_inventory.addLayout(self.choice_weapon) # добавить блок об оружии
        self.chocing_inventory.addLayout(self.choice_armor) # добавить блок о броне
        # кнопка "Создать"
        self.btn1 = psw.QPushButton("Создать") 
        self.btn1.clicked.connect(self.creation_player) # подключение функции "creation_player"
        # кнопка "Выход"
        self.btn2 = psw.QPushButton("Выход")
        self.btn2.clicked.connect(self.exit) # подключение функции "exit"
        # горизонтальный блок кнопок
        self.btns = psw.QHBoxLayout()
        self.btns.addWidget(self.btn1) # добавление первой кнопки
        self.btns.addWidget(self.btn2) # добавление второй кнопки
        # вертикальный главный контейнер
        self.main_layout = psw.QVBoxLayout()
        self.main_layout.addLayout(self.creation_person) # добавление блока о персонаже
        self.main_layout.addLayout(self.chocing_inventory) # добавление блока о снаряжении
        self.main_layout.addLayout(self.btns) # добавление блока кнопок
        # основной виджет
        self.main_widget = psw.QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
    def type_changed(self, text): # функция изменения типа персонажа
        if text == "Человек":
            self.about_person.setText(Human.about) # изменение описания
            self.player_type = "Человек" # изменение типа
            self.type_person_title.setText("Человек") # изменение залоловка
        # аналогично с другими типами
        elif text == "Мутант":
            self.about_person.setText(Mutant.about)
            self.player_type = "Мутант"
            self.type_person_title.setText("Мутант")
        elif text == "Робот":
            self.about_person.setText(Robot.about)
            self.player_type = "Робот"
            self.type_person_title.setText("Робот")
    def creation_player(self): # функция создания персонажа
        global Player
        global inventory_weapon
        global inventory_armor
        inventory_weapon.clear()
        inventory_armor.clear()
        inventory_weapon.update([(self.player_weapon, weapons[self.player_weapon])]) # добавляем оружие
        inventory_armor.update([(self.player_armor, armors[self.player_armor])]) # и броню в инвентарь
        if self.player_type == "Человек":
            Player = Human(self.person_name.text()) # создаём игрока как человека
            Player.get_weapon(weapons[self.player_weapon]) # выдаём ему оружие
            Player.get_armor(armors[self.player_armor]) # и броню
        # аналогично при других типах персонажа
        elif self.player_type == "Мутант":
            Player = Mutant(self.person_name.text())
            Player.get_weapon(weapons[self.player_weapon])
            Player.get_armor(armors[self.player_armor])
        elif self.player_type == "Робот":
            Player = Robot(self.person_name.text())
            Player.get_weapon(weapons[self.player_weapon])
            Player.get_armor(armors[self.player_armor])
        self.close()
        map_window.show()
    def exit(self): # функция перехода из окна создания персонажа в меню
        self.close()
        menu.show()
# Класс окна локаций
class MapWindow(psw.QWidget):
    def __init__(self):
        super(MapWindow, self).__init__()
        self.current_location = "1" # выбранная локация
        self.setWindowTitle("Карта") # название окна
        self.enemyes = 0 # кол-во врагов на локациях
        # словарь локаций, где локации, их тип, и противник генерируются случайно генерируются случайно
        self.locations = {str(i) : Location(str(i), random.choices(["Поле боя", "Лагерь", "Тайник"], [0.8, 0.1, 0.1]), random.choice([Human("Противник", weapon = random.choice(list(weapons.values())), armor = random.choice(list(armors.values()))), Mutant("Противник", weapon = random.choice(list(weapons.values())), armor = random.choice(list(armors.values()))), Robot("Противник", weapon = random.choice(list(weapons.values())), armor = random.choice(list(armors.values())))])) for i in range(1, 11)}
        for key in self.locations:
            if self.locations[key].loc_type[0] == "Поле боя": # в случае если это поле битвы
                self.enemyes += 1
        # верхняя надпись
        self.label = psw.QLabel("""Ниже представлены доступные вам локации. 
Будьте осторожны при их исследовании""")
        self.label.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование надписи
        # кнопки локаций
        self.loc1 = psw.QPushButton("Заброшенное метро")
        self.loc1.clicked.connect(self.loc_change_1) # подключение функции изменения выбранной локации
        self.loc2 = psw.QPushButton("Пустой квартал")
        self.loc2.clicked.connect(self.loc_change_2)
        self.loc3 = psw.QPushButton("Руины небоскрёбов")
        self.loc3.clicked.connect(self.loc_change_3)
        self.loc4 = psw.QPushButton("Сталелитейный завод")
        self.loc4.clicked.connect(self.loc_change_4)
        self.loc5 = psw.QPushButton("Поселение в лесу")
        self.loc5.clicked.connect(self.loc_change_5)
        self.loc6 = psw.QPushButton("Бывший НИИ")
        self.loc6.clicked.connect(self.loc_change_6)
        self.loc7 = psw.QPushButton("Блокпост на дороге")
        self.loc7.clicked.connect(self.loc_change_7)
        self.loc8 = psw.QPushButton("Мёртвое побережье")
        self.loc8.clicked.connect(self.loc_change_8)
        self.loc9 = psw.QPushButton("Тайный бункер")
        self.loc9.clicked.connect(self.loc_change_9)
        self.loc10 = psw.QPushButton("Крупная радиовышка")
        self.loc10.clicked.connect(self.loc_change_10)
        self.loc11 = psw.QPushButton("Боссы")
        self.loc11.setEnabled(False) # первоначально боссы будут заблокированны
        self.loc11.clicked.connect(self.loc_change_11)
        # надпись описания локации
        self.location_about = psw.QLabel("Перед вами раскинулись бескрайние пустоши. Куда бы пойти?")
        # кнопка "Инвентарь"
        self.btn1 = psw.QPushButton("Инвентарь")
        self.btn1.clicked.connect(self.inventory) # подключение функции "inventory"
        # кнопка "Исследовать"
        self.btn2 = psw.QPushButton("Исследовать")
        self.btn2.clicked.connect(self.explore) # подключение функции перехода в локации
        # вертикальный контейнер локаций
        self.v_layout = psw.QVBoxLayout()
        self.v_layout.addWidget(self.label) # добавление надписи
        self.v_layout.addWidget(self.loc1) # добавление кнопок
        self.v_layout.addWidget(self.loc2)
        self.v_layout.addWidget(self.loc3)
        self.v_layout.addWidget(self.loc4)
        self.v_layout.addWidget(self.loc5)
        self.v_layout.addWidget(self.loc6)
        self.v_layout.addWidget(self.loc7)
        self.v_layout.addWidget(self.loc8)
        self.v_layout.addWidget(self.loc9)
        self.v_layout.addWidget(self.loc10)
        self.v_layout.addWidget(self.loc11)
        self.v_layout.addWidget(self.location_about) # добавление описания локации
        # горизонтальный контейнер кнопок
        self.h_layout = psw.QHBoxLayout()
        self.h_layout.addWidget(self.btn1) # добавление первой кнопки
        self.h_layout.addWidget(self.btn2) # добавление второй кнопки
        # главный вертикальный контейнер
        self.main_layout = psw.QVBoxLayout()
        self.main_layout.addLayout(self.v_layout)
        self.main_layout.addLayout(self.h_layout)
        self.setLayout(self.main_layout) # установить контейнер основным
    def loc_change_1(self):
        self.current_location = "1" # изменение выбранной локации
        self.location_about.setText("Уже не действующая и частично затопленная станция метро") # изменение описания
    def loc_change_2(self):
        self.current_location = "2"
        self.location_about.setText("Когда-то это был жилой квартал, но сейчас тут толком никого")
    def loc_change_3(self):
        self.current_location = "3"
        self.location_about.setText("Шаткие бетонные громадины, в которых возможно что-то есть")
    def loc_change_4(self):
        self.current_location = "4"
        self.location_about.setText("Печи уже давно остыли, а из труб перестал валить дым")
    def loc_change_5(self):
        self.current_location = "5"
        self.location_about.setText("Удалённое лесное поселение в глубине чащи. Хорошее укрытие")
    def loc_change_6(self):
        self.current_location = "6"
        self.location_about.setText("Здесь проводились разные исследования, возможно полезные")
    def loc_change_7(self):
        self.current_location = "7"
        self.location_about.setText("Посреди дороги расположилось КПП, подозрительно пустое КПП")
    def loc_change_8(self):
        self.current_location = "8"
        self.location_about.setText("Длинное песчанное побережье с несколькими домиками у берега")
    def loc_change_9(self):
        self.current_location = "9"
        self.location_about.setText("Хорошо скрытый и укреплённый бункер посреди холмов и лесов")
    def loc_change_10(self):
        self.current_location = "10"
        self.location_about.setText("Высокую антенну этой радиовышки видно на много километров")
    def loc_change_11(self):
        self.current_location = "boss"
        self.location_about.setText("В округе ходят легенды о могучих бойцах. Наведаемся к ним?")
    def inventory(self): #функция перехода в окно инвентаря
        inv.update_inventory() # обновление инвентаря
        inv.window_before = "map_window" # обозначение предыдущего окна
        inv.show()
        self.close()
    def explore(self): # функция исследования локации
        global inventory_weapon
        global inventory_armor
        global heals
        global fight
        if self.current_location == "boss":
            self.close
            bosses.show()
        else:
            if self.locations[self.current_location].loc_type[0] == "Тайник": # в случае если это тайник
                random_weapon = random.choice(list(weapons.values()) + [None]) # генерируется случайное оружие
                random_armor = random.choice(list(armors.values()) + [None]) # генерируется случайная броня
                random_heals = random.randint(0, 4) # генерируется случайное количество аптечек
                # окно сообщения о тайнике
                habar = psw.QMessageBox(self)
                habar.setWindowTitle("Вы обнаружили тайник")
                if random_weapon == None and random_armor == None and random_heals == 0: # если ничего нет
                    habar.setText("Вот невезенье! Этот тайник совсем пустой!")
                    looting = habar.exec_()
                if random_weapon != None and random_armor == None and random_heals == 0: # если только оружие
                    habar.setText(f"А вот и оружие! Вы получили {random_weapon.name}.")
                    looting = habar.exec_()
                    if looting == psw.QMessageBox.Ok:
                        inventory_weapon.update({random_weapon.name: random_weapon})
                if random_weapon == None and random_armor != None and random_heals == 0: # если только броня
                    habar.setText(f"Отлично, броня! Вы получили {random_armor.name}.")
                    looting = habar.exec_()
                    if looting == psw.QMessageBox.Ok:
                        inventory_armor.update({random_armor.name: random_armor})
                if random_weapon == None and random_armor == None and random_heals > 0: # если только аптечки
                    habar.setText(f"О, медикаменты! Вы получили {random_heals} аптечки.")
                    looting = habar.exec_()
                    if looting == psw.QMessageBox.Ok:
                        heals += random_heals
                if random_weapon != None and random_armor != None and random_heals == 0: # если оружие и броня
                    habar.setText(f"""Неплохой боевой наборчик!
Вы получили {random_weapon.name} и {random_armor.name}.""")
                    looting = habar.exec_()
                    if looting == psw.QMessageBox.Ok:
                        inventory_weapon.update({random_weapon.name: random_weapon})
                        inventory_armor.update({random_armor.name: random_armor})
                if random_weapon != None and random_armor == None and random_heals > 0: # если оружие и аптечки
                    habar.setText(f"""У вас в руках смерть и жизнь! 
Вы получили {random_weapon.name} и {random_heals} аптечки.""")
                    looting = habar.exec_()
                    if looting == psw.QMessageBox.Ok:
                        inventory_weapon.update({random_weapon.name: random_weapon})
                        heals += random_heals
                if random_weapon == None and random_armor != None and random_heals > 0: # если броня и аптечки
                    habar.setText(f"""Здоровье точно будет в порядке! 
Вы получили {random_armor.name} и {random_heals} аптечки.""")
                    looting = habar.exec_()
                    if looting == psw.QMessageBox.Ok:
                        inventory_armor.update({random_armor.name: random_armor})
                if random_weapon != None and random_armor != None and random_heals > 0: # если полный набор
                    habar.setText(f"""Вот это куча снаряжения на все случаи! 
Вы получили {random_weapon.name}, {random_armor.name} и {random_heals} аптечки!""")
                    looting = habar.exec_()
                    if looting == psw.QMessageBox.Ok:
                        inventory_weapon.update({random_weapon.name: random_weapon})
                        inventory_armor.update({random_armor.name: random_armor})
                        heals += random_heals
                exec(f"self.loc{self.current_location}.setEnabled(False)") # блокировка кнопки локации
                self.current_location = "0" # изменение на начальную выбранную локацию
                self.location_about.setText("В этом тайнике теперь точно ничего нет. Пора идти дальше") # изменение описания внизу окна
            elif self.locations[self.current_location].loc_type[0] == "Лагерь": # в случае если это лагерь
                if Player.health == Player.max_health: # если персонаж полностью здоров
                    exec(f"""if "(лагерь)" not in self.loc{self.current_location}.text():
        self.loc{self.current_location}.setText(self.loc{self.current_location}.text() + " (лагерь)")""") # добавление лагеря в кнопке если он ещё не обозначен
                    self.location_about.setText("Это место оказалось лагерем. Нужно запомнить на будущее.") # изменение описания внизу окна
                else:
                    Player.health += random.randint(10,15) # восстановление здоровья персонажу
                    if Player.health > Player.max_health:
                        Player.health = Player.max_health # текущее здоровье не может быть больше максимального
                    exec(f"""if "(лагерь)" not in self.loc{self.current_location}.text():
        self.loc{self.current_location}.setText(self.loc{self.current_location}.text() + " (лагерь)")""") # добавление лагеря в кнопке если он ещё не обозначен
                    self.location_about.setText("Вы нашли лагерь, где хорошо отдохнули и набрались сил.") # изменение описания внизу окна
                    exec(f"self.loc{self.current_location}.setEnabled(False)") # блокировка кнопки
            elif self.locations[self.current_location].loc_type[0] == "Поле боя": # в случае если это поле битвы
                fight = FightWindow(self.locations[self.current_location].enemy) # меняем противника в окне битвы
                battle = psw.QMessageBox(self)
                battle.setWindowTitle("Нападение!")
                if self.locations[self.current_location].enemy.physic_protect == 5: # если противник человек
                    battle.setText(f"""Похоже кроме вас здесь ещё кто-то есть!
Судя по внешнему виду это человек.
Его оружие: {self.locations[self.current_location].enemy.weapon.name}
Его броня: {self.locations[self.current_location].enemy.armor.name}
Приготовиться к бою!""")
                elif self.locations[self.current_location].enemy.physic_protect == 2: # если противник мутант
                    battle.setText(f"""Похоже кроме вас здесь ещё кто-то есть!
Судя по внешнему виду это мутант.
Его оружие: {self.locations[self.current_location].enemy.weapon.name}
Его броня: {self.locations[self.current_location].enemy.armor.name}
Приготовиться к бою!""")
                else: # если противник робот
                    battle.setText(f"""Похоже кроме вас здесь ещё кто-то есть!
Судя по внешнему виду это робот.
Его оружие: {self.locations[self.current_location].enemy.weapon.name}
Его броня: {self.locations[self.current_location].enemy.armor.name}
Приготовиться к бою!""")
                battle_field = battle.exec_()
                if battle_field == psw.QMessageBox.Ok:
                    fight.show() # переход в окно битвы
                    self.close()
# Класс окна инвентаря персонажа
class InvWindow(psw.QMainWindow):
    def __init__(self):
        super(InvWindow, self).__init__()
        self.window_before = "" # название окна откуда было открыто окно инвентаря
        self.setWindowTitle("Инвентарь персонажа")
        # заголовок блока о персонаже
        self.title1 = psw.QLabel("Характеристики персонажа")
        self.title1.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование надписи
        # имя персонажа
        self.player_name = psw.QLabel(f"Имя: {Player.name}")
        # здоровье персонажа
        self.player_health = psw.QLabel(f"Здоровье: {Player.health}/{Player.max_health}")
        # уровень персонажа
        self.player_level = psw.QLabel(f"Уровень: {level}")
        # опыт персонажа
        self.player_exp = psw.QLabel(f"Опыт: {exp}/{level_up}")
        # тип персонажа
        self.player_type = psw.QLabel(f"Тип: {create_player.player_type}")
        # описание типа персонажа
        self.player_type_about = psw.QLabel(create_player.about_person)
        # вертикальный контейнер информации о персонаже
        self.about_player = psw.QVBoxLayout()
        self.about_player.addWidget(self.title1) # добавление заголовка
        self.about_player.addWidget(self.player_name) # добавление имени персонажа
        self.about_player.addWidget(self.player_health) # добавление здоровья персонажа
        self.about_player.addWidget(self.player_level) # добавление уровня
        self.about_player.addWidget(self.player_exp) # добавление опыта
        self.about_player.addWidget(self.player_type) # добавление типа персонажа
        self.about_player.addWidget(self.player_type_about) # добавление описания типа персонажа
        # заголовок блока об оружии
        self.title2 = psw.QLabel("Выбор оружия") 
        self.title2.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование
        # иконка оружия
        self.icon_weapon = psw.QLabel() 
        self.icon_weapon.setPixmap(psg.QPixmap(Player.weapon.icon))
        # выпадающий список оружия
        self.list_weapon = psw.QComboBox()
        self.list_weapon.addItems(["-"]) # без оружия
        self.list_weapon.currentTextChanged.connect(self.weapon_changed) # подключение функции изменения оружия
        # описание оружия
        self.about_weapon = psw.QLabel("Что ж, обычными кулаками тоже можно биться")
        # характеристики оружия
        self.physic_attack = psw.QLabel("Физический: -")
        self.termo_attack = psw.QLabel("Термический: -")
        self.chemical_attack = psw.QLabel("Химический: -")
        self.electro_attack = psw.QLabel("Электрический: -")
        self.radiation_attack = psw.QLabel("Радиационный: -")
        self.psyonical_attack = psw.QLabel("Псионический: -")
        self.cold_attack = psw.QLabel("Крионический: -")
        self.EMI_attack = psw.QLabel("ЭМИ: -")
        # вертикальный блок выбора оружия
        self.choice_weapon = psw.QVBoxLayout()
        self.choice_weapon.addWidget(self.title2) # добавление заголовка
        self.choice_weapon.addWidget(self.icon_weapon) # добавление иконки
        self.choice_weapon.addWidget(self.list_weapon) # добавление выпадающего списка
        self.choice_weapon.addWidget(self.about_weapon) # добавление описания
        self.choice_weapon.addWidget(psw.QLabel("Наносимый урон")) # добавление надписи
        self.choice_weapon.addWidget(self.physic_attack) # добавление характеристик
        self.choice_weapon.addWidget(self.termo_attack)
        self.choice_weapon.addWidget(self.chemical_attack)
        self.choice_weapon.addWidget(self.electro_attack)
        self.choice_weapon.addWidget(self.radiation_attack)
        self.choice_weapon.addWidget(self.psyonical_attack)
        self.choice_weapon.addWidget(self.cold_attack)
        self.choice_weapon.addWidget(self.EMI_attack)
        # заголовок блока о броне
        self.title3 = psw.QLabel("Выбор брони")
        self.title3.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование
        # иконка брони
        self.icon_armor = psw.QLabel()
        self.icon_armor.setPixmap(psg.QPixmap(Player.armor.icon))
        # выпадающий список брони
        self.list_armor = psw.QComboBox()
        self.list_armor.addItems(["-"]) # без брони
        self.list_armor.currentTextChanged.connect(self.armor_changed) # подключение функции изменения брони
        # описание брони
        self.about_armor = psw.QLabel("Без брони и снаряжения вы долго не проживёте")
        # характеристики брони
        self.physic_protect = psw.QLabel("Физический: -")
        self.termo_protect = psw.QLabel("Термический: -")
        self.chemical_protect = psw.QLabel("Химический: -")
        self.electro_protect = psw.QLabel("Электрический: -")
        self.radiation_protect = psw.QLabel("Радиационный: -")
        self.psyonical_protect = psw.QLabel("Псионический: -")
        self.cold_protect = psw.QLabel("Крионический: -")
        self.EMI_protect = psw.QLabel("ЭМИ: -")
        # вертикальный блок о броне
        self.choice_armor = psw.QVBoxLayout()
        self.choice_armor.addWidget(self.title3) # добавление заголовка
        self.choice_armor.addWidget(self.icon_armor) # добавление иконки
        self.choice_armor.addWidget(self.list_armor) # добавление выпадающего списка
        self.choice_armor.addWidget(self.about_armor) # добавление описания
        self.choice_armor.addWidget(psw.QLabel("Защита от факторов")) # добавление надписи
        self.choice_armor.addWidget(self.physic_protect) # добавление характеристик
        self.choice_armor.addWidget(self.termo_protect)
        self.choice_armor.addWidget(self.chemical_protect)
        self.choice_armor.addWidget(self.electro_protect)
        self.choice_armor.addWidget(self.radiation_protect)
        self.choice_armor.addWidget(self.psyonical_protect)
        self.choice_armor.addWidget(self.cold_protect)
        self.choice_armor.addWidget(self.EMI_protect)
        # горизонтальный блок снаряжения
        self.chocing_inventory = psw.QHBoxLayout()
        self.chocing_inventory.addLayout(self.choice_weapon) # добавление блока об оружии
        self.chocing_inventory.addLayout(self.choice_armor) # добавление блока о броне
        # кнопка "Лечение"
        self.btn1 = psw.QPushButton(f"Лечение ({heals})")
        self.btn1.clicked.connect(self.healing) # подключение функции лечения
        # кнопка "Закрыть"
        self.btn2 = psw.QPushButton("Закрыть")
        self.btn2.clicked.connect(self.exit) # подключение выхода из инвентаря
        # горизонтальный блок кнопок
        self.btns = psw.QHBoxLayout()
        self.btns.addWidget(self.btn1) # добавление кнопки лечения
        self.btns.addWidget(self.btn2) # добавление кнопки выхода
        # основной блок
        self.main_layout = psw.QVBoxLayout() 
        self.main_layout.addLayout(self.about_player) # добавление блока о игроке
        self.main_layout.addLayout(self.chocing_inventory) # добавление блока инвенторя
        self.main_layout.addLayout(self.btns) # добавление блока кнопок 
        self.main_widget = psw.QWidget() 
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
    def update_inventory(self): # обновление данных инвентаря
        # обновление данных о персонаже
        self.player_name.setText(f"Имя: {Player.name}")
        self.player_health.setText(f"Здоровье: {Player.health}/{Player.max_health}")
        self.player_level.setText(f"Уровень: {level}")
        self.player_exp.setText(f"Опыт: {exp}/{level_up}")
        self.player_type.setText(f"Тип: {create_player.player_type}")
        self.player_type_about.setText(create_player.about_person.text())
        for i in inventory_weapon: # добавление новых элементов в список из инвенаря
            if i not in [self.list_weapon.itemText(n) for n in range(self.list_weapon.count())]: # только если этого элемента не было  всписке
                self.list_weapon.addItems([i])
        # обновление данных с оружием и без
        if Player.weapon == None:
            self.icon_weapon.setPixmap(psg.QPixmap("img\icons\weapon\Стандартная_иконка.png"))
            self.physic_attack.setText(f"Физический: {Player.physic_attack}")
            self.termo_attack.setText(f"Термический: {Player.termo_attack}")
            self.chemical_attack.setText(f"Химический: {Player.chemical_attack}")
            self.electro_attack.setText(f"Электрический: {Player.electro_attack}")
            self.radiation_attack.setText(f"Радиационный: {Player.radiation_attack}")
            self.psyonical_attack.setText(f"Псионический: {Player.psyonical_attack}")
            self.cold_attack.setText(f"Крионический: {Player.cold_attack}")
            self.EMI_attack.setText(f"ЭМИ: {Player.EMI_attack}")
            self.about_weapon.setText("Что ж, обычными кулаками тоже можно биться")
        else:
            self.icon_weapon.setPixmap(psg.QPixmap(Player.weapon.icon))
            self.physic_attack.setText(f"Физический: {Player.weapon.physic_attack}")
            self.termo_attack.setText(f"Термический: {Player.weapon.termo_attack}")
            self.chemical_attack.setText(f"Химический: {Player.weapon.chemical_attack}")
            self.electro_attack.setText(f"Электрический: {Player.weapon.electro_attack}")
            self.radiation_attack.setText(f"Радиационный: {Player.weapon.radiation_attack}")
            self.psyonical_attack.setText(f"Псионический: {Player.weapon.psyonical_attack}")
            self.cold_attack.setText(f"Крионический: {Player.weapon.cold_attack}")
            self.EMI_attack.setText(f"ЭМИ: {Player.weapon.EMI_attack}")
            self.about_weapon.setText(Player.weapon.about)
        for i in inventory_armor: # добавление брони из инвенаря в список
            if i not in [self.list_armor.itemText(n) for n in range(self.list_armor.count())]: # только если этой брони ещё нет
                self.list_armor.addItems([i])
        # обновление данных с бронёй и без
        if Player.armor == None:
            self.icon_armor.setPixmap(psg.QPixmap("img\icons\\armor\Стандартная_иконка.png"))
            self.physic_protect.setText(f"Физический: {Player.physic_protect}")
            self.termo_protect.setText(f"Термический: {Player.termo_protect}")
            self.chemical_protect.setText(f"Химический: {Player.chemical_protect}")
            self.electro_protect.setText(f"Электрический: {Player.electro_protect}")
            self.radiation_protect.setText(f"Радиационный: {Player.radiation_protect}")
            self.psyonical_protect.setText(f"Псионический: {Player.psyonical_protect}")
            self.cold_protect.setText(f"Крионический: {Player.cold_protect}")
            self.EMI_protect.setText(f"ЭМИ: {Player.EMI_protect}")
            self.about_armor.setText("Без брони и снаряжения вы долго не проживёте")
        else:
            self.icon_armor.setPixmap(psg.QPixmap(Player.armor.icon))
            self.physic_protect.setText(f"Физический: {Player.armor.physic_protect + Player.physic_protect}")
            self.termo_protect.setText(f"Термический: {Player.armor.termo_protect + Player.termo_protect}")
            self.chemical_protect.setText(f"Химический: {Player.armor.chemical_protect + Player.chemical_protect}")
            self.electro_protect.setText(f"Электрический: {Player.armor.electro_protect + Player.electro_protect}")
            self.radiation_protect.setText(f"Радиационный: {Player.armor.radiation_protect + Player.radiation_protect}")
            self.psyonical_protect.setText(f"Псионический: {Player.armor.psyonical_protect + Player.psyonical_protect}")
            self.cold_protect.setText(f"Крионический: {Player.armor.cold_protect + Player.cold_protect}")
            self.EMI_protect.setText(f"ЭМИ: {Player.armor.EMI_protect + Player.EMI_protect}")
            self.about_armor.setText(Player.armor.about)
        self.btn1.setText(f"Лечение ({heals})") # обновление кличества аптечек
        self.btn1.setEnabled(Player.health < Player.max_health and heals > 0) # доступность кнопки определяется наличием аптечек, а также отношением текущего здоровья к максимальному
    def healing(self): # функция лечения
        global heals
        heals -= 1 # трата аптечки
        self.btn1.setText(f"Лечение ({heals})") # изменение отображаемого кол-ва аптечек
        Player.health += random.randint(15,30) # аптечка восстанавливает случайное кол-во здоровья
        if heals == 0: # если аптечки заканчиваются, то кнопка блокируется
            self.btn1.setEnabled(False)
        if Player.health > Player.max_health: # если здоровье полностью восстановлено, то кнопка блокируется
            Player.health = Player.max_health # текущее здоровье не может быть больше максимального
            self.btn1.setEnabled(False)
        self.player_health.setText(f"Здоровье: {Player.health}/{Player.max_health}") # изменение отображения здоровья
    def weapon_changed(self, name): # изменение характеристик оружия
        if name == "-": # выбор без оружия
            Player.weapon = None # меняется оружие игрока
        else:
            Player.weapon = weapons[name]
        self.update_inventory()
    def armor_changed(self, name):
        if name == "-": # выбор без брони
            Player.armor = None
        else:
            Player.armor = armors[name]
        self.update_inventory()
    def exit(self): # функция выхода из окна
        self.close()
        if self.window_before == "fight": # если переход был из окна боя, то оно обновляется
            fight.update_info()
        elif self.window_before == "bossfight": # если переход был из окна боя с боссом, то оно обновляется
            bossfight.update_info()
        exec(f"{self.window_before}.show()")
# Класс окна битвы
class FightWindow(psw.QWidget):
    def __init__(self, enemy):
        super(FightWindow, self).__init__() 
        self.enemy = enemy # объект противник
        self.setWindowTitle("Бой") # название окна
        # имя противника
        self.enemy_name = psw.QLabel(self.enemy.name)
        # тип противника
        if self.enemy.physic_protect == 5: # если противник человек
            self.enemy_type = psw.QLabel("Тип: Человек")
        elif self.enemy.physic_protect == 2: # если противник мутант
            self.enemy_type = psw.QLabel("Тип: Мутант")
        else: # если противник робот
            self.enemy_type = psw.QLabel("Тип: Робот")
        # здоровье противника
        self.enemy_health = psw.QLabel(f"Здоровье: {self.enemy.health}/{self.enemy.max_health}")
        # оружие противника
        self.enemy_weapon = psw.QLabel(f"Оружие: {self.enemy.weapon.name}")
        # броня противника
        self.enemy_armor = psw.QLabel(f"Броня: {self.enemy.armor.name}")
        # разделитель
        self.space = psw.QLabel("") 
        # имя игрока
        self.player_name = psw.QLabel(Player.name)
        # тип игрока (поскольку игрок может увеличить свою естественную защиту, то его тип определяется через описание)
        if "человек" in Player.about: # если игрок человек
            self.player_type = psw.QLabel("Тип: Человек")
        elif "Мутировавший" in Player.about: # если игрок мутант
            self.player_type = psw.QLabel("Тип: Мутант")
        else: # если игрок робот
            self.player_type = psw.QLabel("Тип: Робот")
        # здоровье игрока
        self.player_health = psw.QLabel(f"Здоровье: {Player.health}/{Player.max_health}")
        # оружие игрока
        self.player_weapon = psw.QLabel(f"Оружие: {Player.weapon.name}")
        # броня игрока
        self.player_armor = psw.QLabel(f"Броня: {Player.armor.name}")
        # горизонтальная разделительная линия
        self.horzont_line = psw.QLabel("_________________________________________")
        self.horzont_line.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование надписи
        # первая информационная строка
        self.information1 = psw.QLabel("")
        # вторая информационная строка
        self.information2 = psw.QLabel("Начинается бой! Атакуйте или отступите!")
        # кнопка атаки
        self.attack_btn = psw.QPushButton("Атаковать")
        self.attack_btn.clicked.connect(self.attack) # подключение функции атаки
        # кнопка инвентаря
        self.inventory_btn = psw.QPushButton("Инвентарь")
        self.inventory_btn.clicked.connect(self.inventory) # функция для перехода в окно карты
        # кнопка отсупления
        self.exit_btn = psw.QPushButton("Отступить")
        self.exit_btn.clicked.connect(self.exit) # функция для перехода в окно карты
        # горизонтальный контейнер кнопок
        self.btns = psw.QHBoxLayout()
        self.btns.addWidget(self.attack_btn) # добавление кнопки атаки
        self.btns.addWidget(self.inventory_btn) # добавление кнопки инвентаря
        self.btns.addWidget(self.exit_btn) # добавление кнопки ухода
        # основной вертикальный контейнер
        self.main_layout = psw.QVBoxLayout()
        self.main_layout.addWidget(self.enemy_name) # добавление информации о противнике
        self.main_layout.addWidget(self.enemy_type)
        self.main_layout.addWidget(self.enemy_health)
        self.main_layout.addWidget(self.enemy_weapon)
        self.main_layout.addWidget(self.enemy_armor)
        self.main_layout.addWidget(self.space) # добавление пустого пространства
        self.main_layout.addWidget(self.player_name) # добавление информации о игроке
        self.main_layout.addWidget(self.player_type)
        self.main_layout.addWidget(self.player_health)
        self.main_layout.addWidget(self.player_weapon)
        self.main_layout.addWidget(self.player_armor)
        self.main_layout.addWidget(self.horzont_line) # добавление разделительной черты
        self.main_layout.addWidget(self.information1) # добавление 1-й информационной строки
        self.main_layout.addWidget(self.information2) # добавление 2-й информационной строки
        self.main_layout.addLayout(self.btns) # добавление блока кнопок
        self.setLayout(self.main_layout) # закрепление основного контейнера
    def exit(self): # функция выхода из окна битвы
        self.enemy.health = self.enemy.max_health
        self.close()
        map_window.show()
    def inventory(self): # функция перехода в инвентарь
        self.close()
        inv.window_before = "fight"
        inv.update_inventory()
        inv.show()
    def update_info(self): # функция обновления данных
        self.enemy_health.setText(f"Здоровье: {self.enemy.health}/{self.enemy.max_health}")
        self.player_health.setText(f"Здоровье: {Player.health}/{Player.max_health}")
        self.player_weapon.setText(f"Оружие: {Player.weapon.name}")
        self.player_armor.setText(f"Броня: {Player.armor.name}")
    def attack(self): # функция атаки противника
        global exp
        global inventory_weapon
        global inventory_armor
        global heals
        global level
        global level_up
        self.information2.setText(Player.attack(self.enemy)) # игрок атакует противника
        self.update_info() # обновление информации
        if self.enemy.health_control() == False: # если противник повержен (здоровье 0 и меньше)
            self.information1.setText("")
            self.information2.setText(f"Вы одолели {self.enemy.name} в бою!")
            # информационное окно о победе
            win = psw.QMessageBox(self)
            win.setWindowTitle("Вы победили!")
            # случайное кол-во опыта, рассчитывающееся как (сумма атаки оружия + средняя защита брони) +- 20%
            random_exp = int((self.enemy.weapon.physic_attack + self.enemy.weapon.termo_attack + self.enemy.weapon.chemical_attack + self.enemy.weapon.electro_attack + self.enemy.weapon.radiation_attack + self.enemy.weapon.psyonical_attack + self.enemy.weapon.cold_attack + self.enemy.weapon.EMI_attack + (self.enemy.armor.physic_protect + self.enemy.armor.termo_protect + self.enemy.armor.chemical_protect + self.enemy.armor.electro_protect + self.enemy.armor.radiation_protect + self.enemy.armor.psyonical_protect + self.enemy.armor.cold_protect + self.enemy.armor.EMI_protect) / 8) * (1 + 0.01 * random.randint(-20, 20)))
            exp += random_exp # прибавление опыта
            # случайное число медикаментов
            random_heals = random.randint(0, 3)
            inventory_weapon.update({self.enemy.weapon.name: self.enemy.weapon}) # добавление оружия в инвентарь
            inventory_armor.update({self.enemy.armor.name: self.enemy.armor}) # добавление брони в инвентарь
            heals += random_heals # добавление аптечек
            map_window.locations[map_window.current_location].loc_type[0] = "Лагерь" # изменение типа локации на лагерь
            map_window.locations[map_window.current_location].enemy = None # убираем противника с локации
            exec(f"""map_window.loc{map_window.current_location}.setText(map_window.loc{map_window.current_location}.text() + " (лагерь)")""") # добавление лагеря в кнопке локации карты
            map_window.location_about.setText("Что ж, после зачистки это место вполне можно сделать лагерем") # изменение описания внизу окна карты
            map_window.enemyes -= 1 # кол-во врагов уменьшается
            if map_window.enemyes == 0: # и если их не осталось, то открываются боссы
                map_window.loc11.setEnabled(True)
            if exp >= level_up: # если опыта достаточно то идёт повышение уровня
                level += 1
                exp -= level_up
                level_up += 25
                win.setText(f"""Вы одолели своего противника и зачистили данную территорию.
Вы забрали его снаряжение и получили {random_exp} очков опыта.
У вас новый уровень!""")
                winning = win.exec_()
                if winning == psw.QMessageBox.Ok:
                    self.close()
                    perks.show() 
            else: # иначе просто оповещают о победе и мы переходим в окно карты
                win.setText(f"""Вы одолели своего противника и зачистили данную территорию.
Вы забрали его снаряжение и получили {random_exp} очков опыта.""")
                winning = win.exec_()
                if winning == psw.QMessageBox.Ok:
                    self.close()
                    map_window.show()
        else: # если противник всё ещё жив (здоровье больше 0)
            self.information1.setText(self.enemy.attack(Player)) # противник атакует игрока и показывается информация
            self.update_info() # обновление информации
            if Player.health_control() == False: # если здоровье игрока 0 и ниже он погибает
                self.information1.setText("")
                self.information2.setText(f"Вы пали в бою")
                # информационное окно о поражении
                lose = psw.QMessageBox(self)
                lose.setWindowTitle("Вы проиграли...")
                lose.setText("""Несмотря на ваши усилия вы пали в бою от рук противника.""")
                losing = lose.exec_()
                if losing == psw.QMessageBox.Ok:
                    self.close()
# Класс окна навыков
class PerksWindow(psw.QWidget):
    def __init__(self):
        super(PerksWindow, self).__init__()
        self.setWindowTitle("Улучшение персонажа") # название окна
        # верхняя надпись
        self.title = psw.QLabel("За повышение уровня вам доступен один из навыков")
        self.title.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование надписи
        # описание навыков
        self.perk1 = psw.QLabel("1) Вы увеличите своё максимальное здоровье на 10 единиц")
        self.perk2 = psw.QLabel("2) Вы увеличите свою защиту от всех факторов на 5 единиц")
        self.perk3 = psw.QLabel("1) Вы увеличите шанс атаки с критическим уроном на 7%")
        # кнопки навыков
        self.btn1 = psw.QPushButton("+ Здоровье")
        self.btn1.clicked.connect(self.perk_1) # подключение функции "perk_1"
        self.btn2 = psw.QPushButton("+ Защита")
        self.btn2.clicked.connect(self.perk_2) # подключение функции "perk_2"
        self.btn3 = psw.QPushButton("+ Крит.урон")
        self.btn3.clicked.connect(self.perk_3) # подключение функции "perk_3"
        # горизонтальный контейнер кнопок
        self.h_layout = psw.QHBoxLayout()
        self.h_layout.addWidget(self.btn1) # добавление первой кнопки
        self.h_layout.addWidget(self.btn2) # добавление второй кнопки
        self.h_layout.addWidget(self.btn3) # добавление третей кнопки
        # вертикальный контейнер
        self.v_layout = psw.QVBoxLayout()
        self.v_layout.addWidget(self.title) # добавление надписи
        self.v_layout.addWidget(self.perk1) # добавление описаний
        self.v_layout.addWidget(self.perk2)
        self.v_layout.addWidget(self.perk3)
        self.v_layout.addLayout(self.h_layout) # добавление блока кнопок
        self.setLayout(self.v_layout) # установить контейнер основным
    def perk_1(self): # функция увеличения здоровья
        Player.max_health += 10
        Player.health += 10
        map_window.show()
        self.close()
    def perk_2(self): # функция увеличения защиты
        Player.physic_protect += 5
        Player.termo_protect += 5
        Player.chemical_protect += 5
        Player.electro_protect += 5
        Player.radiation_protect += 5
        Player.psyonical_protect += 5
        Player.cold_protect += 5
        Player.EMI_protect += 5
        map_window.show()
        self.close()
    def perk_3(self): # функция увеличения шанса на критическую атаку
        Player.krit_chance += 1
        map_window.show()
        self.close()
# Класс окна боссов
class BossesWindow(psw.QWidget):
    def __init__(self):
        super(BossesWindow, self).__init__()
        self.enemy = "-" # выбранный противник
        self.current = "0" # выбранная кнопка
        self.enemyes = 3 # количество боссов
        self.setWindowTitle("Меню выбора противника") # название окна
        # залоговок окна
        self.title = psw.QLabel("Выберете противника. Учтите, у них больше здоровья и шанса крит.атаки")
        self.title.setAlignment(psc.Qt.AlignmentFlag(4)) # центрирование заголовка
        # кнопки противников
        self.enemy1 = psw.QPushButton("Штурмовик")
        self.enemy1.clicked.connect(self.choice1)
        self.enemy2 = psw.QPushButton("Убийца")
        self.enemy2.clicked.connect(self.choice2)
        self.enemy3 = psw.QPushButton("Страж")
        self.enemy3.clicked.connect(self.choice3)
        self.about_enemy = psw.QLabel("Выберете противника")
        # кнопка выбора
        self.btn1 = psw.QPushButton("Сражаться")
        self.btn1.clicked.connect(self.choice)
        self.btn1.setEnabled(False) # изначально заблокирована
        # кнопка выхода
        self.btn2 = psw.QPushButton("Назад")
        self.btn2.clicked.connect(self.exit)
        # горизонтальный контейнер кнопок врагов
        self.enemy_btns = psw.QHBoxLayout()
        self.enemy_btns.addWidget(self.enemy1)
        self.enemy_btns.addWidget(self.enemy2)
        self.enemy_btns.addWidget(self.enemy3)
        # горизонтальный контейнер для кнопок
        self.btns = psw.QHBoxLayout()
        self.btns.addWidget(self.btn1) # добавление кнопки выбора противника
        self.btns.addWidget(self.btn2) # добавление кнопки выхода
        # основной контейнер
        self.mainlayout = psw.QVBoxLayout()
        self.mainlayout.addWidget(self.title) # добавление заголовка
        self.mainlayout.addLayout(self.enemy_btns) # добавление кнопок врагов
        self.mainlayout.addWidget(self.about_enemy) # добавление описания врага
        self.mainlayout.addLayout(self.btns) # добавление нижних кнопок
        self.setLayout(self.mainlayout)
    def exit(self): # функция выхода
        self.close()
        map_window.show()
    def choice1(self): # функция выбора противника
        self.enemy = "Штурмовик"
        self.current = "1"
        self.about_enemy.setText(enemys[self.enemy].about)
        self.btn1.setEnabled(True) # разблокировка кнопки
    def choice2(self):
        self.enemy = "Убийца"
        self.current = "2"
        self.about_enemy.setText(enemys[self.enemy].about)
        self.btn1.setEnabled(True)
    def choice3(self):
        self.enemy = "Страж"
        self.current = "3"
        self.about_enemy.setText(enemys[self.enemy].about)
        self.btn1.setEnabled(True)
    def choice(self):
        global bossfight
        bossfight = BossFightWindow(enemys[self.enemy])
        bossfight.show()
        self.close()
# Класс окна битвы
class BossFightWindow(FightWindow):
    def inventory(self): # функция перехода в инвентарь
        self.close()
        inv.window_before = "bossfight"
        inv.update_inventory()
        inv.show()
    def attack(self): # функция атаки противника
        global exp
        global inventory_weapon
        global inventory_armor
        global heals
        global level
        global level_up
        self.information2.setText(Player.attack(self.enemy)) # игрок атакует противника
        self.update_info() # обновление информации
        if self.enemy.health_control() == False: # если противник повержен (здоровье 0 и меньше)
            self.information1.setText("")
            self.information2.setText(f"{self.enemy.name} пал перед вами!")
            # информационное окно о победе
            win = psw.QMessageBox(self)
            win.setWindowTitle("Вы победили босса!")
            # случайное кол-во опыта, рассчитывающееся как (сумма атаки оружия + средняя защита брони) +- 20%
            random_exp = int((self.enemy.weapon.physic_attack + self.enemy.weapon.termo_attack + self.enemy.weapon.chemical_attack + self.enemy.weapon.electro_attack + self.enemy.weapon.radiation_attack + self.enemy.weapon.psyonical_attack + self.enemy.weapon.cold_attack + self.enemy.weapon.EMI_attack + (self.enemy.armor.physic_protect + self.enemy.armor.termo_protect + self.enemy.armor.chemical_protect + self.enemy.armor.electro_protect + self.enemy.armor.radiation_protect + self.enemy.armor.psyonical_protect + self.enemy.armor.cold_protect + self.enemy.armor.EMI_protect) / 8) * (1 + 0.01 * random.randint(-20, 20)) * 1.5)
            exp += random_exp # прибавление опыта
            # случайное число медикаментов
            random_heals = random.randint(1, 3)
            inventory_weapon.update({self.enemy.weapon.name: self.enemy.weapon}) # добавление оружия в инвентарь
            inventory_armor.update({self.enemy.armor.name: self.enemy.armor}) # добавление брони в инвентарь
            heals += random_heals # добавление аптечек
            exec(f"""bosses.enemy{bosses.current}.setEnabled(False)""") # блокировка кнопки выбора противника
            bosses.about_enemy.setText("Невероятно! Вы смогли победить босса! Давайте следующего!") # изменение описания внизу окна карта
            bosses.enemyes -= 1 # кол-во врагов уменьшается
            if bosses.enemyes == 0: # и если их не осталось, то показывается окно победы
                win.setText(f"""Вы одолели последнюю легенду этой Пустоши.
И отныне вы становитесь {Player.name} Неодолимый!
Поздравляем с победой!""")
                winning = win.exec_()
                if winning == psw.QMessageBox.Ok:
                    self.close()
            else: # иначе оповещают о победе и мы переходим в окно боссов
                if exp >= level_up: # если опыта достаточно то идёт повышение уровня
                    level += 1
                    exp -= level_up
                    level_up += 25
                    win.setText(f"""{self.enemy.name} был повержен вами в этой битве!
Вы забрали его снаряжение и получили {random_exp} очков опыта.
У вас новый уровень!""")
                    winning = win.exec_()
                    if winning == psw.QMessageBox.Ok:
                        self.close()
                        perks.show() 
                else:
                    win.setText(f"""{self.enemy.name} был повержен вами в этой битве!
Вы забрали его снаряжение и получили {random_exp} очков опыта.""")
                    winning = win.exec_()
                    if winning == psw.QMessageBox.Ok:
                        self.close()
                        bosses.show()
        else: # если противник всё ещё жив (здоровье больше 0)
            self.information1.setText(self.enemy.attack(Player)) # противник атакует игрока и показывается информация
            self.update_info() # обновление информации
            if Player.health_control() == False: # если здоровье игрока 0 и ниже он погибает
                self.information1.setText("")
                self.information2.setText(f"Вы пали в бою")
                # информационное окно о поражении
                lose = psw.QMessageBox(self)
                lose.setWindowTitle("Вы проиграли...")
                lose.setText(f"""Что ж. {self.enemy.name} оказался сильнее, чем вы думали.
Ваше мёртвое тело стало ещё одним свидетельством его силы.""")
                losing = lose.exec_()
                if losing == psw.QMessageBox.Ok:
                    self.close()

# экземпляры окон
app = psw.QApplication() # приложение
menu = MenuWindow() # окно начального меню
create_player = CreatePlayer() # окно создания персонажа
map_window = MapWindow() # окно карта
inv = InvWindow() # окно инвентаря
fight = FightWindow(stoormtroper) # окно боя (штурмовик для заглушки)
perks = PerksWindow() # окно навыков
bosses = BossesWindow() # окно боссов
bossfight = BossFightWindow(stoormtroper) # окно битвы с боссами
menu.show()
app.exec_()