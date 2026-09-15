from faker import Faker

fake = Faker("ru_RU")

APPROVED_CARD = "4444 4444 4444 4441"
DECLINED_CARD = "4444 4444 4444 4442"

VALID_MONTH = "12"
VALID_YEAR = "26"
VALID_OWNER = "IVANOV IVAN"
VALID_CVC = "123"

VALID_OWNER_RANDOM = fake.last_name().upper() + " " + fake.first_name().upper()
