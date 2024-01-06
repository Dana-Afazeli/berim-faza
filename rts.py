from core import Core
from task import Task
from uunifast import uunifast
import numpy as np

class RealTimeSystem:
    def __init__(self, config):
        self._config = config
        self._tasks = []
        self._cores = []

        self._init_cores()

    def _init_cores(self):
        for i in range(self._config['n_cores']):
            self._cores.append(Core(f'core_{i}', self._config['per_core_utilization']))

    def _get_mapping_strategy(self):
        strategy = self._config['task_mapping_strategy']
        if strategy == 'WFD':
            def wfd_picker(task, cores):
                for c in sorted(cores, key=lambda c: c.remaining_capacity, reverse=True):
                    if c.can_add_task(task):
                        return c
                else:
                    raise Exception(f'Task {task} cannot be scheduled on current cores')
                
            return wfd_picker
        elif strategy == 'FFD':
            def ffd_picker(task, cores):
                for c in cores:
                    if c.can_add_task(task):
                        return c
                else:
                    raise Exception(f'Task {task} cannot be scheduled on current cores')
            
            return ffd_picker
        else:
            raise Exception('Illegal task mapping strategy')
            
    def _create_tasks(self):
        rng = np.random.default_rng(self._config['random_seed'])
        task_criticalities = rng.choice(
            ['high', 'low'], 
            size=self._config['total_task_count'], 
            p=[self._config['high_criticality_prob'], 1 - self._config['high_criticality_prob']]
        )
        task_utilizations = uunifast(
            self._config['per_core_utilization'] * self._config['n_cores'],
            task_criticalities,
            rng,
            self._calculate_hc_redundancy()
        )
        task_periods = rng.choice(self._config['period_sample_space'], size=self._config['total_task_count'])
        task_mus = ((rng.random((self._config['total_task_count'],)) + 1.5)/5).tolist()
        

        for i in range(self._config['total_task_count']):
            self._tasks.append(Task(
                i,
                task_utilizations[i],
                task_periods[i],
                task_mus[i],
                task_criticalities[i]
            ))

    def _calculate_hc_redundancy(self):
        if self._config['core_failure_prob'] is None:
            return 1
        else:
            return int(np.ceil(
                np.log(self._config['fault_tolerance']) / np.log(self._config['core_failure_prob'])
            ))

    def _map_tasks_to_cores(self):
        hc_redundancy = self._calculate_hc_redundancy()
        sorted_tasks = sorted(self._tasks, key=lambda t: t.u, reverse=True)
        core_picker = self._get_mapping_strategy()
        rep = {'high':hc_redundancy, 'low':1}
        for t in sorted_tasks:
            for _ in range(rep[t.criticality]):
                core_picker(t, self._cores).add_task(t)

    def init_tasks(self):
        self._create_tasks()
        self._map_tasks_to_cores()

    def task_mapping_report(self):
        print('Mapping Results:')
        for c in self._cores:
            print(str(c) + ':')
            [print(t) for t in c._tasks]
            print(f'total core utilizaiton: {sum(t.u for t in c._tasks)}')
            print('-'*30)