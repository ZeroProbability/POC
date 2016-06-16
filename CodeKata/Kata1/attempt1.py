#!/usr/bin/env python
# encoding: utf-8

class Passenger(object):
    def __init__(self, current_floor):
        self.current_floor = current_floor

class Lift(object):
    def __init__(self):
        self.busy = False
        self.current_floor = 1
        self.doors_open = False

    def goto(self, request_init_floor):
        self.busy = True

        self.close_door()
        self.current_floor = request_init_floor
        self.doors_open = True

    def close_door(self):
        print 'door is closing'

class LiftScheduler(object):
    def __init__(self, number_of_lifts):
        self.requests = []
        self.lifts = [Lift() for _ in xrange(number_of_lifts)]

    def create_floor_request(self, request_init_floor, going_up):
        first_free_lift = self.lifts[0]
        first_free_lift.goto(request_init_floor)
        return first_free_lift

def main():
    print "Hello there"

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_passenger_calls_lift():
    passenger = Passenger(1)
    lift_scheduler = LiftScheduler(1)

    lift = lift_scheduler.create_floor_request(passenger.current_floor, True)
    
    assert lift.current_floor == 1
    assert lift.doors_open == True
    assert lift.busy == True

def test_passenger_select_destination():
    passenger = Passenger(1)
    lift_scheduler = LiftScheduler(1)

    lift = lift_scheduler.create_floor_request(passenger.current_floor, True)
    lift.goto(2)

    assert lift.current_floor == 2
    assert lift.doors_open == True
    

