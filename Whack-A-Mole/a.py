import tkinter as tk

class PatientData:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, age, gender, illness):
        if len(self.patients) >= 50:
            print("Error: Can't add more than 50 patients.")
            return
        self.patients.append({"name": name, "age": age, "gender": gender, "illness": illness})
        print("Patient added.")

    def view_patients(self):
        for patient in self.patients:
            print(patient)

class PatientDataApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Patient Data App")
        self.patient_data = PatientData()

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.grid(row=1, column=0)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=1, column=1)

        self.gender_label = tk.Label(self, text="Gender:")
        self.gender_label.grid(row=2, column=0)
        self.gender_entry = tk.Entry(self)
        self.gender_entry.grid(row=2, column=1)

        self.illness_label = tk.Label(self, text="Illness:")
        self.illness_label.grid(row=3, column=0)
        self.illness_entry = tk.Entry(self)
        self.illness_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self, text="Add Patient", command=self.add_patient)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(self, text="View Patients", command=self.view_patients)
        self.view_button.grid(row=5, column=0, columnspan=2)

    def add_patient(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        illness = self.illness_entry.get()
        self.patient_data.add_patient(name, age, gender, illness)

    def view_patients(self):
        self.patient_data.view_patients()

if __name__ == "__main__":
    app = PatientDataApp()
    app.mainloop()