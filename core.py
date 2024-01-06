class Core:
    def __init__(self, id, utilization):
        self.id = id
        self.utilization = utilization
        self._tasks = []
        self._hc_tasks = set()

    def schedule(self):
        if len(self._tasks) == 0: 
            raise Exception('No tasks given')
        # TODO: implement EDF-VD
        
    def add_task(self, task):
        self._tasks.append(task)
        if task.criticality == 'high':
            self._hc_tasks.add(task.id)

    def can_add_task(self, task, care_for_utilization=True):
        if self.remaining_utilization < task.u:
            return False
        elif care_for_utilization and ((1 - self.remaining_utilization) > self.utilization):
            return False
        elif (task.criticality == 'high') and (task.id in self._hc_tasks):
            return False
        else:
            return True

    @property
    def remaining_utilization(self):
        return 1 - sum(t.u for t in self._tasks)
    
    def __str__(self):
        return f'Core(id={self.id},utilization={self.utilization})'