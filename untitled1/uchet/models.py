from django.db import models

# Create your models here.
# Отделы

class Department(models.Model):
    dep_name = models.CharField('Название отдела', max_length=50, primary_key=True)

    def __str__(self):
        return self.dep_name

# Подотделы

class SubDepartment(models.Model):
    dep_name = models.ForeignKey(Department, to_field="dep_name", db_column="dep_name", on_delete=models.CASCADE)
    subdep_name = models.CharField('Название подотдела', max_length=50, primary_key=True)

    def __str__(self):
        return self.subdep_name

# Сотрудники

class Employe(models.Model):
    dep_name = models.ForeignKey(Department, to_field="dep_name", db_column="dep_name", on_delete=models.CASCADE)
    subdep_name = models.ForeignKey(SubDepartment, to_field="subdep_name", db_column="subdep_name", on_delete=models.CASCADE, null=True)
    emp_position = models.CharField('Должность сотрудника', max_length=50, default="Без должности")
    emp_salary = models.IntegerField('Зарплата сотрудника', default=0)
    emp_name = models.CharField('Имя сотрудника', max_length=50)
    emp_surname = models.CharField('Фамилия сотрудника', max_length=50)
    emp_birthdate = models.DateField('Дата рождения сотрудника')
    employment_date = models.DateField('Дата устройства на работу')

    def __str__(self):
        return self.emp_name + " " + self.emp_surname
