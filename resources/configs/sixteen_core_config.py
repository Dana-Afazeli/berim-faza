config = {
    'n_cores': 16,
    'random_seed': 33,
    'task_mapping_strategy': 'WFD', # ['WFD', 'FFD']
    'task_mapping_result_path': 'resources/allocation_results/sixteen_core_mapping',
    'core_failure_prob': 0.3,
    'core_overrun_prob': 0.5,
    'per_core_utilization': 0.75,
    'total_task_count': 200,
    'fault_tolerance': 1e-7,
    'high_criticality_prob': 0.5,
    'period_sample_space': [10, 20, 40, 50, 100, 200, 400, 500, 1000]
}