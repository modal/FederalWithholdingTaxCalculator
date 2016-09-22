from itertools import izip
import sys
##############################################################################
#US Federal Tax Withholding Calculator
#http://payroll.wsu.edu/cgi-bin/withhold2016.cgi
#See IRS 2016 Publication 15
##############################################################################
#Program Inputs
#   Gross Pay
#   Marital Status
#   Pay Schedule
#   Allowance Count
##############################################################################
#TODO
#Create tkinter interface
##############################################################################
USAGE = """
Command line Use:

fwt.py gross_pay marital_status pay_period allowances

------------------------------------------------------------------------------

Marital Status Options
    single
    married

Pay Period Options
    weekly
    biweekly
    semimonthly
    quarterly
    semiannually
    annually
    daily
"""


Allowance = {   "weekly"        :     77.90,
                "biweekly"      :    155.50,
                "semimonthly"   :    168.80,
                "monthly"       :    337.50,
                "quarterly"     :   1012.50,
                "semiannually"  :   2025.00,
                "annually"      :   4050.00,
                "daily"         :     15.60}

rate = [10.0, 15.0, 25.0, 28.0, 33.0, 35.0, 39.6]

bracket =   {  "single"         :
            {  "weekly"         :   "TBD",
                "biweekly"      :   "TBD",
                "semimonthly"   :   "TBD",
                "monthly"       :   "TBD",
                "quarterly"     :   "TBD",
                "semiannually"  :   "TBD",
                "annually"      :   "TBD",
                "daily"         :   "TBD"},

                 "married"      :
            {  "weekly"         :   "TBD",
                "biweekly"      :   "TBD",
                "semimonthly"   :   [356, 1129, 3494, 6685, 10000, 17579, 19813],
                "monthly"       :   "TBD",
                "quarterly"     :   "TBD",
                "semiannually"  :   "TBD",
                "annually"      :   "TBD",
                "daily"         :   "TBD"}
            }
##############################################################################
mstatus = "married"
pay_period = "semimonthly"
gross = 8000.00
allowance_cnt = 8

if 5 != len(sys.argv):
    print(USAGE)
    sys.exit()
else:
    gross   = float(sys.argv[1])
    mstatus = sys.argv[2].lower()
    pay_period = sys.argv[3].lower()
    allowance_cnt = int(sys.argv[4])

postallowance = gross - Allowance[pay_period] * allowance_cnt
#print "After allowances", postallowance

tax = 0
for r, b in izip(rate[::-1], bracket[mstatus][pay_period][::-1]):
    btax=0.0
    if postallowance > b:
        btax += (postallowance - b) * r/100.0
        postallowance = b
    print "{0}% bracket =  {1:10.2f}".format(r, btax)
    tax += btax

print "2016 Federal Withholding Tax= %6.2f" % (tax)

if __name__ == "__main__":
    pass
