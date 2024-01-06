class Core:
    def __init__(self, id, capacity, tasks=[]):
        self.id = id
        self.capacity = capacity
        self._tasks = tasks
        self._hc_tasks = set()

    def schedule(self):
        if len(self._tasks) == 0: 
            raise Exception('No tasks given')
        # TODO: implement EDF-VD
        
    def add_task(self, task):
        self._tasks.append(task)
        if task.criticality == 'high':
            self._hc_tasks.add(task.id)

    def can_add_task(self, task):
        if task.u > self.capacity:
            return False
        elif (task.criticality == 'high') and (task.id in self._hc_tasks):
            return False
        else:
            return True

    @property
    def remaining_capacity(self):
        return self.capacity - sum(t.u for t in self._tasks)
    
    def __str__(self):
        return f'Core(id={self.id},capacity={self.capacity})'