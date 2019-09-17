# Solar System

## Build and Run Instructions
1. Download latest version of Python 3 from `https://www.python.org/downloads/`.
2. Add Python to PATH
3. upgrade pip `python -m pip install pip --upgrade`
3. Download virtialenv through pip command: `pip install virtualenv`
4. Setup virtualenv for the project run : `virtualenv solar-system`
5. Start the virtualenv with `source solar-system/Scripts/activate` or `source solar-system/bin/activate`
6. Install all dependencies from `requirements.txt`. Run : `pip install -r requirements.txt`
7. To run, `python __main__.py`.

## Info
The following program uses the three-step Beeman scheme. 
The Beeman algorithm is a stable method which predicts the position at the next 
time step by combining the current acceleration with the acceleration from the 
previous time step. This new position can then be used to calculate the new 
acceleration which, in turn, predicts the new velocity. The algorithm is given by:
___
![equation](https://latex.codecogs.com/svg.latex?%5Cvec%20r%28t%20&plus;%20%5CDelta%20t%29%20%3D%20%5Cvec%20r%28t%29%20&plus;%20%5Cvec%20v%20%28t%29%5CDelta%20t%20&plus;%20%5Cfrac%7B1%7D%7B6%7D%5B4%5Cvec%20a%20%28t%29%20-%20%5Cvec%20a%28t-%20%5CDelta%20t%29%5D%5CDelta%20t%5E2)
![equation](https://latex.codecogs.com/svg.latex?%5Cvec%20v%28t%20&plus;%20%5CDelta%20t%29%20%3D%20%5Cvec%20v%28t%29%20&plus;%20%5Cfrac%7B1%7D%7B6%7D%5B2%5Cvec%20a%20%28t%20&plus;%20%5CDelta%20t%29%20&plus;%205%5Cvec%20a%28t%29%20-%20%5Cvec%20a%20%28t-%20%5CDelta%20t%29%5D%5CDelta%20t)
___