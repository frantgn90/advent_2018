#!/usr/bin/env python3

import datetime, re, numpy

class Log(object):
    def __init__(self,date, msg):
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
        self.msg = msg
    def __le__(self,other): return self.date <= other.date
    def __lt__(self,other): return self.date <  other.date
    def __ge__(self,other): return self.date >= other.date
    def __gt__(self,other): return self.date >  other.date
    def __ne__(self,other): return self.date != other.date
    def __eq__(self,other): return self.date == other.date

class Guard(object):
    def __init__(self, id):
        self.id = int(id)
        self.shift = numpy.array([0]*60)
        self.total_minutes = 0
        self.most_freq_minute = None
        self.highest_freq = 0
    def falls_asleep(self,minute):
        self.falls_asleep_min = minute
    def wakes_up(self,minute):
        self.shift[self.falls_asleep_min:minute] += 1
#       self.total_minutes += (minute - self.falls_asleep_min)
        self.most_freq_minute = self.shift.argmax()
        self.highest_freq = self.shift[self.most_freq_minute]
    def get_max_minute(self):
        return self.shift.argmax()
#   def __le__(self,other): return self.total_minutes <= other.total_minutes
#   def __lt__(self,other): return self.total_minutes <  other.total_minutes
#   def __ge__(self,other): return self.total_minutes >= other.total_minutes
#   def __gt__(self,other): return self.total_minutes >  other.total_minutes
#   def __ne__(self,other): return self.total_minutes != other.total_minutes
#   def __eq__(self,other): return self.total_minutes == other.total_minutes
    def __le__(self,other): return self.highest_freq <= other.highest_freq
    def __lt__(self,other): return self.highest_freq <  other.highest_freq
    def __ge__(self,other): return self.highest_freq >= other.highest_freq
    def __gt__(self,other): return self.highest_freq >  other.highest_freq
    def __ne__(self,other): return self.highest_freq != other.highest_freq
    def __eq__(self,other): return self.highest_freq == other.highest_freq

if __name__ == "__main__":
    with open("d4.in") as inp:
        logs = []
        for line in inp:
            m = re.search("^\[(.+)\] (.+)$", line)
            logs.append(Log(m.group(1), m.group(2)))
        logs.sort()

    guards = {}
    last_guard = None
    for l in logs:
        m = re.search("^Guard #(\d+) begins shift", l.msg)
        if not m is None:
            last_guard = m.group(1)
            if not last_guard in guards:
                guards.update({last_guard: Guard(last_guard)})
        elif l.msg == "falls asleep":
            guards[last_guard].falls_asleep(l.date.minute)
        elif l.msg == "wakes up":
            guards[last_guard].wakes_up(l.date.minute)
    guards = list(guards.values())
    guards.sort()

    print (guards[-1].most_freq_minute * guards[-1].id)

