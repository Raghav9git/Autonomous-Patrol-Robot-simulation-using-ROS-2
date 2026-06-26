import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped


class PatrolNode(Node):

    def __init__(self):
        super().__init__('patrol_node')

        self.action_client = ActionClient(
            self,
            NavigateToPose,
            'navigate_to_pose'
        )

        # Larger square for visible movement
        self.goals = [
            (1.5, 0.0),
            (1.5, 1.5),
            (0.0, 1.5),
            (0.0, 0.0)
        ]

        self.get_logger().info("Waiting for Nav2 action server...")
        self.action_client.wait_for_server()

        # Start infinite patrol loop
        self.start_patrol()


    def send_goal(self, x, y):

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = PoseStamped()

        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()

        goal_msg.pose.pose.position.x = float(x)
        goal_msg.pose.pose.position.y = float(y)
        goal_msg.pose.pose.position.z = 0.0

        goal_msg.pose.pose.orientation.x = 0.0
        goal_msg.pose.pose.orientation.y = 0.0
        goal_msg.pose.pose.orientation.z = 0.0
        goal_msg.pose.pose.orientation.w = 1.0

        self.get_logger().info(f"Sending goal: ({x}, {y})")

        send_goal_future = self.action_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected!")
            return

        self.get_logger().info("Goal accepted!")

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        self.get_logger().info("Goal reached!")


    def start_patrol(self):
        while rclpy.ok():   # ← INFINITE LOOP HERE
            for (x, y) in self.goals:
                self.send_goal(x, y)

            self.get_logger().info("Patrol cycle completed! Restarting...")


def main(args=None):
    rclpy.init(args=args)
    node = PatrolNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
