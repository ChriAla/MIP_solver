from tkinter import *
from tkinter import messagebox
import pyomo.environ as pe
import pyomo.opt as po

class KnapsackProblem:
    def __init__(self, root):
        self.root = root
        self.create_gui()

    def create_gui(self):
        # Ετικέτες και πεδία εισόδου
        Label(self.root, text="Knapsack Capacity:").grid(row=0, column=0, sticky="w")
        self.entry_capacity = Entry(self.root)
        self.entry_capacity.grid(row=0, column=1)

        Label(self.root, text="Values (space-separated):").grid(row=1, column=0, sticky="nw")
        self.text_values = Text(self.root, height=5, width=40)
        self.text_values.grid(row=1, column=1)

        Label(self.root, text="Weights (space-separated):").grid(row=2, column=0, sticky="nw")
        self.text_weights = Text(self.root, height=5, width=40)
        self.text_weights.grid(row=2, column=1)

        # Κουμπί επίλυσης
        solve_button = Button(self.root, text="Solve the problem", command=self.solve_knapsack)
        solve_button.grid(row=3, column=0, columnspan=2)

    def solve_knapsack(self):
        try:
            # Ανάγνωση δεδομένων από το GUI
            capacity = float(self.entry_capacity.get())
            values_input = self.text_values.get("1.0", END).strip()
            weights_input = self.text_weights.get("1.0", END).strip()

            # Μετατροπή αξιών και βαρών από είσοδο σε λίστες
            values = list(map(float, values_input.split()))
            weights = list(map(float, weights_input.split()))

            # Έλεγχος αν ο αριθμός των αντικειμένων είναι ίδιος
            if len(values) != len(weights):
                raise ValueError("The number of values and weights must be the same.")
            
            num_items = len(values)

            # Δημιουργία μοντέλου Pyomo
            model = pe.ConcreteModel()

            # Σετ αντικειμένων
            model.items = pe.Set(initialize=range(num_items))

            # Μεταβλητές απόφασης (binary): Αν το αντικείμενο i μπει στο σακίδιο
            model.x = pe.Var(model.items, domain=pe.Binary)

            # Συνάρτηση στόχου: Μέγιστη συνολική αξία
            def objective_rule(model):
                return sum(model.x[i] * values[i] for i in model.items)
            
            model.obj = pe.Objective(rule=objective_rule, sense=pe.maximize)

            # Περιορισμός: Το συνολικό βάρος να μην υπερβαίνει τη χωρητικότητα
            def weight_constraint_rule(model):
                return sum(model.x[i] * weights[i] for i in model.items) <= capacity
            
            model.weight_constraint = pe.Constraint(rule=weight_constraint_rule)

            # Επίλυση
            solver = po.SolverFactory('glpk')
            result = solver.solve(model, tee=True)

            # Ανάγνωση αποτελεσμάτων
            selected_items = []
            total_value = pe.value(model.obj)
            for i in model.items:
                if pe.value(model.x[i]) == 1:
                    selected_items.append(f"Item {i+1} (Value: {values[i]}, Weight: {weights[i]})")

            # Εμφάνιση αποτελεσμάτων
            result_text = f"Total Value: {total_value}\nSelected Items:\n" + "\n".join(selected_items)
            messagebox.showinfo("Results", result_text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
