from experta import *
import tkinter as tk
from tkinter import ttk

# Déclaration des faits
class Sexe(Fact):
    pass

class Age(Fact):
    pass

class Taille(Fact):
    pass

class Poids(Fact):
    pass

class Cholesterol(Fact):
    pass

class Sugar(Fact):
    pass

class Temperature(Fact):
    pass

class Activity(Fact):
    pass

class Regime(Fact):
    pass

# Définition des règles
class NutritionEngine(KnowledgeEngine):    

    @Rule(Sexe(value=MATCH.sex),Age(int_value=MATCH.age),Taille(int_value=MATCH.taille),Poids(int_value=MATCH.poids),Activity(MATCH.activity))
    def rule_calculate_caloric_needs(self, sex, age, taille, poids, activity):
        if sex == "Female":
            m = 66.5 + (13.75 * int(poids)) + (5 * int(taille)) - (6.75 * int(age))
        elif sex == "Male":
            m = 655.1 + (9.563 * int(poids)) + (1.850 * int(taille)) - (4.676 * int(age))

        if activity == "Faible":
            w = m * 1.375
        elif activity == "Modéré":
            w = m * 1.55
        elif activity == "Intense":
            w = m * 1.725
        with open("results.txt", "a") as file:
            file.write(f"\n\n *** Vos besoins caloriques sont de {round(w, 2)} calories par jour. ***\n")

    @Rule(Cholesterol("Élevé"))
    def rule_recommandation_alimentaire_cholesterol(self):
        with open("results.txt", "a") as file:
            file.write(" \n *** Recommendation pour un taux de cholestérol élevé *** \n")
            file.write(" Les Aliments à éviter : \n -1- Les aliments riches en graisses saturées, tels que la viande rouge, la volaille avec la peau, les produits laitiers entiers et les aliments transformés, \n -2- Les aliments riches en graisses trans, tels que les aliments frits, les produits de boulangerie et les snacks, \n -3- Les aliments riches en sucres ajoutés, tels que les boissons sucrées, les bonbons, les biscuits et les gâteaux.")
            file.write(" Les Aliments à recommender : \n -1- Les aliments riches en fibres, tels que les fruits, les légumes, les céréales complètes et les légumineuses, \n -2- Les aliments riches en oméga-3, tels que les poissons gras, les noix et les graines, \n -3- Les aliments riches en phytostérols, tels que les huiles végétales, les fruits et légumes.\n")

    @Rule(Sugar("Instable"))
    def rule_recommandation_alimentaire_sugar(self):
        with open("results.txt", "a") as file:
            file.write(" \n *** Recommendation pour un indice de glycémie instable *** \n ")
            file.write(" Les Aliments à éviter : \n -1- Les aliments à base de farine blanche (les pâtes blanches, le riz blanc et les céréales de petit-déjeuner sucrées), \n -2- Les aliments sucrés (les bonbons, les gâteaux, les glaces et les boissons sucrées), \n -3- Les aliments transformés (les pizzas, les hamburgers, les frites et les snacks).")
            file.write(" Les Aliments à recommander : \n -1- Les aliments à base de farine complète (le pain complet, les pâtes complètes, le riz complet et les céréales), \n -2- Les fruits et légumes qui sont riches en fibres, en vitamines et en minéraux, \n -3- Les produits laitiers faibles en gras ou sans gras qui sont riches en protéines et calcium, \n -4- Les légumineuses qui fournissent du fibres et des glucides complexes.\n")

    @Rule(Temperature("Élevée"), Activity("Intense"))
    def rule_recommandation_hydratation(self):
        with open("results.txt", "a") as file:
            file.write("\n *** Recommandation pour l'hydratation *** \n ")
            file.write(" -1- Buvez un verre d'eau avant, pendant et après les repas. \n -2- Ajoutez des fruits ou des légumes à vos boissons.  \n -3-  Mangez des aliments riches en eau, tels que les fruits, les légumes et les soupes. \n -4- Limitez votre consommation de caféine et d'alcool, car ils peuvent entraîner une déshydratation.")

    @Rule(Regime(value=MATCH.v))
    def rule_recommandation_supplements(self, v):
        with open("results.txt", "a") as file:
            if v == "Vitamine A":
                file.write(" \n *** Les aliments riches en vitamine A *** \n")
                file.write(" -1- Les légumes à feuilles vertes, tels que les épinards, les blettes et le chou frisé. \n -2- Les carottes, les patates douces et les autres légumes orange ou jaunes. \n -3- Les fruits rouges et jaunes, tels que les abricots, les mangues et les poivrons rouges, \n -4- Le foie, le lait entier et les produits laitiers entiers. \n")
            elif v == "Vitamine C":
                file.write(" \n *** Les aliments riches en vitamine C *** \n")
                file.write(" -1- Les fruits frais, tels que les oranges, les citrons, les kiwis et les fraises. \n -2- Les légumes frais, tels que les poivrons, le brocoli et les choux de Bruxelles. \n -3- Les pommes de terre, les brocolis et les choux de Bruxelles cuits.\n")
            elif v == "Vitamine B12":
                file.write(" \n *** Les aliments riches en vitamine B12 *** \n")
                file.write(" Les produits d'origine animale, tels que la viande, les fruits de mer, les œufs et les produits laitiers.\n")
            elif v == "Fer":
                file.write(" \n *** Les aliments riches en Fer *** \n")
                file.write (" -1- La viande rouge, la volaille et le poisson. \n -2- Les légumes à feuilles vertes, tels que les épinards et les blettes. \n -3- Les légumineuses, telles que les lentilles, les haricots et les pois. \n -4- Les fruits secs, tels que les figues, les dattes et les raisins secs.\n")


