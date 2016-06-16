#!/usr/bin/env python
# encoding: utf-8

class Passenger(object):
    def __init__(self, current_floor):
        self.current_floor = current_floor

class LiftAction(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs

class Lift(object):
    def __init__(self):
        self.busy = False
        self.current_floor = 1
        self.doors_open = False
        self.action_plan = []

    def select_floor(self, destination, *args, **kwargs):
        self.action_plan.append(LiftAction('close_door'))

        #return actions_performed

    def open_door(self, *args, **kwargs):
        self.doors_open = True

    def close_door(self, *args, **kwargs):
        self.doors_open = False

    def perform(self, action, *args, **kwargs):
        self.__getattribute__(action)(*args, **kwargs)

    def _perform_actions(self, action_list, *args, **kwargs):
        for action in action_list:
            self.perform(action, *args, **kwargs)

    def perform_next_action(self):
        action = self.action_plan.pop(0)
        action_result = self.perform(action.name, action.args, action.kwargs)
        return action_result


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

def test_lift_door_close():
    lift = Lift()
    lift.perform('close_door')

    assert not lift.doors_open

    lift.perform('open_door')
    assert lift.doors_open
    

def test_lift_door_close():
    lift = Lift()
    lift.select_floor(2)

    assert not lift.doors_open
