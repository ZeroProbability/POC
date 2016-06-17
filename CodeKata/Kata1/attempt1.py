#!/usr/bin/env python
# encoding: utf-8

class LiftAction(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs

class Lift(object):
    def __init__(self, lift_id):
        self.lift_id = lift_id
        self.current_floor = 1
        self.doors_open = False
        self.action_plan = []

    def str(self):
        return "{} is {}".format(self.lift_id, self.is_busy())

    def is_busy(self):
        return len(self.action_plan) > 0

    def goto_floor(self, destination, *args):
        self.current_floor = destination

        return "moved to floor {}".format(destination)

    def select_floor(self, destination):
        ''' Passenger selects a floor '''
        self.action_plan.append(LiftAction('close_door'))
        self.action_plan.append(LiftAction('goto_floor', destination))
        self.action_plan.append(LiftAction('open_door'))

    def open_door(self, *args, **kwargs):
        self.doors_open = True

        return 'doors open'

    def close_door(self, *args, **kwargs):
        self.doors_open = False

        return 'doors closed'

    def perform(self, action, *args, **kwargs):
        return self.__getattribute__(action)(*args, **kwargs)

    def perform_next_action(self):
        action = self.action_plan.pop(0)
        action_result = self.perform(action.name, *(action.args), **(action.kwargs))
        return action_result

class LiftScheduler(object):
    def __init__(self, number_of_lifts):
        self.requests = []
        self.lifts = [Lift(lift_id) for lift_id in xrange(1, number_of_lifts+1)]

    def create_floor_request(self, request_init_floor, going_up):
        free_lifts = [ lift for lift in self.lifts if not lift.is_busy() ]
        return_lift = self.lifts[0]
        if len(free_lifts) > 0:
            return_lift = free_lifts[0]

        return_lift.select_floor(request_init_floor)
        return return_lift

def main():
    lift_scheduler = LiftScheduler(3)

    lift = lift_scheduler.create_floor_request(2, False)

    while(lift.is_busy()):
        print lift.perform_next_action()

    lift.select_floor(10)

    while(lift.is_busy()):
        print lift.perform_next_action()


if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_lift_door_close():
    lift = Lift(1)
    lift.select_floor(2)

    assert 'doors closed' == lift.perform_next_action()
    assert 'moved to floor 2' == lift.perform_next_action()
    assert 'doors open' == lift.perform_next_action()

def test_schedule_new_passenger():
    lift_scheduler = LiftScheduler(2)

    lift = lift_scheduler.create_floor_request(3, False)
    assert lift.lift_id == 1

    lift = lift_scheduler.create_floor_request(3, False)
    assert lift.lift_id == 2

    lift = lift_scheduler.create_floor_request(3, False)
    assert lift.lift_id == 1