# Declaration des attributs
Nom, sex, age, taille, poids, cholesterol, sugar, temperature, activity, regime = None, None, None, None, None, None, None, None, None, None


def execution():
    with open("results.txt", "a") as file:   
        file.write("**** Bienvenue dans le système expert de conseil en nutrition personnalisée! **** \n\n ")

    global Nom
    global sex
    global age
    global cholesterol
    global sugar
    global temperature
    global activity
    global regime
    global taille
    global poids


    engine = NutritionEngine()
    engine.reset()

    engine.declare(Sexe(value=sex))
    engine.declare(Age(int_value=age))
    engine.declare(Taille(int_value=taille))
    engine.declare(Poids(int_value=poids))
    engine.declare(Cholesterol(cholesterol))
    engine.declare(Sugar(sugar))
    engine.declare(Temperature(temperature))
    engine.declare(Activity(activity))
    engine.declare(Regime(value=regime))

    # Exécution du moteur d'inférence
    engine.run()



def start_GUI():

    def submit():
         
        global Nom
        global sex
        global age
        global cholesterol
        global sugar
        global temperature
        global activity
        global regime
        global taille
        global poids

        Nom = entry_name.get()
        sex = sex_combo.get()
        age = entry_age.get()
        cholesterol = chol_combo.get()
        sugar = sugar_combo.get()
        temperature = temp_combo.get()
        activity = activity_combo.get()
        regime = vitamins_combo.get()
        taille = entry_taille.get()
        poids = entry_poids.get()

        # Create a label inside the frame
        label_tkinter = tk.Label(
            window,
            text="**** Que ton aliment soit ta seule médecine ****:",
            bg='#d5e6e6',
            fg="#374151",
            font=("Arial", 12, "bold")
        )
        label_tkinter.grid(row=12, column=0, sticky="nsew", padx=(0, 5))

        return True


    # Create the main window
    window = tk.Tk()
    window.title("Système expert de conseil en nutrition personnalisée")


    # Create a gradient background
    window.configure(bg='#d5e6e6')

    label_title = tk.Label(
        window,
        text="Bienvenue dans le système expert de conseil en nutrition personnalisée",
        font=("Arial", 24, "bold"),
        bg='#d5e6e6',
        fg="#cd8282"
    )
    label_title.grid(row=0, column=1, padx=10, pady=10)

    # Create a frame to hold the label and entry
    name_frame = tk.Frame(window)
    name_frame.grid(row=1, column=0, padx=30, pady=10)

    # Create a label inside the frame
    label_name = tk.Label(
        name_frame,
        text="Nom:",
        bg='#d5e6e6',
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_name.grid(row=1, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the name_frame
    entry_name = tk.Entry(name_frame, font=("Arial", 12))
    entry_name.grid(row=1, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    sex_frame = tk.Frame(window)
    sex_frame.grid(row=2, column=0, padx=30, pady=10)

    # Create a label inside the frame
    label_sex = tk.Label(
        sex_frame,
        text="Sex:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_sex.grid(row=2, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the sex_frame
    sex_values = ["Male", "Female"]
    sex_combo = ttk.Combobox(window, values=sex_values, font=("Arial", 12))
    sex_combo.grid(row=2, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    taille_frame = tk.Frame(window)
    taille_frame.grid(row=3, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_taille = tk.Label(
        taille_frame,
        text="Taille:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_taille.grid(row=3, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the taille_frame
    entry_taille = tk.Entry(window, font=("Arial", 12))
    entry_taille.insert(0, "Taille en cm.")
    entry_taille.configure(fg='gray')
    entry_taille.grid(row=3, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    age_frame = tk.Frame(window)
    age_frame.grid(row=4, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_age = tk.Label(
        age_frame,
        text="Age:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_age.grid(row=4, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the age_frame
    entry_age = tk.Entry(window, font=("Arial", 12))
    entry_age.grid(row=4, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    poids_frame = tk.Frame(window)
    poids_frame.grid(row=5, column=0, padx=10, pady=10)

    # Create a label inside theframe
    label_poids = tk.Label(
        poids_frame,
        text="Poids:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_poids.grid(row=5, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the poids_frame
    entry_poids = tk.Entry(window, font=("Arial", 12))
    entry_poids.insert(0, "Poids en kg.")
    entry_poids.configure(fg='gray')
    entry_poids.grid(row=5, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    chol_frame = tk.Frame(window)
    chol_frame.grid(row=6, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_chol = tk.Label(
        chol_frame,
        text="Taux de cholestérol:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_chol.grid(row=6, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the chol_frame
    chol_values = ["Normale", "Élevé"]
    chol_combo = ttk.Combobox(window, values=chol_values, font=("Arial", 12))
    chol_combo.grid(row=6, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    sugar_frame = tk.Frame(window)
    sugar_frame.grid(row=7, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_sugar = tk.Label(
        sugar_frame,
        text="Taux de sucre dans le sang:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_sugar.grid(row=7, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the sugar_frame
    sugar_values = ["Stable", "Instable"]
    sugar_combo = ttk.Combobox(window, values=sugar_values, font=("Arial", 12))
    sugar_combo.grid(row=7, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    temp_frame = tk.Frame(window)
    temp_frame.grid(row=8, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_temp = tk.Label(
        temp_frame,
        text="Température ambiante:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_temp.grid(row=8, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the temp_frame
    temp_values = ["Normale", "Élevée"]
    temp_combo = ttk.Combobox(window, values=temp_values, font=("Arial", 12))
    temp_combo.grid(row=8, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    activity_frame = tk.Frame(window)
    activity_frame.grid(row=9, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_activity = tk.Label(
        activity_frame,
        text="Niveau d'activité:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_activity.grid(row=9, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the activity_frame
    activity_values = ["Faible", "Modéré", "Intense"]
    activity_combo = ttk.Combobox(window, values=activity_values, font=("Arial", 12))
    activity_combo.grid(row=9, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    vitamins_frame = tk.Frame(window)
    vitamins_frame.grid(row=10, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_vitamins = tk.Label(
        vitamins_frame,
        text="Vitamines manquantes:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_vitamins.grid(row=10, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the vitamins_frame
    vitamins_values = ["Vitamine A", "Vitamine C", "Vitamine B12", "Fer", "Aucun"]
    vitamins_combo = ttk.Combobox(window, values=vitamins_values, font=("Arial", 12))
    vitamins_combo.grid(row=10, column=1, sticky="nsew")

    # Create a button to submit the form
    submit_button = tk.Button(
        window,
        text="Envoyer",
        fg="#cd8282",
        font=("Arial", 12, "bold"),
        command=submit
    )
    submit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

    # Set the window size and center it on the screen
    window_width = 1600
    window_height = 1600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Start the main event loop
    window.after(25000, execution)
    window.mainloop()


start_GUI()









