from django.db import models

class ArchitectureRealm(models.Model):
    name = models.CharField('Область Определения Архитектуры', max_length=50)

class ArchitectureCategory(models.Model):
    realm = models.ForeignKey(ArchitectureRealm, on_delete=models.CASCADE)
    name = models.CharField('Категория АС', max_length=50)

class ArchitectureSubCategory(models.Model):
    category = models.ForeignKey(ArchitectureCategory, on_delete=models.CASCADE)
    name = models.CharField('Подкатегория АС', max_length=50)

class AutomatedSystem(models.Model):

    subcategory = models.ForeignKey(ArchitectureSubCategory, on_delete=models.CASCADE)

    code = models.CharField('Код АС', max_length=50)
    name = models.CharField('Автоматизированная Система', max_length=100)
    owner = models.CharField('Владелец', max_length=50, blank=True)
    status = models.CharField('Статус', max_length=50, blank=True)
    cloud_ready = models.CharField('Cloud Ready/Native	', max_length=50, blank=True)
    platform_ready = models.CharField('Platform Ready', max_length=50, blank=True)
    owner_block = models.CharField('Владелец - Блок', max_length=50, blank=True)
    owner_tribe = models.CharField('Владелец - Трайб', max_length=50, blank=True)
    full_name = models.CharField('Полное имя АС', max_length=50, blank=True)
    nickname = models.CharField('Псевдоним АС', max_length=50, blank=True)
    short_description = models.CharField('Краткое описание', max_length=50, blank=True)
    rsa_id = models.CharField('ID в RSA', max_length=50, blank=True)
    service_desk_id = models.CharField('ID в Service Desk', max_length=50, blank=True)
    guid = models.CharField('GUID', max_length=50, blank=True)
    centralization_level = models.CharField('Уровень централизации', max_length=50, blank=True)
    system_criticality = models.CharField('Критичность системы', max_length=50, blank=True)
    target_status = models.CharField('Целевой статус', max_length=50, blank=True)
    target_readiness = models.CharField('Готовность целевого решения', max_length=50, blank=True)
    as_lider = models.CharField('Лидер АС', max_length=50, blank=True)
    as_architect = models.CharField('Архитектор АС', max_length=50, blank=True)
    architect_in_charge = models.CharField('Курирующий архитектор', max_length=50, blank=True)
    editors = models.CharField('Редакторы', max_length=50, blank=True)

    target_architecture_diagram = models.ImageField('Диаграмма целевой архитектуры', upload_to='target_architecture_diagrams', blank=True)    

    def __str__(self):
        return self.name


class Interaction(models.Model):

    automated_system = models.ForeignKey(AutomatedSystem, on_delete=models.CASCADE)

    code = models.CharField('Код', max_length=50)
    int_type = models.CharField('Тип', max_length=50, blank=True)
    protocol = models.CharField('Протокол', max_length=50, blank=True)
    as_provider = models.CharField('АС Поставщик',max_length=50, blank=True)
    fp_provider = models.CharField('ФП Поставщик',max_length=50, blank=True)
    description = models.CharField('Описание',max_length=500, blank=True)
    status = models.CharField('Статус',max_length=50, blank=True)
    iniciator = models.CharField('Инициатор',max_length=50, blank=True)
    int_technology = models.CharField('Технология взаимодействия',max_length=50, blank=True)

    consumer_status = models.CharField('Потребитель - Статус',max_length=50, blank=True)
    consumer_date = models.CharField('Потребитель - Срок',max_length=50, blank=True)
    consumer_as = models.CharField('Потребитель - АС',max_length=50, blank=True)
    consumer_role = models.CharField('Потребитель - Роль',max_length=50, blank=True)
    consumer_process = models.CharField('Потребитель - Процесс',max_length=50, blank=True)
    consumer_sla = models.CharField('Потребитель - SLA',max_length=50, blank=True)
    consumer_comment = models.CharField('Потребитель - Комментарий',max_length=50, blank=True)

    data_description = models.CharField('Передаваемые данные - Описание',max_length=500, blank=True)
    data_encoding = models.CharField('Передаваемые данные - Кодировка',max_length=50, blank=True)
    data_format = models.CharField('Передаваемые данные - Формат',max_length=50, blank=True)
    data_confidential_level = models.CharField('Передаваемые данные - Категория конфиденциальности',max_length=50, blank=True)
    data_integrity_level = models.CharField('Передаваемые данные - Категория целостности',max_length=50, blank=True)

    schedule_initiation = models.CharField('Регламент выгрузки - Инициация',max_length=50, blank=True)
    schedule_year = models.CharField('Регламент выгрузки - Год',max_length=50, blank=True)
    schedule_month = models.CharField('Регламент выгрузки - Месяц',max_length=50, blank=True)
    schedule_week = models.CharField('Регламент выгрузки - Неделя',max_length=50, blank=True)
    schedule_day = models.CharField('Регламент выгрузки - День',max_length=50, blank=True)
    schedule_load_profile = models.CharField('Регламент выгрузки - Характер нагрузки',max_length=50, blank=True)

    filesize_min = models.CharField('Размер файла - Мин',max_length=50, blank=True)
    filesize_max = models.CharField('Размер файла - Макс',max_length=50, blank=True)
    filesize_avg = models.CharField('Размер файла - Средний',max_length=50, blank=True)

    security_ssl_tls = models.CharField('Информационная безопасность - SSL/TLS',max_length=50, blank=True)
    security_encription = models.CharField('Информационная безопасность - Шифрование',max_length=50, blank=True)
    security_digital_signature = models.CharField('Информационная безопасность - ЭП',max_length=50, blank=True)

    architecture_standard_complience = models.CharField('Соответствие стандартам архитектуры',max_length=100, blank=True)
    int_comment = models.CharField('Комментарий',max_length=500, blank=True)

    def __str__(self):
        return self.code