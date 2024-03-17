import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from math import sin, pi



class My_Publisher(Node):
    def __init__(self):
        super().__init__('signal_generator')
        self.publisher_signal = self.create_publisher(Float32, '/signal', 10)
        self.publisher_time = self.create_publisher(Float32, 'time', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('Signal Generator node successfully initialized!!!')
        self.time = 0.0

    def timer_callback(self):
        signal_msg = Float32()
        time_msg = Float32()
        amplitude = 1.0
        frequency = 1.0

        signal_value = self.generate_sine_wave()
        signal_msg.data = signal_value
        
        time_msg.data = self.time

        self.publisher_signal.publish(signal_msg)
        self.publisher_time.publish(time_msg)

        self.get_logger().info(f'Time: {time_msg.data}, Signal: {signal_msg.data}')
        self.time += 0.1  # Increment time by 0.1 seconds (10 Hz)

    def generate_sine_wave(self):
        amplitude = 1.0
        frequency = 1.0
        return amplitude * sin(2 * pi * frequency * self.time)



def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()