"""
models.py
Implementation for Studi Kasus 1:
Classes: Address, Person, Student, Professor
"""

from typing import List, Optional

class Address:
    def __init__(self, street: str, city: str, state: str, postalCode: int, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

    def validate(self) -> bool:
        """Simple validation: ensure required fields present and postalCode positive."""
        if not all([self.street, self.city, self.state, self.country]):
            return False
        if not isinstance(self.postalCode, int) or self.postalCode <= 0:
            return False
        return True

    def outputAsLabel(self) -> str:
        """Return formatted address label."""
        return f"{self.street}\n{self.city}, {self.state} {self.postalCode}\n{self.country}"


class Person:
    def __init__(self, name: str, phoneNumber: str = '', emailAddress: str = '', address: Optional[Address] = None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address
        self._has_parking_pass = False

    def purchaseParkingPass(self) -> None:
        """Mark this person as having purchased a parking pass."""
        self._has_parking_pass = True

    def hasParkingPass(self) -> bool:
        return self._has_parking_pass

    def set_address(self, address: Address) -> None:
        self.address = address

    def get_address_label(self) -> str:
        if self.address:
            return self.address.outputAsLabel()
        return 'No address set'


class Student(Person):
    def __init__(self, name: str, studentNumber: int, averageMark: int = 0, phoneNumber: str = '', emailAddress: str = '', address: Optional[Address] = None):
        super().__init__(name, phoneNumber, emailAddress, address)
        self.studentNumber = studentNumber
        self.averageMark = averageMark
        self._seminars_taken = 0
        self.supervisors: List['Professor'] = []

    def isEligibleToEnroll(self, program_code: str = '') -> bool:
        """Placeholder logic: eligible if averageMark >= 60."""
        return self.averageMark >= 60

    def getSeminarsTaken(self) -> int:
        return self._seminars_taken

    def add_seminar(self, n: int = 1) -> None:
        self._seminars_taken += n

    def add_supervisor(self, prof: 'Professor') -> None:
        if prof not in self.supervisors:
            if len(self.supervisors) >= 5:
                raise ValueError('A student cannot have more than 5 supervisors.')
            self.supervisors.append(prof)
            prof._add_supervisee(self)

    def remove_supervisor(self, prof: 'Professor') -> None:
        if prof in self.supervisors:
            self.supervisors.remove(prof)
            prof._remove_supervisee(self)


class Professor(Person):
    def __init__(self, name: str, staffNumber: int, salary: int = 0, yearsOfService: int = 0, numberOfClasses: int = 0, phoneNumber: str = '', emailAddress: str = '', address: Optional[Address] = None):
        super().__init__(name, phoneNumber, emailAddress, address)
        self.salary = salary
        self.staffNumber = staffNumber
        self.yearsOfService = yearsOfService
        self.numberOfClasses = numberOfClasses
        self.supervisees: List[Student] = []

    def _add_supervisee(self, student: Student) -> None:
        if student not in self.supervisees:
            self.supervisees.append(student)

    def _remove_supervisee(self, student: Student) -> None:
        if student in self.supervisees:
            self.supervisees.remove(student)

    def supervise(self, student: Student) -> None:
        """Public API to add supervisee (will add reciprocal link)."""
        student.add_supervisor(self)

    def stop_supervising(self, student: Student) -> None:
        student.remove_supervisor(self)

    def list_supervisees(self):
        return list(self.supervisees)