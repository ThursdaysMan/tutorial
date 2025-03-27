class TimeWindow:
    def __init__(self, start_time, end_time, delta):
        """
        Initialize the time window for the experiments.

        :param start_time: The starting time of the experiment.
        :param end_time: The final time of the experiment.
        :param delta: The time interval (must be positive).
        """
        if delta <= 0:
            raise ValueError(f"Error: Delta must be a positive number. Received delta={delta}")

        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta

        self.num_experiments = (end_time - start_time) // delta
        self.experiments = self.calculate_experiments()

    def calculate_experiments(self):
        """
        Calculate the start and stop times for the model and observation windows.
        """
        experiments = []
        for i in range(self.num_experiments):
            model_start = self.start_time + i * self.delta
            model_stop = model_start + self.delta

            # Observation window is +/- 30 minutes from model stop time
            window_start = model_stop - (30 * 60)
            window_stop = model_stop + (30 * 60)

            experiments.append({
                "model_start": model_start,
                "model_stop": model_stop,
                "window_start": window_start,
                "window_stop": window_stop
            })

        return experiments

    def display_experiments(self):
        """Prints the calculated experiment times."""
        for i, exp in enumerate(self.experiments):
            print(f"Experiment {i+1}:")
            print(f"  Model Start: {exp['model_start']}")
            print(f"  Model Stop: {exp['model_stop']}")
            print(f"  Window Start: {exp['window_start']}")
            print(f"  Window Stop: {exp['window_stop']}")
            print("-" * 40)


def main():
    try:
        # ✅ Use a positive delta value (1 hour = 3600 seconds)
        tw = TimeWindow(start_time=0, end_time=36000, delta=3600)  
        tw.display_experiments()
    
    except ValueError as e:
        print(f"❌ Error: {e}")  # Display the error message

if __name__ == "__main__":
    main()