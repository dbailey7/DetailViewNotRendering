from django import forms;
from django.core import validators;
from cmpbltrapp.models import mp_archetype, mp_element;

class mp_archetype_model_form(forms.ModelForm):
    class Meta:
        model = mp_archetype;
        fields = '__all__';
    def clean(self):
        all_clean_data = super().clean();
        # Now any of the form's fields can be checkedk, such as ...
        # Custom validation to check that mp_archetype is created by auth user
        creator = all_clean_data['crtby'].lower();
        if creator.lower().find('david') == -1:
            raise forms.ValidationError("Archetype must be created by authorized user");

class mp_element_model_form(forms.ModelForm):
    class Meta:
        model = mp_element;
        fields = '__all__';

# class mp_element_model_form(forms.ModelForm):
#     fldname = forms.CharField();
#     fldtype = forms.CharField();
#     gid = forms.UUIDField();
#     archetypeid = forms.UUIDField();
#     crtdate = forms.DateField();
#     crtby = forms.CharField() ;
#
# class mp_error_model_form(forms.ModelForm):
#     errorcode = forms.CharField() ;
#     meaning = forms.CharField() ;
#
# class mp_instance_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     crtdate = forms.DateField();
#     crtby = forms.CharField() ;
#     archetypeid = forms.UUIDField();
#     parentinstgid = forms.UUIDField();
#     childinstgid = forms.UUIDField();
#
# class mp_joblogs_model_form(forms.ModelForm):
#     jobseq = forms. IntegerField() ;
#     logtime = forms.DateTimeField();
#     logmessage = forms.CharField() ;
#     joblogseq = forms. IntegerField() ;
#
# class mp_jobs_model_form(forms.ModelForm):
#     jobseq = forms. IntegerField() ;
#     name = forms.CharField() ;
#     started = forms.DateTimeField();
#     ended = forms.DateTimeField();
#     status = forms.CharField() ;
#
# class mp_numerictypes_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     ntint = forms. IntegerField();
#
# class mp_relation_model_form(forms.ModelForm):
#     instanceid = forms.CharField() ;
#     instancegid = forms.UUIDField();
#     gid_fieldname = forms.CharField() ;
#     linkinstanceid = forms.CharField() ;
#     linkinstancegid = forms.UUIDField();
#     crtdate = forms.DateField();
#     crtby = forms.UUIDField();
#
# class mp_result_model_form(forms.ModelForm):
#     classname = forms.CharField() ;
#     numnumeric = forms. IntegerField();
#     numtext = forms. IntegerField();
#     numdate = forms. IntegerField();
#     numboolean = forms. IntegerField();
#
# class mp_role_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     empowerments = forms.CharField() ;
#
# class mp_set_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     description = forms.CharField() ;
#
# class mp_user_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     roleid = forms.UUIDField();
#     baggage = forms.CharField() ;
#
# class mpi_activity_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     description = forms.CharField() ;
#
# class mpi_agent_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     bitcoinWalletId = forms.CharField() ;
#     codename = forms.CharField() ;
#     firstengagementdate = forms.DateTimeField();
#     coefficient = forms.DecimalField() ;
#     nt_coefficient = forms. IntegerField();
#
# class mpi_assignment_model_form(forms.ModelForm):
#     id = forms. IntegerField() ;
#     setGid = forms.UUIDField();
#     parent_gid = forms.UUIDField();
#     child_gid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     sharePercent = forms.DecimalField() ;
#     nt_sharePercent = forms. IntegerField();
#
# class mpi_order_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effDate = forms.DateTimeField() ;
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     newCustomerFlag = forms.BooleanField();
#
# class mpi_outcome_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effDate = forms.DateTimeField() ;
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     description = forms.CharField() ;
#     resultCode = forms.CharField() ;
#     resultValue =  forms.DecimalField() ;
#     nt_resultValue = forms. IntegerField();
#
# class mpi_product_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     description = forms.CharField() ;
#     family = forms.CharField() ;
#     cost = forms.DecimalField() ;
#     nt_cost = forms. IntegerField();
#
# class mpi_result_none_agent_model_form(forms.ModelForm):
#     id = forms. IntegerField() ;
#     setGid = forms.UUIDField();
#     time_Gid = forms.UUIDField();
#     rule_Gid = forms.UUIDField();
#     inner_Gid = forms.UUIDField();
#     outer_Gid = forms.UUIDField();
#     name = forms.CharField() ;
#     type = forms.CharField() ;
#     isImmutable = forms.BooleanField();
#     numeric0 =  forms.DecimalField() ;
#     nt_numeric0 = forms. IntegerField();
#     numeric1 =  forms.DecimalField() ;
#     nt_numeric1 = forms. IntegerField();
#     numeric2 =  forms.DecimalField() ;
#     nt_numeric2 = forms. IntegerField();
#     numeric3 =  forms.DecimalField() ;
#     nt_numeric3 = forms. IntegerField();
#     string0 = forms.CharField() ;
#     string1 = forms.CharField() ;
#     string2 = forms.CharField() ;
#     string3 = forms.CharField() ;
#     date0 = forms.DateTimeField();
#     date1 = forms.DateTimeField();
#     date2 = forms.DateTimeField();
#     date3 = forms.DateTimeField();
#     boolean0 = forms.BooleanField();
#     boolean1 = forms.BooleanField();
#     boolean2 = forms.BooleanField();
#     boolean3 = forms.BooleanField();
#
# class mpi_result_sale_agent_model_form(forms.ModelForm):
#     id = forms. IntegerField() ;
#     setGid = forms.UUIDField();
#     time_Gid = forms.UUIDField();
#     rule_Gid = forms.UUIDField();
#     inner_Gid = forms.UUIDField();
#     outer_Gid = forms.UUIDField();
#     name = forms.CharField() ;
#     type = forms.CharField() ;
#     isImmutable = forms.BooleanField();
#     numeric0 =  forms.DecimalField() ;
#     nt_numeric0 = forms. IntegerField();
#     numeric1 =  forms.DecimalField() ;
#     nt_numeric1 = forms. IntegerField();
#     numeric2 =  forms.DecimalField() ;
#     nt_numeric2 = forms. IntegerField();
#     numeric3 =  forms.DecimalField() ;
#     nt_numeric3 = forms. IntegerField();
#     string0 = forms.CharField() ;
#     string1 = forms.CharField() ;
#     string2 = forms.CharField() ;
#     string3 = forms.CharField() ;
#     date0 = forms.DateTimeField();
#     date1 = forms.DateTimeField();
#     date2 = forms.DateTimeField();
#     date3 = forms.DateTimeField();
#     boolean0 = forms.BooleanField();
#     boolean1 = forms.BooleanField();
#     boolean2 = forms.BooleanField();
#     boolean3 = forms.BooleanField();
#
# class mpi_result_sale_order_model_form(forms.ModelForm):
#     id = forms. IntegerField() ;
#     setGid = forms.UUIDField();
#     time_Gid = forms.UUIDField();
#     rule_Gid = forms.UUIDField();
#     inner_Gid = forms.UUIDField();
#     outer_Gid = forms.UUIDField();
#     name = forms.CharField() ;
#     type = forms.CharField() ;
#     isImmutable = forms.BooleanField();
#     numeric0 =  forms.DecimalField() ;
#     nt_numeric0 = forms. IntegerField();
#     numeric1 =  forms.DecimalField() ;
#     nt_numeric1 = forms. IntegerField();
#     numeric2 =  forms.DecimalField() ;
#     nt_numeric2 = forms. IntegerField();
#     numeric3 =  forms.DecimalField() ;
#     nt_numeric3 = forms. IntegerField();
#     string0 = forms.CharField() ;
#     string1 = forms.CharField() ;
#     string2 = forms.CharField() ;
#     string3 = forms.CharField() ;
#     date0 = forms.DateTimeField();
#     date1 = forms.DateTimeField();
#     date2 = forms.DateTimeField();
#     date3 = forms.DateTimeField();
#     boolean0 = forms.BooleanField();
#     boolean1 = forms.BooleanField();
#     boolean2 = forms.BooleanField();
#     boolean3 = forms.BooleanField();
#
# class mpi_result_sale_role_model_form(forms.ModelForm):
#     id = forms. IntegerField() ;
#     setGid = forms.UUIDField();
#     time_Gid = forms.UUIDField();
#     rule_Gid = forms.UUIDField();
#     inner_Gid = forms.UUIDField();
#     outer_Gid = forms.UUIDField();
#     name = forms.CharField() ;
#     type = forms.CharField() ;
#     isImmutable = forms.BooleanField();
#     numeric0 =  forms.DecimalField() ;
#     nt_numeric0 = forms. IntegerField();
#     numeric1 =  forms.DecimalField() ;
#     nt_numeric1 = forms. IntegerField();
#     numeric2 =  forms.DecimalField() ;
#     nt_numeric2 = forms. IntegerField();
#     numeric3 =  forms.DecimalField() ;
#     nt_numeric3 = forms. IntegerField();
#     string0 = forms.CharField() ;
#     string1 = forms.CharField() ;
#     string2 = forms.CharField() ;
#     string3 = forms.CharField() ;
#     date0 = forms.DateTimeField();
#     date1 = forms.DateTimeField();
#     date2 = forms.DateTimeField();
#     date3 = forms.DateTimeField();
#     boolean0 = forms.BooleanField();
#     boolean1 = forms.BooleanField();
#     boolean2 = forms.BooleanField();
#     boolean3 = forms.BooleanField();
#
# class mpi_role_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     roleclass_Gid = forms.UUIDField();
#     Agent_Gid = forms.UUIDField();
#     multiplier =  forms.DecimalField() ;
#     nt_multiplier = forms. IntegerField();
#     tbd1 = forms.CharField() ;
#     tbd2 = forms.CharField() ;
#
# class mpi_roleclass_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     description = forms.CharField() ;
#     tbd1 = forms.CharField() ;
#     tbd2 = forms.CharField() ;
#
# class mpi_sale_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     order_gid = forms.UUIDField();
#     LineItem = forms.CharField() ;
#     activityType_gid = forms.UUIDField();
#     ledgerDate = forms.DateTimeField() ;
#     territory_gid = forms.UUIDField();
#     product_gid = forms.UUIDField();
#     unitPrice =  forms.DecimalField() ;
#     nt_unitPrice = forms. IntegerField();
#     quantity =  forms.DecimalField() ;
#     nt_quantity = forms. IntegerField();
#     totalPrice =  forms.DecimalField() ;
#     nt_totalPrice = forms. IntegerField();
#
# class mpi_sys_flow_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     rulename = forms.CharField() ;
#     sequenceInFlow = forms. IntegerField();
#     parameterValueList = forms. IntegerField();
#     outerSetName = forms. IntegerField();
#     outerSetFilter = forms. IntegerField();
#     innerSetName = forms. IntegerField();
#     innerSetFilter = forms. IntegerField();
#     timeid = forms.CharField() ;
#     isImmutable = forms.BooleanField();
#     resultSetName = forms.CharField() ;
#
# class mpi_sys_rule_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     parameterList = forms.CharField() ;
#     outerSetClass = forms.CharField() ;
#     outerSetFilter = forms.CharField() ;
#     innerSetClass = forms.CharField() ;
#     innerSetFilter = forms.CharField() ;
#     behavior = forms.CharField() ;
#     customBehavior = forms.CharField() ;
#     logicalElementList = forms.CharField() ;
#     ruleOutputList = forms.CharField() ;
#     resultName = forms.CharField() ;
#     resultType = forms.CharField() ;
#
# class mpi_sys_time_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     periodStart = forms.DateTimeField() ;
#     periodStart = forms.DateTimeField() ;
#     type = forms.CharField() ;
#     group = forms.CharField() ;
#
# class mpi_territory_model_form(forms.ModelForm):
#     id = forms.CharField() ;
#     gid = forms.UUIDField();
#     setGid = forms.UUIDField();
#     effStart = forms.DateTimeField() ;
#     effEnd = forms.DateTimeField() ;
#     parent_gid = forms.UUIDField();
#     isDeleted = forms.BooleanField();
#     deleteDate = forms.DateTimeField() ;
#     altName = forms.CharField() ;
#     population = forms.CharField() ;
#     population = forms. IntegerField();
#     squareMiles =  forms.DecimalField() ;
#     nt_squareMiles = forms. IntegerField();
#     costBasis =  forms.DecimalField() ;
#     nt_costBasis = forms. IntegerField();
