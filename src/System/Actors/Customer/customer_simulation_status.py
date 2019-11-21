class CustomerSimulationStatus:
        BEFORE = 1  # Before entering the system...
        IN = 2      # In a system, the customer is being monitored by the monitoring agent
        IN_VQ = 3   # In a virtual queue, awaiting for the right queue
        IN_QUEUE = 4  # In a queue
        AFTER = 5     # Deactivated agent, left system

