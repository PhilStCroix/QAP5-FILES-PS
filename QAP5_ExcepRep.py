# ONE STOP INSURANCE COMPANY customer policy system
# FILE READ WRITE APPEND EXCEPTION REPORTS
# Author: Phil St Croix
# Written: Mar 18, 2023

import datetime
import FormatValues as FV

def get_exception_report():

    # Get todays date
    today = datetime.datetime.now()

    # declare constants needed for calculations
    EXTRA_LIAB = 130.00
    GLASS_LIAB = 86.00
    LOAN_CAR_LIAB = 58.00
    HST_RATE = 0.15
    PROCESS_FEE = 39.99

    # create Exception report header
    print()
    print("ONE STOP INSURANCE COMPANY")
    print(f"MONTHLY PAYMENT LISTING AS OF {FV.FDateM(today)}")
    print()
    print("POLICY CUSTOMER              TOTAL                 TOTAL      MONTHLY")
    print("NUMBER NAME                  PREMIUM     HST       COST       PAYMENT")
    print("======================================================================")

    # accumulators and counters set to zero here
    totalPolicyAcc = 0
    totalInsPremAcc = 0
    totalHstAcc = 0
    totalCostAcc = 0
    totalMonthlyPayAcc = 0

    # open policies.dat
    with open('policies.dat', 'r') as f:
        for policyDataLine in f:
            policyLine = policyDataLine.split(',')
            policyNum = int(policyLine[0].strip())
            firstName = policyLine[1].strip()
            lastName = policyLine[2].strip()
            fullName = firstName + ' ' + lastName
            numCars = int(policyLine[8].strip())
            extraLiab = policyLine[9].strip()
            glassLiab = policyLine[10].strip()
            loanCarLiab = policyLine[11].strip()
            # perform all calculations each time thru loop
            # initialize extra cost inner accumulator
            extraCostCtr = 0
            if extraLiab == 'Y':
                extraLiabAmt = numCars * EXTRA_LIAB
                extraCostCtr += extraLiabAmt
            if glassLiab == 'Y':
                glassLiabAmt = numCars * GLASS_LIAB
                extraCostCtr += glassLiabAmt
            if loanCarLiab == 'Y':
                loanCarLiab = numCars * LOAN_CAR_LIAB
                extraCostCtr += loanCarLiab
            insPrem = float(policyLine[-1].strip())
            totalPrem = insPrem + extraCostCtr
            HST = insPrem * HST_RATE
            totalCost = insPrem + HST
            monPay = (totalCost + PROCESS_FEE) / 12
            paymentType = policyLine[12].strip()
            # create the exception report body
            if paymentType == 'M':
                print(f"{policyNum:>5d}  {fullName:<20s} {FV.FDollar2(insPrem):>9s} {FV.FDollar2(HST):>9s}   {FV.FDollar2(totalCost):>9s}  {FV.FDollar2(monPay):>9s}")
                # increment counter and accumulators for every Monthly account
                totalPolicyAcc += 1
                totalInsPremAcc += insPrem
                totalHstAcc += HST
                totalCostAcc += totalCost
                totalMonthlyPayAcc += monPay

    # create the exception report footer including accumulator totals
    print("======================================================================")
    print(f"Total Policies: {totalPolicyAcc:>3d}        {FV.FDollar2(totalInsPremAcc):>9s} {FV.FDollar2(totalHstAcc):>9s}  {FV.FDollar2(totalCostAcc):>9s}  {FV.FDollar2(totalMonthlyPayAcc):>9s}")

exceptionReport = get_exception_report()