from django.db import models


class AutomatedSystem(models.Model):
    name = models.CharField('Автоматизированная Система', max_length=100)
    def __str__(self):
        return self.name

class Interaction(models.Model):
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