from django.db import models

POSITION = (
    (1, "Instalator"),
    (2, "Elektryk"),
    (3, "Pracownik biurowy"),
    (4, "Handlowiec")
)

TYPES_OF_INVESTMENT = (
    (1, "Panele fotowoltaiczne"),
    (2, "Pompa ciepła"),
    (3, "Kolektory słoneczne"),
    (4, "Kocioł")
)


class Squad(models.Model):
    name = models.CharField(max_length=64, default="BRAK")

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.IntegerField(choices=POSITION)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Investment(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    street_name = models.CharField(max_length=128)
    city_name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10)
    type_of_investment = models.IntegerField(choices=TYPES_OF_INVESTMENT)
    workers = models.ManyToManyField(Squad, through='SquadInvestment')

    @property
    def name(self):
        return "{}, {}".format(self.street_name, self.city_name)

    def __str__(self):
        return self.name


class SquadInvestment(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    @property
    def squad_and_investment(self):
        return "{} - {}".format(self.investment, self.squad)

    def __str__(self):
        return self.squad_and_investment


class DayName(models.Model):
    name = models.TextField(null=False, unique=True)

    def __str__(self):
        return self.name


class EachDate(models.Model):
    day_name = models.IntegerField()
    month_name = models.IntegerField()
    year_name = models.IntegerField()
    investment = models.ManyToManyField(Investment, through='InvestmentEachDate')

    @property
    def name(self):
        return "{}.{}.{}".format(self.day_name, self.month_name, self.year_name)

    def __str__(self):
        return self.name


class InvestmentEachDate(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    date = models.ForeignKey(EachDate, on_delete=models.CASCADE)


