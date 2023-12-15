# SPDX-FileCopyrightText: 2023 Sho Haneishi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Fibonacci():
    def __init__(self, node):
        self.pub = node.create_publisher(Int32, "fibonacci_sequence", 10)
        self.fib, self.a, self.b = 0, 0, 1
        self.n = 1
        node.create_timer(1.0, self.pub_fibo)

    def pub_fibo(self):
        msg = Int32()
        if self.n == 1:
            msg.data = 1
        else:
            self.fib = self.a + self.b
            msg.data = self.fib
            self.a = self.b
            self.b = self.fib
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("fibonacci")
    fibonacci = Fibonacci(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
