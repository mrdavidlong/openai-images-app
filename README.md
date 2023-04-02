# Image generation with OpenAI API

Using OpenAI API to generate images from a description. It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

<img width="507" alt="van_gogh_painting_starry_night" src="https://user-images.githubusercontent.com/7539968/229337939-b2b5714f-29ae-42aa-a58e-be9b2764ef38.png">

<img width="571" alt="snoopy_in_rocket_in_space" src="https://user-images.githubusercontent.com/7539968/229338341-6413b5e6-8308-48e2-99b1-a8d24a4df279.png">

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-images-app
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements and upgrade openai

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run -h localhost -p 5002
   ```

You should now be able to access the app at [http://localhost:5002](http://localhost:5002)
