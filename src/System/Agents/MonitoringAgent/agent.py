from System.Agents.MonitoringAgent.monitoring_agent_status import MonitoringAgentStatus


class MonitoringAgent:

    # Status
    status = MonitoringAgent.NEW

    monitored_customer = None  # Every monitoring agent has his own unit to monitor


    def set_monitored(self, customer):
        self.monitored_customer = customer
        self.status = MonitoringAgent.ACTIVE


    def monitor_customer(self):
        if self.status == MonitoringAgent.ACTIVE:
            pass