class Task:
    def __init__(self, id, u, T=None, mu=None, criticality=None):
        self.id = id
        self.u = u
        self.T = T
        self.mu = mu
        self.criticality = criticality
        self.executed_timesteps = None

        self.reset()

    @property
    def high_wcet(self):
        if self.criticality == 'low':
            raise Exception("Low criticality tasks don't have high wcet")
        elif self.T is None:
            raise Exception('Period is not set')
        else:
            return int(self.T * self.u)
        
    @property
    def low_wcet(self):
        if self.T is None:
            raise Exception('Period is not set')
        elif self.criticality is None:
            raise Exception('Criticality is not specified')
        elif self.criticality == 'low':
            return self.high_wcet
        elif self.mu is None:
            raise Exception('Mu is not set')
        else:
            return self.mu * self.high_wcet
        
    def reset(self):
        self.executed_timesteps = 0

    def execute_timestep(self):
        self.execute_timestep += 1

    def __str__(self):
        return f'Task(id={self.id},u={self.u},T={self.T},criticality={self.criticality})'

