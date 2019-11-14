from System.Agents.MonitoringAgent.monitoring_agent_status import MonitoringAgentStatus
from System.Agents.ManagingAgent.customer_monitoring_status import CustomerMonitoringStatus
from Utils.GeneratorUtil import GeneratorUtil


class MonitoringAgent:

    # Status
    status = None
    monitoring_success_rate = None

    customer = None  # Every monitoring agent has his own unit to monitor

    # IoT, cooperating devices
    thermal_camera = None
    camera = None

    def __init__(self, rate):
        self.status = MonitoringAgentStatus.NEW
        self.monitoring_success_rate = rate

    def set_monitored(self, customer):
        self.customer = customer
        self.status = MonitoringAgentStatus.ACTIVE


    def monitor_customer(self):
        if self.status == MonitoringAgentStatus.ACTIVE:
            if GeneratorUtil.generate_uniform_random() <= self.monitoring_success_rate:
                self.customer.set_monitoring_status(CustomerMonitoringStatus.AFTER_MONITORING)