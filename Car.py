class Car:
    def __init__(self):
        self.wheel_angle = 0
        self.speed = 0
        self.time = 0
        self.is_break = False

    def __add__(value_first, value_second):
        print ("Adding: ")
        return value_first + value_second

    def act(self,event, time):
        print('Before action: speed: {}, wheel_angle: {}'.format(self.speed, self.wheel_angle))
        if event == 'run':
            self.speed = 90
        elif event == 'turn right':
            self.turn_right
        elif event == 'turn left':
            self.turn_left
        elif event == 'break':
            self.is_break = True
            print('Car brake')
        elif event == 'obstacle':
            self.turn_right
            self.turn_left
        else:
            raise Exception("Unknown operation")
        self.time += time
        print('After action: speed: {}, wheel_angle: {}'.format(self.speed, self.wheel_angle))
        print('Time: ', self.time)

    def turn_right(self):
        self.wheel_angle = self.wheel_angle + 90
        self.speed = self.speed - 10
    
    def turn_left(self):
        self.wheel_angle = self.wheel_angle - 90
        self.speed = self.speed - 10

