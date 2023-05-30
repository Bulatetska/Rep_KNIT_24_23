from functions import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
try:
    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)
except Exception as e:
    print("Виникла помилка:", e)
