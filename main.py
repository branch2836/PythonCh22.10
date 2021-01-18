from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['DEBUG'] = True

images = ['grid_0.png', 'grid_1.png', 'grid_2.png', 'grid_3.png', 'grid_4.png',
    'grid_5.png', 'grid_6.png', 'grid_7.png', 'grid_8.png']

def fill_choices(index):
    options = {}
    if index in [1, 2, 4, 5, 7, 8]:
        options['Left'] = index-1
    elif index == 3:
        options['Left'] = 5
    if index in [0, 1, 3, 4, 6, 7]:
        options['Right'] = index+1
    elif index == 5:
        options['Right'] = 3
    if index in [1, 3, 4, 5, 6, 7, 8]:
        options['Up'] = (index-3)%9
    if index in [0, 1, 2, 3, 4, 5, 7]:
        options['Down'] = (index+3)%9
    return options

@app.route('/', methods=['GET', 'POST'])
def show_grid():
    if request.method == 'POST':
        # Collect the user's direction choice from the form.
        choice = int(request.form['choice'])
        # Add the number of the new box to the 'steps' string.
        steps = f"{request.form['steps']}-{choice}"
        # Assign the new image title.
        image = images[choice]
        # Determine which direction choices belong with the new box.
        choices = fill_choices(choice)
    else:
        # Randomly select a starting grid image.
        image = random.choice(images)
        # Determine which direction choices belong with the highlighted box.
        choices = fill_choices(images.index(image))
        # Assign the number of the highlighted box to the 'steps' string.
        steps = str(images.index(image))

    tab_title = "Flask Exercises"
    page_title = "Move Around A Grid"
    return render_template('grid.html', tab_title=tab_title, page_title=page_title,
        choices=choices, image=image, steps=steps)

if __name__ == '__main__':
    app.run()