# ONE STOP INSURANCE COMPANY customer policy system
# FILE READ WRITE APPEND DETAILED AND EXCEPTION REPORTS
# Author: Phil St Croix
# Written: Mar 18, 2023

import datetime
import FormatValues as FV

def get_detail_report():

    # Get todays date
    today = datetime.datetime.now()

    # declare constants needed for calculations
    EXTRA_LIAB = 130.00
    GLASS_LIAB = 86.00
    LOAN_CAR_LIAB = 58.00
    HST_RATE = 0.15
    PROCESS_FEE = 39.99

    # create report  detail report header
    print()
    print("ONE STOP INSURANCE COMPANY")
    print(F"POLICY LISTING AS OF {FV.FDateM(today)}")
    print()
    print("POLICY CUSTOMER              INSURANCE     EXTRA      TOTAL")
    print("NUMBER NAME                   PREMIUM      COSTS     PREMIUM")
    print("=============================================================")

    #  accumulator counters can be set to zero here
    totalPolicyAcc = 0
    insPremACC = 0
    totalExtraCostAcc = 0
    totalInsPremACC = 0

    # open policies.dat and loop thru it
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

            # create the detailed report body
            print(f"{policyNum:>5d}  {fullName:<20s}  {FV.FDollar2(insPrem):>9s}  {FV.FDollar2(extraCostCtr):>9s}   {FV.FDollar2(totalPrem):>9s}")

            # increment counters and accumulators
            totalPolicyAcc += 1
            insPremACC += insPrem
            totalExtraCostAcc += extraCostCtr
            totalInsPremACC += totalPrem

    # create detailed report footer including accumulator totals
    print("=============================================================")
    print(f"Total Policies: {totalPolicyAcc:>3d}         {FV.FDollar2(insPremACC):>9s}  {FV.FDollar2(totalExtraCostAcc):>9s}  {FV.FDollar2(totalInsPremACC):>9s}")

detailReport = get_detail_report()