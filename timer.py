import time


class Timer:
    def __init__(self, days=0, hours=0, minutes=0, seconds=0):
        self.timer = {"days": days, "hours": hours,
                      "minutes": minutes, "seconds": seconds}
        self.isStopped = False
        self.isDone = False

    def getDays(self):
        return self.timer["days"]

    def setDays(self, num):
        self.timer["days"] = num

    def getHours(self):
        return self.timer["hours"]

    def setHours(self, num):
        self.timer["hours"] = num

    def getMinutes(self):
        return self.timer["minutes"]

    def setMinutes(self, num):
        self.timer["minutes"] = num

    def getSeconds(self):
        return self.timer["seconds"]

    def setSeconds(self, num):
        self.timer["seconds"] = num

    def resetTime(self, string):
        if string == "days":
            self.setHours(23)
            self.setMinutes(59)
            self.setSeconds(59)
        elif string == "hours":
            self.setMinutes(59)
            self.setSeconds(59)
        else:
            self.setSeconds(59)

    def main(self):
        if self.getSeconds() == 0:
            if self.getMinutes() == 0:
                if self.getHours() == 0:
                    if self.getDays() == 0:
                        self.isDone = True
                    else:
                        self.resetTime("days")
                        self.setDays(self.getDays()-1)
                        time.sleep(1)
                else:
                    self.resetTime("hours")
                    self.setHours(self.getHours()-1)
                    time.sleep(1)
            else:
                self.resetTime("minutes")
                self.setMinutes(self.getMinutes()-1)
                time.sleep(1)
        else:
            self.setSeconds(self.getSeconds()-1)
            time.sleep(1)
