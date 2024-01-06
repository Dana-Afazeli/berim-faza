config = {
    'n_cores': 8,
    'random_seed': 42,
    'task_mapping_strategy': 'WFD', # ['WFD', 'FFD']
    'task_mapping_result_path': 'resources/allocation_results/eigh_core_allocation',
    'core_failure_prob': None,
    'core_overrun_prob': None,
    'per_core_utilization': 0.5,
    'total_task_count': 50,
    'fault_tolerance': 1e-5,
    'high_criticality_prob': 0.5,
    'period_sample_space': [10, 20, 40, 50, 100, 200, 400, 500, 1000]
}