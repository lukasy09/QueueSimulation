class VirtualQueueAgent:

    # instance
    instance = None

    @staticmethod
    def get_instance():
        if VirtualQueueAgent.instance is None:
            VirtualQueueAgent.instance = VirtualQueueAgent()
            return VirtualQueueAgent.instance

        return VirtualQueueAgent.instance