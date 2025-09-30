from django.db import models

class AppSetting(models.Model):
    file_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.file_path

class LnTMain(models.Model):
    date = models.DateField(auto_now=True)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    reportType = models.CharField(max_length=255, blank=True, null=True)
    
class LnTDIGITAL_INPUT(models.Model):
    lntmain = models.ForeignKey(LnTMain, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    sln = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    lnt_val = models.CharField(max_length=255, blank=True, null=True)
    exp_val = models.CharField(max_length=255, blank=True, null=True)
    ref_val = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lnt_val_H = models.CharField(max_length=255, blank=True, null=True)
    exp_val_H = models.CharField(max_length=255, blank=True, null=True)
    ref_val_H = models.CharField(max_length=255, blank=True, null=True)
    status_H = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    data_on = models.CharField(max_length=255, blank=True, null=True)


class LnTDIGITAL_OUTPUT(models.Model):
    lntmain = models.ForeignKey(LnTMain, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    sln = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    lnt_val = models.CharField(max_length=255, blank=True, null=True)
    exp_val = models.CharField(max_length=255, blank=True, null=True)
    ref_val = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lnt_val_H = models.CharField(max_length=255, blank=True, null=True)
    exp_val_H = models.CharField(max_length=255, blank=True, null=True)
    ref_val_H = models.CharField(max_length=255, blank=True, null=True)
    status_H = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    data_on = models.CharField(max_length=255, blank=True, null=True)


class LnTANALOG_INPUT(models.Model):
    lntmain = models.ForeignKey(LnTMain, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    sln = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    lnt_val = models.CharField(max_length=255, blank=True, null=True)
    exp_val = models.CharField(max_length=255, blank=True, null=True)
    ref_val = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    
    lnt_val_N_10 = models.CharField(max_length=255, blank=True, null=True)
    exp_val_N_10 = models.CharField(max_length=255, blank=True, null=True)
    ref_val_N_10 = models.CharField(max_length=255, blank=True, null=True)
    status_N_10 = models.CharField(max_length=255, blank=True, null=True)
    
    lnt_val_P_10 = models.CharField(max_length=255, blank=True, null=True)
    exp_val_P_10 = models.CharField(max_length=255, blank=True, null=True)
    ref_val_P_10 = models.CharField(max_length=255, blank=True, null=True)
    status_P_10 = models.CharField(max_length=255, blank=True, null=True)
    
    address = models.CharField(max_length=255, blank=True, null=True)
    data_on = models.CharField(max_length=255, blank=True, null=True)


class LnTANALOG_OUTPUT(models.Model):
    lntmain = models.ForeignKey(LnTMain, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    sln = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    lnt_val = models.CharField(max_length=255, blank=True, null=True)
    exp_val = models.CharField(max_length=255, blank=True, null=True)
    ref_val = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    
    lnt_val_N_10 = models.CharField(max_length=255, blank=True, null=True)
    exp_val_N_10 = models.CharField(max_length=255, blank=True, null=True)
    ref_val_N_10 = models.CharField(max_length=255, blank=True, null=True)
    status_N_10 = models.CharField(max_length=255, blank=True, null=True)
    
    lnt_val_P_10 = models.CharField(max_length=255, blank=True, null=True)
    exp_val_P_10 = models.CharField(max_length=255, blank=True, null=True)
    ref_val_P_10 = models.CharField(max_length=255, blank=True, null=True)
    status_P_10 = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    data_on = models.CharField(max_length=255, blank=True, null=True)


class LnT_AIO_Test(models.Model):
    lntmain = models.ForeignKey(LnTMain, on_delete=models.CASCADE)

    # Resistance Fields
    AIO_R1 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R2 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R3 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R4 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R5 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R6 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R7 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R8 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R9 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R10 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R11 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R12 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R13 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R14 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R15 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R16 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R17 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R18 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R19 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R20 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R21 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R22 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R23 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R24 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R25 = models.CharField(max_length=255, blank=True, null=True)
    AIO_R26 = models.CharField(max_length=255, blank=True, null=True)

    # Voltage Fields
    AIO_V1 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V2 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V3 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V4 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V5 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V6 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V7 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V8 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V9 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V10 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V11 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V12 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V13 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V14 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V15 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V16 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V17 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V18 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V19 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V20 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V21 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V22 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V23 = models.CharField(max_length=255, blank=True, null=True)
    AIO_V24 = models.CharField(max_length=255, blank=True, null=True)
    

    # Fascia LED Checkboxes
    AIO_LED1 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED2 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED3 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED4 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED5 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED6 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED7 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED8 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED9 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED10 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED11 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED12 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED13 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED14 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED15 = models.CharField(max_length=255, blank=True, null=True)
    AIO_LED16 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"AIO Test for {self.lntmain}"
    
class LnT_DI_Test(models.Model):
    lntmain = models.ForeignKey(LnTMain, on_delete=models.CASCADE)

    # Resistance Fields (Ohm)
    R1 = models.CharField(max_length=255, blank=True, null=True)
    R2 = models.CharField(max_length=255, blank=True, null=True)
    R3 = models.CharField(max_length=255, blank=True, null=True)
    R4 = models.CharField(max_length=255, blank=True, null=True)
    R5 = models.CharField(max_length=255, blank=True, null=True)
    R6 = models.CharField(max_length=255, blank=True, null=True)
    R7 = models.CharField(max_length=255, blank=True, null=True)
    R8 = models.CharField(max_length=255, blank=True, null=True)
    R9 = models.CharField(max_length=255, blank=True, null=True)
    R10 = models.CharField(max_length=255, blank=True, null=True)
    R11 = models.CharField(max_length=255, blank=True, null=True)
    R12 = models.CharField(max_length=255, blank=True, null=True)

    R13 = models.CharField(max_length=255, blank=True, null=True)
    R14 = models.CharField(max_length=255, blank=True, null=True)
    R15 = models.CharField(max_length=255, blank=True, null=True)
    R16 = models.CharField(max_length=255, blank=True, null=True)
    R17 = models.CharField(max_length=255, blank=True, null=True)
    R18 = models.CharField(max_length=255, blank=True, null=True)
    R19 = models.CharField(max_length=255, blank=True, null=True)
    R20 = models.CharField(max_length=255, blank=True, null=True)
    R21 = models.CharField(max_length=255, blank=True, null=True)
    R22 = models.CharField(max_length=255, blank=True, null=True)
    R23 = models.CharField(max_length=255, blank=True, null=True)
    R24 = models.CharField(max_length=255, blank=True, null=True)

    R25 = models.CharField(max_length=255, blank=True, null=True)
    R26 = models.CharField(max_length=255, blank=True, null=True)
    R27 = models.CharField(max_length=255, blank=True, null=True)
    R28 = models.CharField(max_length=255, blank=True, null=True)
    R29 = models.CharField(max_length=255, blank=True, null=True)
    R30 = models.CharField(max_length=255, blank=True, null=True)
    R31 = models.CharField(max_length=255, blank=True, null=True)
    R32 = models.CharField(max_length=255, blank=True, null=True)
    R33 = models.CharField(max_length=255, blank=True, null=True)
    R34 = models.CharField(max_length=255, blank=True, null=True)
    R35 = models.CharField(max_length=255, blank=True, null=True)
    R36 = models.CharField(max_length=255, blank=True, null=True)

    R37 = models.CharField(max_length=255, blank=True, null=True)
    R38 = models.CharField(max_length=255, blank=True, null=True)
    R39 = models.CharField(max_length=255, blank=True, null=True)
    R40 = models.CharField(max_length=255, blank=True, null=True)
    R41 = models.CharField(max_length=255, blank=True, null=True)
    R42 = models.CharField(max_length=255, blank=True, null=True)
    R43 = models.CharField(max_length=255, blank=True, null=True)
    R44 = models.CharField(max_length=255, blank=True, null=True)
    R45 = models.CharField(max_length=255, blank=True, null=True)
    R46 = models.CharField(max_length=255, blank=True, null=True)
    R47 = models.CharField(max_length=255, blank=True, null=True)
    R48 = models.CharField(max_length=255, blank=True, null=True)





    # Voltage Fields (Volts)
    V1 = models.CharField(max_length=255, blank=True, null=True)
    V2 = models.CharField(max_length=255, blank=True, null=True)
    V3 = models.CharField(max_length=255, blank=True, null=True)
    V4 = models.CharField(max_length=255, blank=True, null=True)
    V5 = models.CharField(max_length=255, blank=True, null=True)
    V6 = models.CharField(max_length=255, blank=True, null=True)
    V7 = models.CharField(max_length=255, blank=True, null=True)
    V8 = models.CharField(max_length=255, blank=True, null=True)
    V9 = models.CharField(max_length=255, blank=True, null=True)
    V10 = models.CharField(max_length=255, blank=True, null=True)
    V11 = models.CharField(max_length=255, blank=True, null=True)
    V12 = models.CharField(max_length=255, blank=True, null=True)

    # Fascia LED Checkboxes
    checkbox_26 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_27 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_28 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_29 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_30 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_31 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_32 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_33 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_34 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_35 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_36 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_37 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_38 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_39 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_40 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_41 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_42 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_43 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_44 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_45 = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"DI Test for {self.lntmain}"
    
class LnT_DO_Test(models.Model):
    lntmain = models.ForeignKey(LnTMain, on_delete=models.CASCADE)

    # Resistance Fields
    R1 = models.CharField(max_length=255, blank=True, null=True)
    R2 = models.CharField(max_length=255, blank=True, null=True)
    R3 = models.CharField(max_length=255, blank=True, null=True)
    R4 = models.CharField(max_length=255, blank=True, null=True)
    R5 = models.CharField(max_length=255, blank=True, null=True)
    R6 = models.CharField(max_length=255, blank=True, null=True)
    R7 = models.CharField(max_length=255, blank=True, null=True)
    R8 = models.CharField(max_length=255, blank=True, null=True)
    R9 = models.CharField(max_length=255, blank=True, null=True)
    R10 = models.CharField(max_length=255, blank=True, null=True)
    R11 = models.CharField(max_length=255, blank=True, null=True)
    R12 = models.CharField(max_length=255, blank=True, null=True)
    R13 = models.CharField(max_length=255, blank=True, null=True)
    R14 = models.CharField(max_length=255, blank=True, null=True)
    R15 = models.CharField(max_length=255, blank=True, null=True)
    R16 = models.CharField(max_length=255, blank=True, null=True)
    R17 = models.CharField(max_length=255, blank=True, null=True)
    R18 = models.CharField(max_length=255, blank=True, null=True)
    R19 = models.CharField(max_length=255, blank=True, null=True)
    R20 = models.CharField(max_length=255, blank=True, null=True)
    R21 = models.CharField(max_length=255, blank=True, null=True)
    R22 = models.CharField(max_length=255, blank=True, null=True)
    

    # Voltage Fields
    V1 = models.CharField(max_length=255, blank=True, null=True)
    V2 = models.CharField(max_length=255, blank=True, null=True)
    V3 = models.CharField(max_length=255, blank=True, null=True)
    V4 = models.CharField(max_length=255, blank=True, null=True)
    V5 = models.CharField(max_length=255, blank=True, null=True)
    V6 = models.CharField(max_length=255, blank=True, null=True)
    V7 = models.CharField(max_length=255, blank=True, null=True)
    V8 = models.CharField(max_length=255, blank=True, null=True)
    V9 = models.CharField(max_length=255, blank=True, null=True)
    V10 = models.CharField(max_length=255, blank=True, null=True)
    V11 = models.CharField(max_length=255, blank=True, null=True)
    V12 = models.CharField(max_length=255, blank=True, null=True)
    V13 = models.CharField(max_length=255, blank=True, null=True)
    V14 = models.CharField(max_length=255, blank=True, null=True)
    V15 = models.CharField(max_length=255, blank=True, null=True)
    V16 = models.CharField(max_length=255, blank=True, null=True)
    V17 = models.CharField(max_length=255, blank=True, null=True)
    V18 = models.CharField(max_length=255, blank=True, null=True)
    V19 = models.CharField(max_length=255, blank=True, null=True)
    V20 = models.CharField(max_length=255, blank=True, null=True)


    # Fascia LED Checkboxes
    checkbox_26 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_27 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_28 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_29 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_30 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_31 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_32 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_33 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_34 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_35 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_36 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_37 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_38 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_39 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_40 = models.CharField(max_length=255, blank=True, null=True)
    checkbox_41 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"DO Test for {self.lntmain}"
    
class LTMainDetails(models.Model):
    # Left Section
    product_description = models.CharField(max_length=255, blank=True, null=True)
    cat_no = models.CharField(max_length=255, blank=True, null=True)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    manufacturing_date = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    project_no = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_reference_no = models.CharField(max_length=255, blank=True, null=True)

    # Right Section
    bill_of_material = models.CharField(max_length=255, blank=True, null=True)
    ga_assembly_instruction = models.CharField(max_length=255, blank=True, null=True)
    test_instruction = models.CharField(max_length=255, blank=True, null=True)
    manufacturing = models.CharField(max_length=255, blank=True, null=True)
    date1 = models.CharField(max_length=255, blank=True, null=True)
    quality_control_review = models.CharField(max_length=255, blank=True, null=True)
    date2 = models.CharField(max_length=255, blank=True, null=True)
    customer_inspection = models.CharField(max_length=255, blank=True, null=True)
    date3 = models.CharField(max_length=255, blank=True, null=True)
    tested_by1 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.project_name} - {self.customer_name}"
    
class LnTSscCard(models.Model):
    # Left Section
    type = models.CharField(max_length=255, blank=True, null=True)
    obseredval1 = models.CharField(max_length=255, blank=True, null=True)
    obseredval2 = models.CharField(max_length=255, blank=True, null=True)
    obseredval3 = models.CharField(max_length=255, blank=True, null=True)
    obseredval4 = models.CharField(max_length=255, blank=True, null=True)
    obseredval5 = models.CharField(max_length=255, blank=True, null=True)
    obseredval6 = models.CharField(max_length=255, blank=True, null=True)
    obseredval7 = models.CharField(max_length=255, blank=True, null=True)
    obseredval8 = models.CharField(max_length=255, blank=True, null=True)
    status1 = models.CharField(max_length=255, blank=True, null=True)
    status2 = models.CharField(max_length=255, blank=True, null=True)
    status3 = models.CharField(max_length=255, blank=True, null=True)
    status4 = models.CharField(max_length=255, blank=True, null=True)
    status5 = models.CharField(max_length=255, blank=True, null=True)
    status6 = models.CharField(max_length=255, blank=True, null=True)
    status7 = models.CharField(max_length=255, blank=True, null=True)
    status8 = models.CharField(max_length=255, blank=True, null=True)

    
    def __str__(self):
        return f"{self.type}"