def print_models(unprinted_designs, completed_models):
    try:
        while unprinted_designs:
            current_design = unprinted_designs.pop()
            # Імітація друку моделі на 3D-принтері.
            print("Printing model: " + current_design)
            completed_models.append(current_design)
    except Exception as e:
        print("Помилка друку моделей:", e)

def show_completed_models(completed_models):
    try:
        print("\nThe following models have been printed:")
        for completed_model in completed_models:
            print(completed_model)
    except Exception as e:
        print("Помилка виведення надрукованих моделей:", e)
