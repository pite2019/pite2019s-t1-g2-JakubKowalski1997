class Car:
    def __init__(self):
        self.wheel_angle = 0
        self.speed = 0
        self.time = 0
        self.is_break = False
        self.actions = {'run': self.run, 'turn right': self.turn_right, 'turn left': self.turn_left, 'obstacle': self.pass_by_obstacle}

    def __add__(value_first, value_second):
        print ("Adding: ")
        return value_first + value_second

    def act(self,event, time):
        print('Before action: speed: {}, wheel_angle: {}'.format(self.speed, self.wheel_angle))
        if event == 'break':
            self.is_break = True
            print('Car brake')
        elif self.actions.get(event) == None:
            raise Exception("Unknown operation")
        else:
            self.actions[event]()
        print('After action: speed: {}, wheel_angle: {}'.format(self.speed, self.wheel_angle))
        print('Time: ', self.time)


    def turn_right(self):
        self.wheel_angle = self.wheel_angle + 90
        self.speed = self.speed - 10
    
    def turn_left(self):
        self.wheel_angle = self.wheel_angle - 90
        self.speed = self.speed - 10

    def run(self):
        self.speed = 90

    def pass_by_obstacle(self):
        self.turn_right
        self.turn_left
