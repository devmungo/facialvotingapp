<p align="left">
  <a href="https://www.linkedin.com/in/luckymungomeni/" target="_blank"><img alt="LinkedIn" title="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>

# About The Project
The online voting application is designed to provide secure, accessible, and efficient voting capabilities for the citizens of South Africa. Leveraging the Cloud Infrastructure of Amazon Web Services (AWS), the application ensures the integrity of the electoral process while promoting inclusivity and transparency. It incorporates various AWS services to address security concerns, handle scalability, and provide a seamless user experience.

Some of the features of this project includes login, registration, email verification, facial recognition, Ballot, toting, live result talying as well as profile management. This application has been hosted at AWS Fargate.

Architecture

<img src="https://github.com/devmungo/facialvotingapp/blob/main/Final%20Architecture.png">


# Setup Instructions

1. Clone the repository `git clone https://github.com/devmungo/facialvotingapp.git`
2. Open the project from the code editor `code .` or `atom .`
3. Create virtual environment `python -m venv env`
4. Activate the virtual environment `source env/Scripts/activate`
5. Install required packages to run the project `pip install -r requirements.txt`
6. Fill up the environment variables
7. Create database tables
    ```sh
    python manage.py migrate
    ```
8. Create a super user
    ```sh
    python manage.py createsuperuser
    ```
    _GitBash users may have to run this to create a super user - `winpty python manage.py createsuperuser`_
9. Run server
    ```sh
    python manage.py runserver
    ```
10. Login to admin panel - (`http://127.0.0.1:8000/admin`)


[Check Live Demo](http://anomip.com/)


## Support
😀 If you like this project, give it a ⭐ and share it with friends!

<p align="left">
  <a href="https://www.youtube.com/@anomip"><img alt="YouTube" title="YouTube" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"/></a>
</p>

## Contact Me
<p align="left">
  <a href="https://www.linkedin.com/in/luckymungomeni/"><img alt="LinkedIn" title="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:developer.mungomenil@gmail.com"><img alt="Gmail" title="Gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>


