from djongo import models

class Machine(models.Model):
    name = models.CharField(max_length=5)
    product_type = models.CharField(max_length=64,choices=[
        ('large_machine','Coffee Machine Large'),
        ('small_machine','Coffee Machine Small'),
        ('espresso','Espresso Machine'),
    ])

    water_line_compitable = models.BooleanField(blank=True)
    model = models.CharField(max_length=64,choices = [
        ('base_model','base model'),
        ('preimum_model','preimum model'),
        ('deluxe_model','deluxe model'),
    ])

    def __str__(self):
        return self.name


class Pod(models.Model):
    name = models.CharField(max_length=5)
    product_type = models.CharField(max_length=64,choices=[
        ('large_pod','Coffee Pod Large'),
        ('small_pod','Coffee Pod Small'),
        ('espresso','Espresso Pod'),
    ])
    flavor = models.CharField(max_length=64,choices=[
        ('vanilla','Vanilla'),
        ('caramel','Caramel'),
        ('psl','PSL'),
        ('mocha','Mocha'),
        ('hazelnut','Hazelnut'),
    ])

    pack_size = models.CharField(max_length=64,choices=[
        ('1_dozen','1 dozen (12)'),
        ('3_dozen','3 dozen (36)'),
        ('5_dozen','5 dozen (60)'),
        ('7_dozen','7 dozen (84)'),
        ])

    def __str__(self):
        return self.name
    