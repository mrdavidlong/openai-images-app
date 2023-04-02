# Image generation with OpenAI API

Using OpenAI API to generate images from a description. It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Example 1
<img width="530" alt="van_gogh_is_painting_starry_night" src="https://user-images.githubusercontent.com/7539968/229382563-607d4898-d5e3-4079-a5d5-aab2de46bf05.png">

Description: "Van Gogh is painting starry night"

## Example 2

<img width="530" alt="snoopy_in_a_rocket_in_space" src="https://user-images.githubusercontent.com/7539968/229380198-73201e89-c014-426c-9403-45e21698b7a2.png">

Description: "Snoopy in a rocket in space"

# Setup

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

8. Run the app on localhost port 5002 (feel free to change it to another port number)

   ```bash
   $ flask run -h localhost -p 5002
   ```

You should now be able to access the app at [http://localhost:5002](http://localhost:5002)

## Optional
In the future, if you want to upgrade your openai version, run this:
   ```bash
   $ pip install --upgrade openai
   ```

And if you want to update your requirements.txt file, run this:
   ```bash
   $ pip freeze > requirements.txt   
   ```
