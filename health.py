"""
REFERENCE

Hospital::equipmentLevel information
0 = Transport arranged for people
1 = Transport arranged for people
2 = Transport arranged for people
3 = Transport arranged for people
4 = Transport arranged for people
5 = Transport arranged for people
"""

class Solution:
    def __init__(self, zoneReach, treatmentRatePerYear, expertise, beginDate, endDate, operatingStatus):
        self.zoneReach = "KA" #modify to match: reach only Karnataka state
        self.treatmentRatePerYear = 2646000 #number of people treated per year by the whole system. Treatment definition = "went into Aravind System and met with one personel"
        self.expertise = "Eyecare" #Aravind System will only treat the patients that have problem related to Eyecare
        self.beginDate = 01-01-1976 #convert in the most common date format. By default if no month/day, first january
        self.endDate = "N/A" #system is still operating
        self.operatingStatus = 'Y'

class Hopital:
    def __init__(self, name, area, popTargeted, nbPopPaying, nbPopFree, popTreated, expertise)
        self.name = name
        self.area = {'locations': area[0], 'adress': area[1]} #area is a list with first element = [regions], second element = adress
        self.popTargeted = popTargeted
        self.popScreened = nbPopPaying + nbPopFree
        self.popTreated = popTreated #surgeries
        self.expertiseMain = expertise[0] # element is one of the main healthcare categories
        self.expertiseSpecific = expertise[1] # element is a list of specialties for the main category
        self.equipmentLevel = equipmentLevel #cf. equipmentLevel index
        self.nbOutpatientsFree
        self.nbOutpatientPaying = nbPopPaying
        self.nbSurgeryFree =
        self.nbSurgerySubsidized =
        self.nbSurgeryPay =
        self.priceSurgeryPay = 
        self.priceSurgerySubsidized = 900 #750*88%+2000*12% (balance between ICCE and ECCE)
        self.priceSurgeryFree = 0
        self.nbPopFree = nbPopFree #check sum free + paid = Screened






#possible merge 
class CommunityEye:
    def __init__()
        self.nbOutpatients
        self.costRegistration = 10

class VisionCenter:
    def __init__()
        self.nbOutpatients
        self.costRegistration = 10

class OutreachCamp:
    def __init__()
        self.nbOutpatients
        self.costRegistration = 0


Surgery (only Hospital)
        - Free 
        - Subsidized
        - Pay

OutPatient
        - Free (Hospital, Camps)
        - Paying (Hospital, VisionCenter(10Rpee), CommunityEyeClinic (10 Rpee)

class Cost:
    def __init__(self, Operation, Salary, Asset)
        self.Operation = 20 #info for cataract operation, in US $, can be converted in Ruppees, we will research it later
        self.Salary = 000
        self.Asset = 99

    class Cost.Operation:
        def __init__(self, diagnosticTest)
            self.costSurgery = '1000'
            self.costDiagnosisTest = '1000' #could be expanded in level1, level2, etc.
            self.cost = 1000 #tofinish

    class Cost.Salary:
        def __init__(self, salaryParamed, salarySurgeon)
            self.salaryParamed = '1000'
            self.salarySurgeon = '1000'

    class Cost.Activity:
        def __init__(costAssetsYearly, costEquipment)
            self.costAssetsYearly = '1000' #find in Aravind financials
            self.costEquipment = '1000'

class HumanResources: '''#number of personel per structure
    def __init__(self)
        self.Personel = 999
        self.TrainingLevel = 999

    class HumanResources.Personel:
        def __init__(self, numberSurgeonStructure1, numberParamedStructure2):
            numberSurgeonStructure1 = '1000' #Not sure exactly how to cross: structure type (whether Aravind System or Aravind Hospital or Eye camp center etc. with the level of competencies)
            numberParamedStructure2 = '1000'

    class HumanResources.TrainingLevel:
        def __init__(self, programEmployeeFormation, programEmployeeWelfare, programSelfDevelopment, programMotherInclusion)
            self.programEmployeeFormation = 1 #general method: Binary level for presence of the program. 0 if no, 1 if yes. Final score as a float between 0 and 1 as # of Yes / # of total programs
            self.programSelfDevelopment = 1
            self.programEmployeeWelfare = 1
            self.programMotherInclusion = 1

        def levelScore(self):
            return (programMotherInclusion + programEmployeeWelfare + programSelfDevelopment + programEmployeeFormation) /(4)
class 




        print 'initializing Aravind System'



#Parent


    #patient in class Person
    def visit_or_not(self, patient):
        if not patient.money>self.visit_cost:
            print 'patient cannot afford treatment'
            return False
        if patient.diabetes > threshold_diabetes and patient.cardio > threshold_cardio:
            print "patient in good health, no need to consult"
            return False
        return True

    solution_id = 1
    zoneReach = #Karnataka
    treatment_rate = 

class 
'''