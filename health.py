import random

class Aravind(object):
    #Use this to assign each hospital to cover surrounding districts
    #Based on Aravind's data
    #A more robust approach would be to define adjacencies for all districts
    covered_district_mapping = {
                'Coimbatore': ['Coimbatore', 'Nilgiris', 'Kollam'],
                'Dindigul': ['Dindigul'],
                'Madurai': ['Ariyalur', 'Dharmapuri', 'Karur', 'Madurai', 
                    'Nagapattinam', 'Namakkal', 'Perambalur', 'Pudukkottai',
                    'Ramanathapuram', 'Siviganga', 'Thanjavur', 'Thiruvarur',
                    'Tiruchirappalli', 'Virudhunagar'],
                'Pondicherry': ['Chennai', 'Cuddalore', 'Kanchipuram',
                    'Krishnagiri', 'Thiruvallur', 'Tiruvannamalai',
                    'Vellore', 'Villupuram'],
                'Salem': ['Erode', 'Salem'],
                'Theni': ['Theni', 'Kottayam', 'Iduki'],
                'Tirunelveli': ['Kanniyakumari', 'Thoothukudi', 'Tirunelveli'],
                'Tiruppur': ['Tiruppur'],
                #These are not from the google drive
                'Tuticorin': ['Tuticorin'],
                'Udumalaipet': ['Udumalaipet']}

    def __init__(self, eye_health_treatment_thresholds):
        self.district_names = ['Madurai', 'Theni', 'Tirunelveli', 
                'Coimbatore', 'Pondicherry', 'Dindigul', 'Tiruppur', 'Salem',
                'Tuticorin', 'Udumalaipet']
        self.treatment_costs = {
                'hospital': 500,
                'clinic': 200,
                'vision_center': 100,
                'camp': 20}
        #FROM DATA
        self.urban_hospital_probability = 0.915
        self.urban_clinic_probability = 1 - self.urban_hospital_probability
        self.rural_vision_center_probability = 0.397
        self.rural_camp_probability = 1 - self.rural_vision_center_probability
        self._init_facilities()

    def _init_facilities(self):
        self.hospitals = list()
        self.clinics = list()
        self.vision_centers = list()
        self.camps = list()
        self._init_hospitals()
        self._init_clinics()
        self._init_vision_centers()
        self._init_camps()

    def _init_hospitals(self):
        treatment_cost = self.treatment_costs['hospital']
        treatable_problems = ['cataracts', 'glasses']
        for district_name in self.district_names:
            self.hospitals.append(Hospital(district_name, 
                treatment_cost, treatable_problems))

    def _init_clinics(self):
        treatment_cost = self.treatment_costs['clinic']
        treatable_problems = ['glasses']
        for district_name in self.district_names:
            self.clinics.append(Clinic(district_name,
                treatment_cost, treatable_problems))

    def _init_vision_centers(self):
        treatment_cost = self.treatment_costs['vision_center']
        treatable_problems = ['glasses']
        for district_name in self.district_names:
            self.vision_centers.append(VisionCenter(district_name,
                treatment_cost, treatable_problems))

    def _init_camps(self):
        treatment_cost = self.treatment_costs['camp']
        treatable_problems = ['glasses']
        for district_name in self.district_names:
            self.vision_centers.append(Camp(district_name,
                treatment_cost, treatable_problems))

    #True if treatment was done, False otherwise
    def treat(self, person):
        #Assign the person to a type of facility randomly
        rnd = random.random()
        if person.classification == 'urban':
            if rnd <= self.urban_hospital_probability:
                treatment_facility = 'hospitals'
            else:
                treatment_facility = 'clinics'
        elif person.classification == 'rural':
            if rnd <= self.rural_vision_center_probability:
                treatment_facility = 'vision_centers'
            else:
                treatment_facility = 'camps'
        return self.treat_with_facility(treatment_facility, person)

    #True if treatment was done, False otherwise
    def treat_with_facility(self, treatment_facility, person):
        #Now that we know the type of facility
        #Find a facility that can cover the patient and have it treat them
        facility_list = getattr(self, treatment_facility)
        for facility in facility_list:
            if facility.covers_person(person):
                return facility.treat(person)
        return False

#Generic class which includes Hospital, EyeClinic, and VisionCamp
class AravindFacility(object):
    def __init__(self, district_name, treatment_cost, treatable_problems):
        self.district_name = district_name
        self.treatment_cost = treatment_cost
        self.treatable_problems = treatable_problems
        self._init_covered_districts()

    def _init_covered_districts(self):
        #Use Python version of "switch statement"
        self.covered_districts = Aravind.covered_district_mapping[
                self.district_name]

    #True if the district is in the list of districts this hospital covers
    def covers_person(self, person):
        return person.district in self.covered_districts

    def treat(self, person):
        for problem in self.treatable_problems:
            self.treat_problem(problem, person)
        self.charge_fee(person)

    #problem is a string containing the name of the
    # problem: "", for example
    def treat_problem(self, problem, person):
        health_utility_improvement = {
                'surgery': 0.14,    #FROM DATA
                'glasses': 0.05     #ASSUMPTION
                }[problem]
        person.health_utility += health_utility_improvement

    #Overwritten by subclasses
    def charge_fee(self, person):
        pass

class Hospital(AravindFacility):

    def charge_fee(self, person):
        person.money -= self.treatment_cost

class Clinic(AravindFacility):

    def charge_fee(self, person):
        person.money -= self.treatment_cost

class VisionCenter(AravindFacility):

    def charge_fee(self, person):
        person.money -= self.treatment_cost

class Camp(AravindFacility):

    def charge_fee(self, person):
        person.money -= self.treatment_cost

'''
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

"""
Surgery (only Hospital)
        - Free 
        - Subsidized
        - Pay

OutPatient
        - Free (Hospital, Camps)
        - Paying (Hospital, VisionCenter(10Rpee), CommunityEyeClinic (10 Rpee)
"""

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

class HumanResources: """#number of personel per structure
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
    location = #Karnataka
    treatment_rate = 

class 
"""
'''

if __name__ == "__main__":
    #This is very bad right now because the Solution __init__ method isn't
    #fully developed yet. But this is an example of how to work with a class
    aravind = Solution(location = 'Karnataka', expertise = 'eyecare',
            start_date = 'TODO', end_date = None, is_operating = True)
