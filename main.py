from resources.configs.sixteen_core_config import config
from rts import RealTimeSystem

def main():
    rts = RealTimeSystem(config)
    rts.init_tasks()
    rts.task_mapping_report()

if __name__ == "__main__":
    main()