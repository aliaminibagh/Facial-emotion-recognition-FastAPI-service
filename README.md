# Facial-emotion-recognition-FastAPI-service

<!-- TABLE OF CONTENTS -->
<details>
  <summary >Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#usage">usage</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

# About The Project!

This repository aims to provide dockerized, convenient, easy deployable and scalable REST API for face detection and emotion recognition pipeline using FastAPI.
Use the `README.md` to get started.

# Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](python.org/)
* [pytorch](https://pytorch.org/)
* [OpenCV](https://opencv.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://www.docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
# Getting Started
To get a local copy up and running follow these simple example steps.
### Prerequisites
* Docker
 Download docker engine according to your OS. [Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=header) [Linux](https://hub.docker.com/search?offering=community&operating_system=linux&q=&type=edition) [Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=header)

### Usage

To run the API,  after install `docker`, execute the following commands:

 - **Create Docker Image**
  ```sh
  docker build -t face_emotion_recognition:1.0 .
  ```
- **Run Docker Container**
 ```sh
  docker run -p 8000:8000 -d face_emotion_recognition:1.0 
  ```
- **Start FastAPI Service**

open the browser and write `localhost:8000/docs` in the url place
- **Test The Service**

For using service see the demo video !
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b features`)
3. Commit your Changes (`git commit -m 'Add some Features'`)
4. Push to the Branch (`git push origin features`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ali Amini Bagh -  aliaminibagh@gmail.com

Project Link: [Facial-emotion-recognition-FastAPI-service](https://github.com/aliaminibagh/Facial-emotion-recognition-FastAPI-service)
