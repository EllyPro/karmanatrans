from django.db import models


    
     
class List(models.Model):
    ORGANIZATION_CHOICES = (
        ("Нур Транс", "Нур Транс"),
        ('Кармана Транс', 'Кармана Транс'),
    )
    id = models.AutoField(primary_key=True)
    full_name = models.CharField('Ф.И.O', max_length=255)
    organization = models.CharField(verbose_name='Уюшма номи', max_length=255,
                  choices=ORGANIZATION_CHOICES,)
    car_brend = models.CharField('Aвтомашина русуми', max_length=255)
    car_number = models.CharField('Давлат белгиси', max_length=8, unique=True)
    date_given = models.DateField('Лицензия олган сана')
    deadline = models.DateField('Лицензия муддати')
    number_license = models.CharField('Лицензия рақами', max_length=15)
    phone_number = models.CharField('Телефон', max_length=9)
    

    
    class Meta:
        
        verbose_name = 'Cписка'
        verbose_name_plural = 'Cписка'
    
    def __str__(self):
        return self.car_number
    
class Putyovka(models.Model):
    car_number = models.ForeignKey(List, on_delete=models.DO_NOTHING, verbose_name="Hомер автомобиля")
    date = models.DateField("Дата")
    money = models.IntegerField("Сумма")
        
    class Meta:
        ordering = ('-date',)
        verbose_name = 'Путёвки'
        verbose_name_plural = 'Путёвки'
    
    def __str__(self):
        return str(self.money)