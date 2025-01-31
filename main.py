from tkinter import *
from Assign_Prob_tk import AssignmentProblem
from Knapsack_prob_tk import KnapsackProblem
from Scheduling_Prob_tk import SchedulingProblem
from Vehicle_Rout_Prob_tk import VehicleRoutingProblem
from Facility_Loc_Prob_tk import FacilityLocationProblem

class OptimizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Optimization Problems")
        self.create_menu()

    def create_menu(self):
        Label(self.root, text="Select an Optimization Problem", font=("Arial", 14)).grid(row = 0, column = 0, pady=10)

        Button(self.root, text="Assignment Problem", command=self.open_assignment).grid(row = 1, column = 0, padx=20, pady=5)
        Button(self.root, text="Knapsack Problem", command=self.open_knapsack).grid(row = 2, column = 0, padx=20, pady=5)
        Button(self.root, text="Facility Location Problem", command=self.open_facility).grid(row = 3, column = 0, padx=20, pady=5)
        Button(self.root, text="Scheduling Problem", command=self.open_scheduling).grid(row = 4, column = 0, padx=20, pady=5)
        Button(self.root, text="Vehicle Routing Problem", command=self.open_vrp).grid(row = 5, column = 0, padx=20, pady=5)

    def open_assignment(self):
        new_window = Toplevel(self.root)
        new_window.title("Assignment Problem")
        AssignmentProblem(new_window)

    def open_knapsack(self):
        new_window = Toplevel(self.root)
        new_window.title("Knapsack Problem")
        KnapsackProblem(new_window)

    def open_facility(self):
        new_window = Toplevel(self.root)
        new_window.title("Facility Location Problem")
        FacilityLocationProblem(new_window)

    def open_scheduling(self):
        new_window = Toplevel(self.root)
        new_window.title("Scheduling Problem")
        SchedulingProblem(new_window)

    def open_vrp(self):
        new_window = Toplevel(self.root)
        new_window.title("Vehicle Routing Problem")
        VehicleRoutingProblem(new_window)


if __name__ == "__main__":
    root = Tk()
    app = OptimizationApp(root)
    root.mainloop()
