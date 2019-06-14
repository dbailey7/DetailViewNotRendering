from django.db import models;
from django.core.urlresolvers import reverse;

# Create your models here ..
class mp_archetype(models.Model):
    id = models.CharField(primary_key=True, max_length=64, unique=True, blank=False);
    gid = models.UUIDField();
    crtdate = models.DateField();
    crtby = models.CharField(max_length=128);

    def __str__(self):
        return self.crtby + '-' + str(self.crtdate) + '-' + self.id;

    def get_absolute_url(self):
        return reverse("cmpbltrapp:mp_archetype-detail",kwargs={'pk':self.pk})


class mp_element(models.Model):
    fldname = models.CharField(max_length=64);
    fldtype = models.CharField(max_length=64);
    gid = models.UUIDField();
    archetypeid = models.UUIDField();
    crtdate = models.DateField();
    crtby = models.CharField(max_length=128);

    def __str__(self):
        return self.fldname;

    def get_absolute_url(self):
        return reverse("cmpbltrapp:edetail",kwargs={'pk':self.pk})

# class mp_error(models.Model):
#     errorcode = models.CharField(max_length=256);
#     meaning = models.CharField(max_length=256);
#
#     def __str__(self):
#         return self.errorcode;
#
# class mp_instance(models.Model):
#     id = models.CharField(primary_key=True, max_length=64, unique=True, blank=False);
#     gid = models.UUIDField();
#     crtdate = models.DateField();
#     crtby = models.CharField(max_length=128);
#     archetypeid = models.UUIDField();
#     parentinstgid = models.UUIDField();
#     childinstgid = models.UUIDField();
#
#     def __str__(self):
#         return  self.archetypeid + '-' + self.crtby + '-' + self.crtdate;
#
# class mp_joblogs(models.Model):
#     jobseq = models.PositiveIntegerField(unique=True, null=True, blank=False);
#     logtime = models.DateTimeField();
#     logmessage = models.CharField(max_length=256);
#     joblogseq = models.PositiveIntegerField(unique=True, null=True, blank=False);
#
#     def __str__(self):
#         return self.jobseq + '-' + self.logmessage;
#
# class mp_jobs(models.Model):
#     jobseq = models.PositiveIntegerField(unique=True, null=True, blank=False);
#     name = models.CharField(max_length=256, blank=False);
#     started = models.DateTimeField();
#     ended = models.DateTimeField();
#     status = models.CharField(max_length=256);
#
#     def __str__(self):
#         return self.name + '-' + self.jobseq;
#
# class mp_numerictypes(models.Model):
#     id = models.CharField(primary_key=True, max_length=64, unique=True, blank=False);
#     ntint = models.PositiveIntegerField();
#
#     def __str__(self):
#         return self.columnname;
#
# class mp_relation(models.Model):
#     instanceid = models.CharField(max_length=64, unique=True, null=True, blank=False);
#     instancegid = models.UUIDField();
#     gid_fieldname = models.CharField(max_length=64, unique=True, null=True, blank=False);
#     linkinstanceid = models.CharField(max_length=64, unique=True, null=True, blank=False);
#     linkinstancegid = models.UUIDField();
#     crtdate = models.DateField();
#     crtby = models.UUIDField();
#
#     def __str__(self):
#         return self.gid_fieldname + '-' + self.linkinstanceid;
#
# class mp_result(models.Model):
#     classname = models.CharField(max_length=64, unique=True, null=True, blank=False);
#     numnumeric = models.PositiveIntegerField();
#     numtext = models.PositiveIntegerField();
#     numdate = models.PositiveIntegerField();
#     numboolean = models.PositiveIntegerField();
#
#     def __str__(self):
#         return self.classname;
#
# class mp_role(models.Model):
#     id = models.CharField(primary_key=True, max_length=64, unique=True, blank=False);
#     gid = models.UUIDField();
#     empowerments = models.CharField(max_length=512);
#
#     def __str__(self):
#         return self.id + '-' + self.empowerments;
#
# class mp_set(models.Model):
#     id = models.CharField(primary_key=True, max_length=64, unique=True, blank=False);
#     gid = models.UUIDField();
#     description = models.CharField(max_length=512);
#
#     def __str__(self):
#         return self.id + '-' + self.description;
#
# class mp_user(models.Model):
#     id = models.CharField(primary_key=True, max_length=64, unique=True, blank=False);
#     gid = models.UUIDField();
#     roleid = models.UUIDField();
#     baggage = models.CharField(max_length=512);
#
#     def __str__(self):
#         return self.id + '-' + self.baggage;
#
# class mpi_activity(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     description = models.CharField(max_length=256);
#
#     def __str__(self):
#         return self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + self.description;
#
# class mpi_agent(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     bitcoinWalletId = models.CharField(max_length=256);
#     codename = models.CharField(max_length=256);
#     firstengagementdate = models.DateTimeField();
#     coefficient = models.DecimalField(max_digits=19, decimal_places=10);
#     nt_coefficient = models.PositiveIntegerField();
#
#     def __str__(self):
#         return self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + self.codename;
#
# class mpi_assignment(models.Model):
#     id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False);
#     setGid = models.UUIDField();
#     parent_gid = models.UUIDField();
#     child_gid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     sharePercent = models.DecimalField(max_digits=19, decimal_places=10);
#     nt_sharePercent = models.PositiveIntegerField();
#
#     def __str__(self):
#         return self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + self.sharePercent;
#
# class mpi_order(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effDate = models.DateTimeField(null=True, blank=False);
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     newCustomerFlag = models.BooleanField();
#
#     def __str__(self):
#         return self.id  + '-' + self.effDate + '-' + self.newCustomerFlag;
#
# class mpi_outcome(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effDate = models.DateTimeField(null=True, blank=False);
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     description = models.CharField(max_length=256);
#     resultCode = models.CharField(max_length=256);
#     resultValue =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_resultValue = models.PositiveIntegerField();
#
#     def __str__(self):
#         return self.id  + '-' + self.effDate + '-' + self.description;
#
# class mpi_product(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     description = models.CharField(max_length=256);
#     family = models.CharField(max_length=256);
#     cost = models.DecimalField(max_digits=19, decimal_places=10);
#     nt_cost = models.PositiveIntegerField();
#
#     def __str__(self):
#         return self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + self.description;
#
# class mpi_result_none_agent(models.Model):
#     id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False);
#     setGid = models.UUIDField();
#     time_Gid = models.UUIDField();
#     rule_Gid = models.UUIDField();
#     inner_Gid = models.UUIDField();
#     outer_Gid = models.UUIDField();
#     name = models.CharField(max_length=256);
#     type = models.CharField(max_length=256);
#     isImmutable = models.BooleanField();
#     numeric0 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric0 = models.PositiveIntegerField();
#     numeric1 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric1 = models.PositiveIntegerField();
#     numeric2 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric2 = models.PositiveIntegerField();
#     numeric3 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric3 = models.PositiveIntegerField();
#     string0 = models.CharField(max_length=256);
#     string1 = models.CharField(max_length=256);
#     string2 = models.CharField(max_length=256);
#     string3 = models.CharField(max_length=256);
#     date0 = models.DateTimeField();
#     date1 = models.DateTimeField();
#     date2 = models.DateTimeField();
#     date3 = models.DateTimeField();
#     boolean0 = models.BooleanField();
#     boolean1 = models.BooleanField();
#     boolean2 = models.BooleanField();
#     boolean3 = models.BooleanField();
#
#     def __str__(self):
#         return self.name + '-' + self.type;
#
# class mpi_result_sale_agent(models.Model):
#     id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False);
#     setGid = models.UUIDField();
#     time_Gid = models.UUIDField();
#     rule_Gid = models.UUIDField();
#     inner_Gid = models.UUIDField();
#     outer_Gid = models.UUIDField();
#     name = models.CharField(max_length=256);
#     type = models.CharField(max_length=256);
#     isImmutable = models.BooleanField();
#     numeric0 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric0 = models.PositiveIntegerField();
#     numeric1 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric1 = models.PositiveIntegerField();
#     numeric2 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric2 = models.PositiveIntegerField();
#     numeric3 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric3 = models.PositiveIntegerField();
#     string0 = models.CharField(max_length=256);
#     string1 = models.CharField(max_length=256);
#     string2 = models.CharField(max_length=256);
#     string3 = models.CharField(max_length=256);
#     date0 = models.DateTimeField();
#     date1 = models.DateTimeField();
#     date2 = models.DateTimeField();
#     date3 = models.DateTimeField();
#     boolean0 = models.BooleanField();
#     boolean1 = models.BooleanField();
#     boolean2 = models.BooleanField();
#     boolean3 = models.BooleanField();
#
#     def __str__(self):
#         return self.name + '-' + self.type;
#
# class mpi_result_sale_order(models.Model):
#     id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False);
#     setGid = models.UUIDField();
#     time_Gid = models.UUIDField();
#     rule_Gid = models.UUIDField();
#     inner_Gid = models.UUIDField();
#     outer_Gid = models.UUIDField();
#     name = models.CharField(max_length=256);
#     type = models.CharField(max_length=256);
#     isImmutable = models.BooleanField();
#     numeric0 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric0 = models.PositiveIntegerField();
#     numeric1 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric1 = models.PositiveIntegerField();
#     numeric2 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric2 = models.PositiveIntegerField();
#     numeric3 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric3 = models.PositiveIntegerField();
#     string0 = models.CharField(max_length=256);
#     string1 = models.CharField(max_length=256);
#     string2 = models.CharField(max_length=256);
#     string3 = models.CharField(max_length=256);
#     date0 = models.DateTimeField();
#     date1 = models.DateTimeField();
#     date2 = models.DateTimeField();
#     date3 = models.DateTimeField();
#     boolean0 = models.BooleanField();
#     boolean1 = models.BooleanField();
#     boolean2 = models.BooleanField();
#     boolean3 = models.BooleanField();
#
#     def __str__(self):
#         return self.name + '-' + self.type;
#
# class mpi_result_sale_role(models.Model):
#     id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False);
#     setGid = models.UUIDField();
#     time_Gid = models.UUIDField();
#     rule_Gid = models.UUIDField();
#     inner_Gid = models.UUIDField();
#     outer_Gid = models.UUIDField();
#     name = models.CharField(max_length=256);
#     type = models.CharField(max_length=256);
#     isImmutable = models.BooleanField();
#     numeric0 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric0 = models.PositiveIntegerField();
#     numeric1 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric1 = models.PositiveIntegerField();
#     numeric2 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric2 = models.PositiveIntegerField();
#     numeric3 =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_numeric3 = models.PositiveIntegerField();
#     string0 = models.CharField(max_length=256);
#     string1 = models.CharField(max_length=256);
#     string2 = models.CharField(max_length=256);
#     string3 = models.CharField(max_length=256);
#     date0 = models.DateTimeField();
#     date1 = models.DateTimeField();
#     date2 = models.DateTimeField();
#     date3 = models.DateTimeField();
#     boolean0 = models.BooleanField();
#     boolean1 = models.BooleanField();
#     boolean2 = models.BooleanField();
#     boolean3 = models.BooleanField();
#
#     def __str__(self):
#         return self.name + '-' + self.type;
#
# class mpi_role(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     roleclass_Gid = models.UUIDField();
#     Agent_Gid = models.UUIDField();
#     multiplier =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_multiplier = models.PositiveIntegerField();
#     tbd1 = models.CharField(max_length=256);
#     tbd2 = models.CharField(max_length=256);
#
#     def __str__(self):
#         self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + self.roleclass_gid + '-' + self.Agent_gid;
#
# class mpi_roleclass(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     description = models.CharField(max_length=256);
#     tbd1 = models.CharField(max_length=256);
#     tbd2 = models.CharField(max_length=256);
#
#     def __str__(self):
#         self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + \
#         self.roleclass_gid + '-' + self.parent_gid + '-' + self.description;
#
# class mpi_sale(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     order_gid = models.UUIDField();
#     LineItem = models.CharField(max_length=256);
#     activityType_gid = models.UUIDField();
#     ledgerDate = models.DateTimeField(null=True);
#     territory_gid = models.UUIDField();
#     product_gid = models.UUIDField();
#     unitPrice =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_unitPrice = models.PositiveIntegerField();
#     quantity =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_quantity = models.PositiveIntegerField();
#     totalPrice =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_totalPrice = models.PositiveIntegerField();
#
#     def __str__(self):
#         self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + \
#         self.order_gid + '-' + self.LineItem;
#
# class mpi_sys_flow(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     rulename = models.CharField(max_length=256);
#     sequenceInFlow = models.PositiveIntegerField();
#     parameterValueList = models.PositiveIntegerField();
#     outerSetName = models.PositiveIntegerField();
#     outerSetFilter = models.PositiveIntegerField();
#     innerSetName = models.PositiveIntegerField();
#     innerSetFilter = models.PositiveIntegerField();
#     timeid = models.CharField(max_length=256);
#     isImmutable = models.BooleanField();
#     resultSetName = models.CharField(max_length=256);
#
#     def __str__(self):
#         self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + \
#         self.rulename + '-' + self.sequenceInFlow + '-' + \
#         self.resultSetName;
#
# class mpi_sys_rule(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     parameterList = models.CharField(max_length=256);
#     outerSetClass = models.CharField(max_length=256);
#     outerSetFilter = models.CharField(max_length=256);
#     innerSetClass = models.CharField(max_length=256);
#     innerSetFilter = models.CharField(max_length=256);
#     behavior = models.CharField(max_length=256);
#     customBehavior = models.CharField(max_length=256);
#     logicalElementList = models.CharField(max_length=256);
#     ruleOutputList = models.CharField(max_length=256);
#     resultName = models.CharField(max_length=256);
#     resultType = models.CharField(max_length=256);
#
#     def __str__(self):
#         self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + \
#         self.resultname + '-' + self.resultType;
#
# class mpi_sys_time(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     periodStart = models.DateTimeField(null=True, blank=False);
#     periodStart = models.DateTimeField(null=True, blank=False);
#     type = models.CharField(max_length=256);
#     group = models.CharField(max_length=256);
#
#     def __str__(self):
#         self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + \
#         self.periodStart + '-' + self.periodEnd + '-' + \
#         self.type + '-' + self.group;
#
# class mpi_territory(models.Model):
#     id = models.CharField(primary_key=True, max_length=128, unique=True, blank=False);
#     gid = models.UUIDField();
#     setGid = models.UUIDField();
#     effStart = models.DateTimeField(null=True, blank=False);
#     effEnd = models.DateTimeField(null=True, blank=False);
#     parent_gid = models.UUIDField();
#     isDeleted = models.BooleanField();
#     deleteDate = models.DateTimeField(null=True);
#     altName = models.CharField(max_length=256);
#     population = models.CharField(max_length=256);
#     population = models.PositiveIntegerField();
#     squareMiles =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_squareMiles = models.PositiveIntegerField();
#     costBasis =  models.DecimalField(max_digits=19, decimal_places=10);
#     nt_costBasis = models.PositiveIntegerField();
#
#     def __str__(self):
#         self.id  + '-' + self.effStart + '-' + self.effEnd + '-' + \
#         self.periodStart + '-' + self.periodEnd + '-' + self.altName;
