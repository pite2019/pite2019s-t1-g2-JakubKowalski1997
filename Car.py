class Car:
    def __init__(self):
        self.wheel_angle = 0
        self.speed = 0
        self.time = 0

    def act(self,event, time):
        print('Before action: speed: {}, wheel_angle: {}'.format(self.speed, self.wheel_angle))
        if event == 'run':
            self.speed = 90
        elif event == 'turn right':
            self.wheel_angle = self.wheel_angle + 90
            self.speed 
        elif event == 'turn left':
            self.wheel_angle = self.wheel_angle - 90
        else:
            raise Exception("Unknown operation")
        print('After action: speed: {}, wheel_angle: {}'.format(self.speed, self.wheel_angle))


