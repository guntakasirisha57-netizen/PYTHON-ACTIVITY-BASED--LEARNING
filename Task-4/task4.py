#python source code

START
INPUT basic, allowances, overtime, incentives

gross = basic + allowances + overtime + incentives

IF gross <= 10000
    deduction = gross * 0.05
ELSE IF gross <= 20000
    deduction = 500 + (gross-10000) * 0.10
ELSE
    deduction = 1500 + (gross-20000) * 0.15
END IF

net = gross - deduction

PRINT gross, deduction, net
STOP
