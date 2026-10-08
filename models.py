# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DataSource(models.Model):
    data_source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=200)
    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=20)
    source_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'data_source'
        unique_together = (('source_name', 'file_name', 'source_date'),)


class ExcludedParty(models.Model):
    party_id = models.AutoField(primary_key=True)
    party_type = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    business_name = models.CharField(max_length=100)
    provider_category = models.CharField(max_length=150)
    specialty = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=3)
    zip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'excluded_party'


class ExclusionRecord(models.Model):
    exclusion_record_id = models.AutoField(primary_key=True)
    party = models.ForeignKey(ExcludedParty, models.DO_NOTHING)
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING)
    import_log = models.ForeignKey('ImportLog', models.DO_NOTHING)
    exclusion_type = models.CharField(max_length=50)
    exclusion_date = models.DateField()
    reinstatement_date = models.DateField()
    waiver_date = models.DateField()
    waiver_state = models.CharField(max_length=10)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'exclusion_record'


class Identifier(models.Model):
    identifier_id = models.AutoField(primary_key=True)
    party = models.ForeignKey(ExcludedParty, models.DO_NOTHING)
    identifier_type = models.CharField(max_length=10)
    identifier_value = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'identifier'


class ImportLog(models.Model):
    import_log_id = models.AutoField(primary_key=True)
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING)
    imported_at = models.DateTimeField()
    status = models.CharField(max_length=20)
    records_loaded = models.IntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'import_log'
