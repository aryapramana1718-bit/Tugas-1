"""
main.py
Demonstration of Studi Kasus 1 classes and relationships.
Run: python main.py
"""

from models import Address, Student, Professor, Person

def demo():
    # Create address
    addr = Address('123 Elm St', 'Springfield', 'IL', 62704, 'USA')
    print('Address valid?', addr.validate())
    print("\nAddress label:\n", addr.outputAsLabel())
    print('---')

    # Create person
    p = Person('Alice Example', '555-1234', 'alice@example.com')
    p.purchaseParkingPass()
    print(p.name, 'has parking pass?', p.hasParkingPass())
    print('---')

    # Create professor
    prof = Professor('Dr. John', staffNumber=1001, salary=80000, yearsOfService=12, numberOfClasses=3)
    prof.set_address(addr)

    # Create students
    s1 = Student('Bob Student', studentNumber=2001, averageMark=75)
    s2 = Student('Carol Student', studentNumber=2002, averageMark=58)

    # Professor supervises students
    prof.supervise(s1)
    prof.supervise(s2)
    print(f"Professor {prof.name} supervises: {[s.name for s in prof.list_supervisees()]}")
    print(f"Student {s1.name} supervisors: {[p.name for p in s1.supervisors]}")
    print('---')

    # Check eligibility
    print(s1.name, 'eligible?', s1.isEligibleToEnroll('CS101'))
    print(s2.name, 'eligible?', s2.isEligibleToEnroll('CS101'))

    # Demonstrate seminar count
    s1.add_seminar(2)
    print(s1.name, 'seminars taken:', s1.getSeminarsTaken())

if __name__ == '__main__':
    demo()