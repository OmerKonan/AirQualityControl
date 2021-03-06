import pymongo
from pymongo import MongoClient


class Database:
    """
    The class to send sensor data  to database
    """
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://yhsaylam:123@cluster0-o17jr.mongodb.net/AirControl?retryWrites=true&w=majority")  #Database address
        self.db = self.cluster["AirControl"]
        self.collection = self.db["AirControl"]
        self.TimeStr = ""
        self.COStr = ""
        self.CO2Str = ""
        self.SmokeStr = ""
        self.LPGStr = ""
        self.TempStr = ""
        self.HumStr = ""
        self.FailureStr = ""

    def prepare_data(self, SensorValArr):
        
        """
        Databese message should be string. The method setting data as a string with a asidöasidasdkasidkasidk BURAYI TEKRAR KONTROL ET
        """
        self.TimeStr = SensorValArr[0]
        self.COStr = str(SensorValArr[3]) + " ppm"
        self.CO2Str = str(SensorValArr[4]) + " ppm"
        self.SmokeStr = str(SensorValArr[2]) + " ppm"
        self.LPGStr = str(SensorValArr[1]) + " ppm"
        self.TempStr = str(SensorValArr[5]) + " °C"
        self.HumStr = "%" + str(SensorValArr[6]) 
        self.FailureStr = str(SensorValArr[7])

    def send_data(self):

        """
        Sending data as a JSON file with post variable.
        """

        post = {"_id":self.TimeStr, "LPG" : self.LPGStr, "Smoke": self.SmokeStr,"CO": self.COStr, "CO2" : self.CO2Str, "Temperature": self.TempStr, "Humidity": self.HumStr, "Failure": self.FailureStr}

        self.collection.insert_one(post)



