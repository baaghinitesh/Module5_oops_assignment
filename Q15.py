# 15. Implement a static method in a class that checks if a given year is a leap year.

class YearUtils:
    @staticmethod
    def is_leap_year(year):
        """Check if a given year is a leap year."""
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

if __name__ == "__main__":
    year = int(input("enter year to cheq it is leapyear or not : "))
    
    if YearUtils.is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
