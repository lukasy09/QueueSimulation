from System.Agents.MonitoringAgent.monitoring_agent_status import MonitoringAgentStatus
from System.Agents.ManagingAgent.customer_monitoring_status import CustomerMonitoringStatus
from System.Actors.IoT.camera import Camera
from System.Actors.IoT.thermal_camera import ThermalCamera
from Utils.GeneratorUtil import GeneratorUtil


class MonitoringAgent:

    # Status
    status = None
    monitoring_success_rate = None

    customer = None  # Every monitoring agent has his own unit to monitor

    # IoT, cooperating devices
    thermal_camera = ThermalCamera.get_instance()
    camera = Camera.get_instance()


    # Customer generating config
    age_distribution = (35.6, 25)
    sex_options = ["M", "F"]
    disable_probability = 0.15
    pregnant_probability = 0.1  # On the condition if the customer is "F"

    # Customer features config
    elderly_threshold = 65


    def __init__(self, rate):
        self.status = MonitoringAgentStatus.NEW
        self.monitoring_success_rate = rate

    def set_monitored(self, customer):
        self.customer = customer
        self.status = MonitoringAgentStatus.ACTIVE


    def monitor_customer(self):
        if self.status == MonitoringAgentStatus.ACTIVE:
            if GeneratorUtil.generate_uniform_random() <= self.monitoring_success_rate:
                grabbed_data = self.camera.record()

                if grabbed_data['age'] > self.elderly_threshold:
                    self.customer.elderly = True

                if grabbed_data['sex'] < 0.5:
                    self.customer.sex = self.sex_options[0]
                else:
                    self.customer.sex = self.sex_options[1]

                if grabbed_data['disable'] <= self.disable_probability:
                    self.customer.disable = True

                if grabbed_data['pregnant'] <= self.pregnant_probability and self.customer.sex == self.sex_options[1]:
                    self.customer.pregnant = True

                self.customer.set_monitoring_status(CustomerMonitoringStatus.AFTER_MONITORING)