PATH = "./data/autos.csv"

TRAIN_COLUMN = {
    'dateCrawled':str, 
    'name':str, 
    'seller':str, 
    'offerType':str, 
    'price':str, 
    'abtest':str,
    'vehicleType':str, 
    'yearOfRegistration':'int64', 
    'gearbox':str, 
    'powerPS':'int64', 
    'model':str, 
    'odometer':str, 
    'monthOfRegistration':'int64', 
    'fuelType':str, 
    'brand':str,
    'notRepairedDamage':str,
    'dateCreated':str,
    'nrOfPictures':'int64',
    'postalCode':'int64',
    'lastSeen':str
}

COLUMN_CHANGE = {
    "dateCreated": "ad_created",
    "dateCrawled": "date_crawled",
    "fuelType": "fuel_type",
    "lastSeen": "last_seen",
    "monthOfRegistration": "registration_month",
    "notRepairedDamage": "unrepaired_damage",
    "nrOfPictures": "num_of_pictures",
    "offerType": "offer_type",
    "postalCode": "postal_code",
    "powerPS": "power_ps",
    "vehicleType": "vehicle_type",
    "yearOfRegistration": "registration_year"
}