from datetime import datetime as dt

class Person:
    
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        current_date = dt.strptime("01.01.2018", "%d.%m.%Y")
        birth_date = dt.strptime(self.birth_date, "%d.%m.%Y")
        return int((current_date - birth_date).days // 365.2425)

    def work(self):
        if self.gender == "male":
            return f"He is a {self.job}"
        elif self.gender == "female":
            return f"She is a {self.job}"
        else:
            return f"Is a {self.job}"

    def money(self):
        return f"{int(self.salary * 12 * self.working_years):,}".replace(",", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder",
                15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995",
                "designer", 2.2, 2150, "Austria", "Vienna")
    p3 = Person('Adam', 'Greene', '24.12.1961', 'director',
                36, 11000, 'England', 'London', 'male')

    print(p3.money())

    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
