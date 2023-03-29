class Controller(CPU_Memory):
    email = Email()

    def trigger_cpu_alert(
        self, frequency, max_cpu_attempts: int = 10, cpu_attempts: int = 0
    ):
        if cpu_attempts == max_cpu_attempts:
            subject = self.email.init_subject(status="WARNING", type=0)
            content = self.email.init_content(
                max_attemps=max_cpu_attempts, frequency=frequency, type=0
            )
            self.email.send(subject, content)
            print(f"High CPU Usage {self.get_cpu_percent()}")
            print(f"[0] Sending warning CPU email!")
            Log.get_log(f"[0] Sending warning CPU email!")
        elif cpu_attempts == max_cpu_attempts * 3:
            subject = self.email.init_subject(status="CRITICAL", type=0)
            content = self.email.init_content(
                max_attemps=max_cpu_attempts * 3, frequency=frequency, type=0
            )
            self.email.send(subject, content)
            print(f"Critical CPU Usage {self.get_cpu_percent()}")
            print(f"[1] Sending critical CPU email!")
            Log.get_log(f"[1] Sending critical CPU email!")

    def trigger_memory_alert(
        self, frequency, max_memory_attempts: int = 10, memory_attempts: int = 0
    ):
        if memory_attempts == max_memory_attempts:
            subject = self.email.init_subject(status="WARNING", type=1)
            content = self.email.init_content(
                max_attemps=max_memory_attempts, frequency=frequency, type=1
            )
            self.email.send(subject, content)
            print(f"High Memory Usage {self.get_memory_percent()}")
            print(f"[0] Sending warning memory email!")
            Log.get_log(f"[0] Sending warning memory email!")
        elif memory_attempts == max_memory_attempts * 3:
            subject = self.email.init_subject(status="CRITICAL", type=1)
            content = self.email.init_content(
                max_attemps=max_memory_attempts * 3, frequency=frequency, type=1
            )
            self.email.send(subject, content)
            print(f"Critical Memory Usage {self.get_memory_percent()}")
            print(f"[1] Sending critical memory email!")
            Log.get_log(f"[1] Sending critical memory email!")


def main():
    monitor_service = CPU_Memory()
    controller = Controller()
    max_cpu_attempts = 10
    max_memory_attempts = 10
    cpu_attempts = 0
    memory_attempts = 0
    cpu_threshold: float = 30
    memory_threshold: float = 60
    frequency = 0.5
    hold_on = 10
    log_init = Log()
    log_init.set_up()
    while True:
        Log.get_log("Started the cpu-memory monitor serivce.")
        if monitor_service.alert_cpu(threshold=cpu_threshold):
            cpu_attempts += 1
            if cpu_attempts == (max_cpu_attempts - 1):
                time.sleep(hold_on)
            elif cpu_attempts == (max_cpu_attempts - 1) * 3:
                time.sleep(hold_on * 3)
        else:
            cpu_attempts = 0

        if monitor_service.alert_memory(threshold=memory_threshold):
            memory_attempts += 1
            if memory_attempts == (max_memory_attempts - 1):
                time.sleep(hold_on)
            elif memory_attempts == (max_memory_attempts - 1) * 3:
                time.sleep(hold_on * 3)
        else:
            memory_attempts = 0

        print(f"Memory usage: {monitor_service.get_memory_percent()}%")
        print(f"Count Memory Attempts: {memory_attempts}")
        print("-" * 20)
        print(f"CPU usage: {monitor_service.get_cpu_percent()}%")
        print(f"Count CPU Attempts: {cpu_attempts}")
        print("-" * 20)

        threading.Thread(
            target=controller.trigger_memory_alert,
            args=(frequency, max_memory_attempts, memory_attempts),
        ).start()
        threading.Thread(
            target=controller.trigger_cpu_alert,
            args=(frequency, max_cpu_attempts, cpu_attempts),
        ).start()
        time.sleep(frequency)


if __name__ == "__main__":
    main()
