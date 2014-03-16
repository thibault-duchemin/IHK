import io
from sqlalchemy import func
import numpy as np
from array import *

def state_name(state_name):
    return data.session.query(io.State).filter(io.State.name == state_name).all()

def generate_population(data):
    for state in data.session.query(io.State):
        generate_state_population(data, state)

def generate_state_population(data, state):
    #get only the "total population" entry for each district
    for district in data.session.query(io.District).filter(
            io.District.state == state.name).filter(
            io.District.classification == 'Total'):
        generate_district_population(data, state, district)

#Accept district and state objects, plus the Database object from io.py
def generate_district_population(data, state, district):
    mpce = data.session.query(io.Mpce).filter_by(state=state.name).first()
    #Bulk insert as per http://docs.sqlalchemy.org/en/rel_0_8/faq.html
    #split into multiple insertion waves due to memory limitations
    insertions_per_wave = 1000000
    #insert the population in waves of 1000000 people 
    for i in xrange(district.population_total/insertions_per_wave):
        insert_wave(data, state, district, mpce, insertions_per_wave)
        print 'wave inserted'
    #insert the last few people
    insert_wave(data, state, district, mpce, district.population_total % insertions_per_wave)
    #commit the changes; otherwise, they will be wasted!
    data.session.commit()
    print 'Population of', district.name, 'inserted'

def insert_wave(data, state, district, mpce, insertion_count):
    insert = io.Person.__table__.insert()
    data.engine.execute(insert, [generate_person_dict(data, state, district, mpce)
            for j in xrange(insertion_count)])

#generate a dict of values corresponding to the attributes of a Person
def generate_person_dict(data, state, district, mpce):
    #This is where math and statistics comes in
    return {'money': mpce.mpce_average, 'diabetes': 0.1,
            'cardio': 0.2, 'district': district.name, 'state': state.name,
            'classification': 'ignored'}

#THIS METHOD DOES NOT WORK
#It is kept as a reminder of why we can't generate the entire population at once
#Accept Database object from io.py as input
def generate_people(data):
    population = list()
    for state in data.session.query(io.State).all():
        for district in data.get_districts_by_state_name(state.name):
            for i in xrange(district.population_total):
                population.append(Person('money', 'diabetes', 'cardio', 
                    district.name, state.name, 'ignored'))
            print 'district', district.name
        print 'state', state.name
    return population


######################## below by RieK #########################

def pop_byState(state_name, class_type):
    return data.session.query(io.District.state, io.District.name, io.District.classification, func.sum(io.District.population_total)).filter(io.District.state == state_name).filter(io.District.classification == class_type).group_by(io.District.state).all()

def exp_byState(state_name, class_type):
    return data.session.query(io.Mpce.state, io.Mpce.mpce_type, io.Mpce.classification, io.Mpce.mpce_average).filter(io.Mpce.state == state_name).filter(io.Mpce.mpce_type == "mmrp").filter(io.Mpce.classification == class_type).all()

def exp_Percentile(state_name, class_type):
    return data.session.query(io.Mpce).filter(io.Mpce.state == state_name).filter(io.Mpce.mpce_type == "mmrp").filter(io.Mpce.classification == class_type).first()


def generate_people_expense(state_name, class_type):
    mean = exp_byState(state_name, class_type)[0][3]
    std = 10
    # For testing, only generating 100,000th of population
    pop = (pop_byState(state_name, "Rural")[0][3])/100000
    listP = (exp_Percentile(state_name, class_type)[0][2:11]).append(0,0)
    #for i in xrange(1:10):
    #    percentile+i = np.random.uniform(
    expenseList = np.random.normal(mean, std, pop)
    return expenseList[0:10]

if __name__ == "__main__":
    data = io.Database()
    print pop_byState("Tamil Nadu", "Rural")[0][3]
    print exp_byState("Tamil Nadu", "rural")[0][3]
    print exp_Percentile("Tamil Nadu", "rural").get_d_all(True)
    #listP = (exp_Percentile("Tamil Nadu", "rural")[0][2:11]).insert(0)
    #print listP

