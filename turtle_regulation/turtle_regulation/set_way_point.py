import rclpy
import math
from rclpy.node import Node
from turtlesim.msg import Pose

class SetWayPointNode(Node):
    def __init__(self):
        super().__init__('set_way_point_node')

        # Attribut pour stocker la pose de la tortue
        self.current_pose = None
        self.waypoint = (7.0, 7.0)

        # Souscription au topic /turtle1/pose
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):
        # Mettre à jour la pose de la tortue
        self.current_pose = msg

        # Coordonnées actuelles de la tortue
        xa = msg.x
        ya = msg.y

        # Coordonnées du waypoint
        xb, yb = self.waypoint

        # Calcul de l'angle désiré (vers le waypoint)
        theta_desired = math.atan2(yb - ya, xb - xa)

        # Affichage
        self.get_logger().info(
            f"Pose : x={xa:.2f}, y={ya:.2f}, theta={msg.theta:.2f} | "
            f"θ_desired={theta_desired:.2f} rad | Waypoint: {self.waypoint}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = SetWayPointNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
